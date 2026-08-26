# src/operation/suite/operation/token/suite.py

"""
Module: operation.suite.operation.token.suite
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from assurance import TokenValidator
from fabrication import TokenBuilder
from kit import OperationSuite, TokenSensorSuite, TokenToolkit
from domain.model import Token
from operation import PawnPromoter


class TokenOperationSuite(OperationSuite[Token]):
    """
    Role:
        -  Dependency Container
        -  Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Token.

    Attributes:
        toolkit: TokenToolkit
        builder: TokenBuilder
        validator: TokenValidator

    Provides:

    Super Class:
        Suite

    Notes:
        -  Suite for an empty class which makes managing toolkits easier.
        -  Any toolkits for a suite should be a Suite subclass.
    """
    toolkit: TokenToolkit = TokenToolkit()
    builder: TokenBuilder = TokenBuilder()
    validator: TokenValidator = TokenValidator()
    
    promoter: PawnPromoter = PawnPromoter()
    sensor: TokenSensorSuite = TokenSensorSuite()

