# src/assurance/depend/service/model/token/depend.py

"""
Module: assurance.depend.service.model.token.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ServiceDependency
from domain import Token
from exchange import (
    AlertValidationService, RankValidationService,
    SquareValidationService, TeamValidationService, FootstepValidationService
)


class TokenServiceDependency(ServiceDependency[Token]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy TokenValidator's ValidationService dependencies.

    Attributes:
        team: TeamValidationService
        rank: RankValidationService
        alert: AlertValidationService
        square: SquareValidationService
        footstep: FootstepValidationService
        
    Provides:

    Super Class:
        Dependency
    """
    _team: TeamValidationService
    _rank: RankValidationService
    _alert: AlertValidationService
    _square: SquareValidationService
    _footstep: FootstepValidationService
    
    def __init__(
            self,
            team: Optional[TeamValidationService] | None = None,
            rank: Optional[RankValidationService] | None = None,
            alert: Optional[AlertValidationService] | None = None,
            square: Optional[SquareValidationService] | None = None,
            footstep: Optional[FootstepValidationService] | None = None,
    ):
        """
        Args:
            team: Optional[TeamValidatorClient]
            rank: Optional[RankValidatorClient]
            alert: Optional[AlertValidationService]
            square: Optional[SquareValidationService]
            footstep: Optional[FootstepValidationService]
        """
        super().__init__()
        self._team = team or TeamValidationService()
        self._rank = rank or RankValidationService()
        self._alert = alert or AlertValidationService()
        self._square = square or SquareValidationService()
        self._footstep = footstep or FootstepValidationService()
    
    @property
    def team(self) -> TeamValidationService:
        return self._team
    
    @property
    def rank(self) -> RankValidationService:
        return self._rank
    
    @property
    def alert(self) -> AlertValidationService:
        return self._alert
    
    @property
    def square(self) -> SquareValidationService:
        return self._square
    
    @property
    def footstep(self) -> FootstepValidationService:
        return self._footstep