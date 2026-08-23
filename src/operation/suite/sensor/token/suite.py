# src/operation/suite/detector/carrier_validator/toolkit.detector.py

"""
Module: kit.detector.suite.carrier_validator.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from kit import SensorSuite
from domain.model import Token
from sensor import FriendshipAnalyzer, TokenCollider, TokenHomeReporter, TokenReadinessAnalyzer


class TokenSensorSuite(SensorSuite[Token]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Token.

    Attributes:
        collider: Optional[TokenCollider]
        home: Optional[TokenHomeReporter]
        friendship: Optional[FriendshipAnalyzer]
        readiness: Optional[TokenReadinessAnalyzer]

    Provides:

    Super Class:
        SensorSuite
    """
    _collider: TokenCollider
    _home: TokenHomeReporter
    _friendship: FriendshipAnalyzer
    _readiness: TokenReadinessAnalyzer
    
    def __init__(
            self,
            collider: Optional[TokenCollider] | None = None,
            home: Optional[TokenHomeReporter] | None = None,
            friendship: Optional[FriendshipAnalyzer] | None = None,
            readiness: Optional[TokenReadinessAnalyzer] | None = None,
    ):
        """
        Args:
            collider: Optional[TokenCollider]
            home: Optional[TokenHomeReporter]
            friendship: Optional[FriendshipAnalyzer]
            readiness: Optional[TokenReadinessAnalyzer]
        """
        self._collider = collider or TokenCollider()
        self._home = home or TokenHomeReporter()
        self._friendship = friendship or FriendshipAnalyzer()
        self._readiness = readiness or TokenReadinessAnalyzer()
        
    @property
    def home(self) -> TokenHomeReporter:
        return self._home
    
    @property
    def collider(self) -> TokenCollider:
        return self._collider
    
    @property
    def friendship(self) -> FriendshipAnalyzer:
        return self._friendship
    
    @property
    def readiness(self) -> TokenReadinessAnalyzer:
        return self._readiness

