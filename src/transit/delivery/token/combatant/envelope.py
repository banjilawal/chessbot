# src/transit/delivery/token/combatant/envelope.py

"""
Module: transit.delivery.token.combatant.envelope
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    CombatantReadiness, Footstep, Formation, HomeSquare, Team, Token,
    TokenDeployment, TokenPrimeExtract
)
from transit import RootTokenEnvelope


class CombatantTokenEnvelope(RootTokenEnvelope):
    """
    Role
        -   Data Transfer

    Responsibilities:
        1.  Data from a RooTokenValidator forwarded to client validators.

    Attributes:
        readiness: CombatantReadiness
        captor: Optional[Token]

    Provides:

    Super Class:
        RootTokenEnvelope
    """
    _id: int
    _team: Team
    _footstep: Footstep
    _formation: Formation
    _home_square: HomeSquare
    _deployment: TokenDeployment
    _readiness: CombatantReadiness
    _captor: Optional[Token]

    def __init__(
            self,
            id: int,
            team: Team,
            footstep: Footstep,
            formation: Formation,
            home_square: HomeSquare,
            deployment: TokenDeployment,
            readiness: CombatantReadiness,
            prime_extract: TokenPrimeExtract,
            captor: Optional[Token] | None = None,
    ):
        """
        Args:
            id: int
            team: Team
            footstep: Footstep
            formation: Formation
            home_square: HomeSquare
            deployment: TokenDeployment
            readiness: CombatantReadiness
            prime_extract: TokenPrimeExtract
            captor: Optional[Token]
        """
        super().__init__(
            id=id,
            team=team,
            footstep=footstep,
            formation=formation,
            home_square=home_square,
            deployment=deployment,
            prime_extract=prime_extract,
        )
        self._captor = captor
        self._readiness = readiness
    
    @property
    def prime_extract(self) -> TokenPrimeExtract:
        return cast(TokenPrimeExtract, super().prime_extract)
    
    @property
    def captor(self) -> Optional[Token]:
        return self._captor
    
    @property
    def readiness(self) -> CombatantReadiness:
        return self._readiness

