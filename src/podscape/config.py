from pathlib import Path
from typing import Union

PROJECT_ROOT = Path(__file__).parent.absolute()

def get_project_root() -> Path:
    return PROJECT_ROOT
