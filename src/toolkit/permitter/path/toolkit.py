# src/toolkit/permitter/path/toolkit.py

"""
Module: toolkit.permitter.path.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from err import PathNullException
from model import Path
from toolkit import PermitterToolkit
from validation import SquareValidator

@dataclass
class PathToolkit(PermitterToolkit):
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
        permitter: Path

    Provides:

    Super Class:
        Toolkit
    """
    square_validator: SquareValidator = SquareValidator()
    null_exception: PathNullException = PathNullException()
    permitter: Path = Path


    