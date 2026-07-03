# src/toolkit/origin/toolkit.py

"""
Module: toolkit.origin.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from analyzer import SquareTokenRelationAnalyzer
from microservice import Microservice
from operation import Operation
from toolkit import Toolkit
from validation import SquareValidator, TokenValidator


class TokenOriginRelationToolkit(Toolkit):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services a Origin object requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        token_validator: TokenValidator = TokenValidator()
        square_validator: SquareValidator = SquareValidator()
        relation_analyzer: SquareTokenRelationAnalyzer

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        Toolkit
    """

    DEPENDENCIES: List[Operation] = []
    SERVICE_DEPENDENCIES: List[Microservice] = []

    token_validator: TokenValidator = TokenValidator()
    square_validator: SquareValidator = SquareValidator()
    relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer()