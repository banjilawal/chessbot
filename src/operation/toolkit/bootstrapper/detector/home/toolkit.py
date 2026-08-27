# src/operation/toolkit/carrier_validator/token/toolkit.py

"""
Module: operation.toolkit.carrier_validator.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from bootstrapper import HomeDetectorBootstrapper
from err import BoardValidatorException
from microservice import IdentityService
from operation.toolkit.bootstrapper.detector.home.toolkit import BootstrapperToolkit
from transit.dispatcher.validator import BoardValidationDispatcher, TokenHomeContextValidator, TokenValidationDispatcher


@dataclass
class HomeDetectorBootstrapperToolkit(BootstrapperToolkit[HomeDetectorBootstrapper]):
    """
    Role:
        - Dependency Management

    Responsibilities:
        1.  Bundles dependencies a worker needs to complete its task.
        2.  Loose Coupling between an operation and its resources.
        3.  Simplify Entry points.

    Attributes:
        board_validator: BoardValidator
        token_validator: TokenValidator
        identity_service: IdentityService

    Provides:
        -  def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        DetectorBootstrapperToolkit
    """
    board_validator: BoardValidationDispatcher = BoardValidatorException()
    token_validator: TokenValidationDispatcher = TokenValidationDispatcher()
    identity_service: IdentityService = IdentityService()
    context_validator: TokenHomeContextValidator = TokenHomeContextValidator()