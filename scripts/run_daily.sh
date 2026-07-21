#!/usr/bin/env bash
# Daily paper pipeline: fetch -> score -> generate report
# Usage: ./scripts/run_daily.sh [YYYY-MM-DD] [--no-llm]
#   Default: yesterday's date

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$SCRIPT_DIR/data"

# A weekday with zero arXiv records is usually an API/indexing propagation issue,
# not a normal empty publication day.  Retry before declaring the run failed.
# Environment overrides keep the behavior tunable in cron or during testing.
ZERO_PAPER_MAX_ATTEMPTS="${ZERO_PAPER_MAX_ATTEMPTS:-4}"
ZERO_PAPER_RETRY_DELAY_SECONDS="${ZERO_PAPER_RETRY_DELAY_SECONDS:-300}"

# Parse arguments
TARGET_DATE=""
NO_LLM=""
DAYS=1   # Default: fetch only the target arXiv day to avoid repeated daily picks

for arg in "$@"; do
    case "$arg" in
        --no-llm)
            NO_LLM="--no-llm"
            ;;
        --days=*)
            DAYS="${arg#--days=}"
            ;;
        *)
            if [ -z "$TARGET_DATE" ]; then
                TARGET_DATE="$arg"
            fi
            ;;
    esac
done

# Default to the last arXiv working day if no date provided.
# arXiv does not publish on weekends: if today is Monday, use Friday;
# if today is Sunday, use Friday; if today is Saturday, use Friday.
# For all other days, use yesterday.
if [ -z "$TARGET_DATE" ]; then
    TODAY_DOW=$(date +%u)   # 1=Mon ... 7=Sun (ISO weekday)
    case "$TODAY_DOW" in
        1) DAYS_BACK=3 ;;   # Monday   -> Friday (3 days back)
        7) DAYS_BACK=2 ;;   # Sunday   -> Friday (2 days back)
        6) DAYS_BACK=1 ;;   # Saturday -> Friday (1 day back)
        *) DAYS_BACK=1 ;;   # Tue-Fri  -> yesterday
    esac
    TARGET_DATE=$(date -d "$DAYS_BACK days ago" +%Y-%m-%d 2>/dev/null || date -v-${DAYS_BACK}d +%Y-%m-%d)
fi

echo "========================================" >&2
echo " Daily Paper Pipeline" >&2
echo " Date: $TARGET_DATE (last $DAYS days)" >&2
echo " Scoring: Paper Evaluation SOP (deterministic)" >&2
if [ -n "$NO_LLM" ]; then
    echo " Note: --no-llm is retained for compatibility; SOP scoring does not use LLM." >&2
fi
echo "========================================" >&2

mkdir -p "$DATA_DIR"

FETCH_FILE="$DATA_DIR/${TARGET_DATE}_fetched.json"
SCORED_FILE="$DATA_DIR/${TARGET_DATE}_scored.json"

# Step 1: Fetch papers
# arXiv has no weekend announcements.  On a weekday, a zero result is retried
# because export.arxiv.org can temporarily lag the public announcement index.
echo "" >&2
echo "[1/3] Fetching papers from arXiv..." >&2
TARGET_DOW=$(date -d "$TARGET_DATE" +%u 2>/dev/null || date -j -f %Y-%m-%d "$TARGET_DATE" +%u)
IS_WEEKDAY=false
if [ "$TARGET_DOW" -le 5 ]; then
    IS_WEEKDAY=true
fi

PAPER_COUNT=0
for ((attempt=1; attempt<=ZERO_PAPER_MAX_ATTEMPTS; attempt++)); do
    python3 "$SCRIPT_DIR/fetch_papers.py" \
        --date "$TARGET_DATE" \
        --days "$DAYS" \
        --config "$SCRIPT_DIR/config.yaml" \
        --output "$FETCH_FILE"

    PAPER_COUNT=$(python3 -c "import json; d=json.load(open('$FETCH_FILE')); print(d['total_papers'])")
    echo "  -> Fetched $PAPER_COUNT papers (attempt $attempt/$ZERO_PAPER_MAX_ATTEMPTS)" >&2

    if [ "$PAPER_COUNT" -gt 0 ] || [ "$IS_WEEKDAY" = false ]; then
        break
    fi
    if [ "$attempt" -lt "$ZERO_PAPER_MAX_ATTEMPTS" ]; then
        echo "  Weekday zero-result: retrying in ${ZERO_PAPER_RETRY_DELAY_SECONDS}s (arXiv index may be lagging)." >&2
        sleep "$ZERO_PAPER_RETRY_DELAY_SECONDS"
    fi
done

if [ "$PAPER_COUNT" -eq 0 ]; then
    if [ "$IS_WEEKDAY" = true ]; then
        echo "ERROR: arXiv returned 0 papers for weekday $TARGET_DATE after $ZERO_PAPER_MAX_ATTEMPTS attempts." >&2
        exit 2
    fi
    echo "  No papers found for weekend target $TARGET_DATE; no report generated." >&2
    echo "  Pipeline complete (no report generated)." >&2
    exit 0
fi

# Step 2: Score papers
echo "" >&2
echo "[2/3] Scoring papers with Paper Evaluation SOP..." >&2
python3 "$SCRIPT_DIR/score_papers_sop.py" \
    "$FETCH_FILE" \
    --config "$SCRIPT_DIR/config.yaml" \
    --output "$SCORED_FILE"

SCORED_SUMMARY=$(python3 -c "import json; d=json.load(open('$SCORED_FILE')); print(f\"{d['after_filter']} relevant ({d['selected_count']} selected, {d['watch_count']} watch; {d['filtered_count']} filtered)\")")
echo "  -> $SCORED_SUMMARY" >&2

# Step 3: Generate report
echo "" >&2
echo "[3/3] Generating daily report..." >&2
python3 "$SCRIPT_DIR/generate_report.py" \
    "$SCORED_FILE" \
    --config "$SCRIPT_DIR/config.yaml"

echo "" >&2
echo "========================================" >&2
echo " Pipeline complete!" >&2
echo " Data: $DATA_DIR/" >&2
echo " Report: $REPO_ROOT/literature/notes/${TARGET_DATE}_Daily_Papers.md" >&2
echo "========================================" >&2
