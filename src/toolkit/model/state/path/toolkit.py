# src/toolkit/model/path/toolkit.py

"""
Module: toolkit.model.path.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from err import PathNullException
from model import Path
from toolkit import ModelToolkit
from validator import SquareValidator

@dataclass
class PathToolkit(ModelToolkit):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Path tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        square_validator: SquareValidator
        null_exception: PathNullException
        model: Path

    Provides:

    Super Class:
       ModelToolkit
    """
    square_validator: SquareValidator = SquareValidator()
    null_exception: PathNullException = PathNullException()
    model: Path = Path


    