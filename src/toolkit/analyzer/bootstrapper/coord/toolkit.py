# src/toolkit/analyzer/coord/toolkit.py

"""
Module: toolkit.analyzer.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from analyzer import Coord
from toolkit import AnalyzerBootstrapperToolkit
from validator import NumberValidator, PrimingValidator


@dataclass
class CoordToolkit(AnalyzerBootstrapperToolkit[Coord]):
    """
    Role:
        -   Dependency Management

    Responsibilities:
        1.  Aggregates workers and services a Coord requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        number_validator: NumberValidator
        priming_validator: PrimingValidator

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:
        
    Super Class:
        Toolkit
    """
    number_validator: NumberValidator = NumberValidator()
    priming_validator: PrimingValidator = PrimingValidator()
