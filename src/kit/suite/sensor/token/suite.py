# src/kit/suite/detector/carrier_validator/toolkit.detector.py

"""
Module: kit.detector.suite.carrier_validator.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from kit import SensorSuite
from model import Token
from sensor import FriendshipAnalyzer, TokenCollider, TokenHomeReporter, TokenReadinessAnalyzer


class TokenSensorSuite(SensorSuite[Token]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

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
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    friendship: FriendshipAnalyzer = FriendshipAnalyzer()
    collider: TokenCollider = TokenCollider()
    readiness: TokenReadinessAnalyzer = TokenReadinessAnalyzer()
    home: TokenHomeReporter = TokenHomeReporter()

