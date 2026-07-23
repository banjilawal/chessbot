# src/toolkit/carrier_validator/token/toolkit.py

"""
Module: toolkit.carrier_validator.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from bootstrapper import HomeDetectorBootstrapper
from err import BoardValidatorException
from microservice import IdentityService
from toolkit import BootstrapperToolkit
from validator import BoardValidator, TokenHomeContextValidator, TokenValidator


@dataclass
class HomeDetectorBootstrapperToolkit(BootstrapperToolkit[HomeDetectorBootstrapper]):
    """
    Role:
        -   Dependency Management

    Responsibilities:
        1.  Bundles dependencies a worker needs to complete its task.
        2.  Loose Coupling between an operation and its resources.
        3.  Simplify Entry points.

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