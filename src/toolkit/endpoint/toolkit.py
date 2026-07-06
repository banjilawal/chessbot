# src/toolkit/endpoint/toolkit.py

"""
Module: toolkit.endpoint.toolkit
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
from validator import SquareValidator, TokenValidator


class TokenEndpointRelationToolkit(Toolkit):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services a Endpoint object requires for its tasks.
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
        
    Notes:
        -   The toolkit does not support any models. It just makes TokenOriging and TokenDestination RelationValidator
            method signatures simpler.
    """

    DEPENDENCIES: List[Operation] = []
    SERVICE_DEPENDENCIES: List[Microservice] = []

    token_validator: TokenValidator = TokenValidator()
    square_validator: SquareValidator = SquareValidator()
    relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer()