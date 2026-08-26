# src/operation/toolkit/analyzer/path/toolkit.py

"""
Module: operation.toolkit.analyzer.path.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from err import PathNullException
from sensor.analyzer import Path
from transit.dispatcher.validator import SquareValidationDispatcher

@dataclass
class PathToolkit(AnalyzerToolkit):
    """
    Role:
        -  Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Path tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        square_validator: SquareValidator
        null_exception: PathNullException
        analyzer: Path

    Provides:

    Super Class:
        Toolkit
    """
    square_validator: SquareValidationDispatcher = SquareValidationDispatcher()
    null_exception: PathNullException = PathNullException()
    analyzer: Path = Path


    