# src/assurance/validator/model/token/common/safe/table.py

"""
Module: assurance.validator.model.token.common.table.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from assurance import Walk
from domain import Coord, Formation, HomeSquare, Team, TokenDeployment


class SafeSuperTokenPropertyTable:
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Token super class properties that are safe.

    Attributes:
        id: int
        team: Team
        formation: Formation
        home_square: HomeSquare
        deployment: TokenDeployment
        position_log: Walk

    Provides:

    Super Class:
    """
    _id: int
    _team: Team
    _formation: Formation
    _home_square: HomeSquare
    _deployment: TokenDeployment
    _position_log: Walk
    
    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            deployment: TokenDeployment,
            position_table: Walk,
    ):
        """
            id: int
            team: Team
            formation: Formation
            home_square: HomeSquare
            deployment: TokenDeployment
            position_log: Walk
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
    def position_log(self) -> Walk:
        return self._position_log
    
    @property
    def prime_extract(self) -> TokenPrimeExtract:
        return self._prime_extract
    
    @property
    def position(self) -> Optional[Coord]:
        return self._position_log.position
    
    @property
    def previous_position(self) -> Optional[Coord]:
        return self._position_log.previous_position
    