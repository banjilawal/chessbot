# src/toolkit/coord/toolkit.py

"""
Module: toolkit.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import Coord
from toolkit import Toolkit
from validation import NumberValidator, ValidationPrimer


@dataclass
class CoordToolkit(Toolkit[Coord]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services a Coord requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        number_validator: NumberValidator
        validation_primer: ValidationPrimer

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:
        
    Super Class:
        Toolkit
    """
    number_validator: NumberValidator = NumberValidator()
    validation_primer: ValidationPrimer = ValidationPrimer()
