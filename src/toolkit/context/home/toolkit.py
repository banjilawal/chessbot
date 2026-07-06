# src/toolkit/context/home/toolkit.py

"""
Module: toolkit.context.home.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from context import TokenHomeContext
from err import BoardValidatorException, ContextNullException, TokenHomeContextNullException
from microservice import IdentityService
from toolkit import TokenToolkit, Toolkit
from validation import BoardValidator, TokenValidator


@dataclass
class TokenHomeContextToolkit(Toolkit[TokenHomeContext]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services an entity requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        board_validator: BoardValidator
        token_validator: TokenValidator
        identity_service: IdentityService
        null_exception: TokenHomeContextNullException
        model: TokenHomeContext

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        DetectorBootstrapperToolkit
    """

    model_toolkit: TokenToolkit = TokenToolkit()
    board_validator: BoardValidator = BoardValidatorException()
    token_validator: TokenValidator = TokenValidator()
    context_model: TokenHomeContext = Type[TokenHomeContext]
    context_null_exception: ContextNullException = TokenHomeContextNullException()
    
    