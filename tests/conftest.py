from pathlib import Path

import pytest
import yaml


@pytest.fixture
def sop_config():
    return yaml.safe_load(Path("scripts/config.yaml").read_text())["sop"]
