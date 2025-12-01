# src/utils.py
import yaml
import logging
from pathlib import Path

def load_config(path: str):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def setup_logger(log_path: str = "logs/run.log", level: str = "INFO"):
    level_obj = getattr(logging, level.upper(), logging.INFO)
    logger = logging.getLogger("dq_checker")
    logger.setLevel(level_obj)
    if not logger.handlers:
        fh = logging.FileHandler(log_path)
        fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(fmt)
        logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        logger.addHandler(ch)
    return logger
