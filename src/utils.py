import yaml
from pathlib import Path

DATA_PATH = Path("../data/")
CONFIG_PATH = DATA_PATH / "config.yml"

with open(CONFIG_PATH, mode="r") as fp:
    config = yaml.safe_load(fp)
