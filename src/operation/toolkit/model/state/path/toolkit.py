# src/operation/toolkit/model/path/toolkit.py

"""
Module: operation.toolkit.model.path.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from err import PathNullException
from domain.model import Path
from operation.toolkit.model.state.path.toolkit import StateModelToolkit
from assurance.validator import SquareValidator

@dataclass
class PathToolkit(StateModelToolkit):
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
    model: Type[Path] = Path


    