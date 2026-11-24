from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = BASE_DIR / "models"
DOCS_DIR = BASE_DIR / "docs"

PROJECT_NAME = "SevanEco AI"
PROJECT_REGION = "Lake Sevan, Armenia"
RANDOM_STATE = 42
