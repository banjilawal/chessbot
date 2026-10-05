# src/assurance/data/data/token/table.py

"""
Module: transit.delivery.token.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import (
    CoordChart, Formation, HomeSquare, Team, Token, TokenDeployment,
    TokenPrimeExtract
)
from transit import ProductEnvelope


class RootTokenEnvelope(ProductEnvelope[Token]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores Token super class properties that are reference.

    Attributes:
        id: int
        team: Team
        walk: CoordChart
        formation: Formation
        home_square: HomeSquare
        deployment: TokenDeployment
        prime_extract: TokenPrimeExtract

    Provides:

    Super Class:
        ProductEnvelopeTable
    """
    _id: int
    _team: Team
    _walk: CoordChart
    _formation: Formation
    _home_square: HomeSquare
    _deployment: TokenDeployment
    

    def __init__(
            self,
            id: int,
            team: Team,
            walk: CoordChart,
            formation: Formation,
            home_square: HomeSquare,
            deployment: TokenDeployment,
            prime_extract: TokenPrimeExtract,
    ):
        """
        Args:
            id: int
            team: Team
            walk: CoordChart
            formation: Formation
            home_square: HomeSquare
            deployment: TokenDeployment
            prime_extract: TokenPrimeExtract
        """
        super().__init__(prime_extract=prime_extract)
        self._id = id
        self._team = team
        self._walk = walk
        self._formation = formation
        self._home_square = home_square
        self._deployment = deployment
    
    @property
    def prime_extract(self) -> TokenPrimeExtract:
        return cast(TokenPrimeExtract, super().prime_extract)
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def walk(self) -> CoordChart:
        return self._walk
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def home_square(self) -> HomeSquare:
        return self._home_square
    
    @property
    def deployment(self) -> TokenDeployment:
        return self._deployment

