# src/toolkit/bootstrapper/token/toolkit.py

"""
Module: toolkit.bootstrapper.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from bootstrap import HomeDetectorBootstrapper
from err import BoardValidatorException
from microservice import IdentityService
from toolkit import BootstrapperToolkit
from validation import BoardValidator, TokenHomeContextValidator, TokenValidator


@dataclass
class HomeDetectorBootstrapperToolkit(BootstrapperToolkit[HomeDetectorBootstrapper]):
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

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        DetectorBootstrapperToolkit
    """
    board_validator: BoardValidator = BoardValidatorException()
    token_validator: TokenValidator = TokenValidator()
    identity_service: IdentityService = IdentityService()
    context_validator: TokenHomeContextValidator = TokenHomeContextValidator()