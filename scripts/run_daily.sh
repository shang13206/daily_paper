#!/usr/bin/env bash
# Daily paper pipeline: fetch -> score -> generate report
# Usage: ./scripts/run_daily.sh [YYYY-MM-DD] [--no-llm]
#   Default: yesterday's date

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$SCRIPT_DIR/data"

# Parse arguments
TARGET_DATE=""
NO_LLM=""

for arg in "$@"; do
    case "$arg" in
        --no-llm)
            NO_LLM="--no-llm"
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
echo " Date: $TARGET_DATE" >&2
if [ -n "$NO_LLM" ]; then
    echo " LLM Scoring: DISABLED" >&2
fi
echo "========================================" >&2

mkdir -p "$DATA_DIR"

FETCH_FILE="$DATA_DIR/${TARGET_DATE}_fetched.json"
SCORED_FILE="$DATA_DIR/${TARGET_DATE}_scored.json"

# Step 1: Fetch papers
echo "" >&2
echo "[1/3] Fetching papers from arXiv..." >&2
python3 "$SCRIPT_DIR/fetch_papers.py" \
    --date "$TARGET_DATE" \
    --config "$SCRIPT_DIR/config.yaml" \
    --output "$FETCH_FILE"

# Check if we got any papers
PAPER_COUNT=$(python3 -c "import json; d=json.load(open('$FETCH_FILE')); print(d['total_papers'])")
echo "  -> Fetched $PAPER_COUNT papers" >&2

if [ "$PAPER_COUNT" -eq 0 ]; then
    echo "  No papers found for $TARGET_DATE. This may be normal (weekends/holidays)." >&2
    echo "  Pipeline complete (no report generated)." >&2
    exit 0
fi

# Step 2: Score papers
echo "" >&2
echo "[2/3] Scoring and filtering papers..." >&2
python3 "$SCRIPT_DIR/score_papers.py" \
    "$FETCH_FILE" \
    --config "$SCRIPT_DIR/config.yaml" \
    --output "$SCORED_FILE" \
    $NO_LLM

SCORED_COUNT=$(python3 -c "import json; d=json.load(open('$SCORED_FILE')); print(len(d['papers']))")
echo "  -> $SCORED_COUNT papers after filtering" >&2

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
