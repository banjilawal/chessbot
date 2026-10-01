# src/assurance/reference/property/token/table.py

"""
Module: assurance.reference.property.token.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from __future__ import annotations

from typing import Optional

from assurance import ReferencePropertyTable, TokenPositionChart
from domain import Coord, Formation, HomeSquare, Team, Token, TokenDeployment


class TokenReferencePropertyTable(ReferencePropertyTable[Token]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Token super class properties that are reference.

    Attributes:
        id: int
        team: Team
        formation: Formation
        home_square: HomeSquare
        deployment: TokenDeployment
        position_log: TokenPositionChart

    Provides:

    Super Class:
    """
    _id: int
    _team: Team
    _formation: Formation
    _home_square: HomeSquare
    _deployment: TokenDeployment
    _position_log: TokenPositionChart
    
    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            deployment: TokenDeployment,
            position_table: TokenPositionChart,
    ):
        """
            id: int
            team: Team
            formation: Formation
            home_square: HomeSquare
            deployment: TokenDeployment
            position_log: TokenPositionChart
        """
        self._id = id
        self._team = team
        self._formation = formation
        self._home_square = home_square
        self._deployment = deployment
        self._position_log = position_table
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def home_square(self) -> HomeSquare:
        return self._home_square
    
    @property
    def deployment(self) -> TokenDeployment:
        return self._deployment
    
    @property
    def position_log(self) -> TokenPositionChart:
        return self._position_log
    
    @property
    def position(self) -> Optional[Coord]:
        return self._position_log.position
    
    @property
    def previous_position(self) -> Optional[Coord]:
        return self._position_log.previous_position
