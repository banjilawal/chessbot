# src/assurance/depend/wrapper/model/token/depend.py

"""
Module: assurance.depend.wrapper.model.token.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Token
from exchange import (
    AlertValidationServer, RankValidationServer,
    SquareValidationServer, TeamValidationServer, FootstepValidationServer
)


class TokenWrapperDependency(ModelWrapperDependency[Token]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy TokenValidator's ResponseWrapper dependencies.

    Attributes:
        team: TeamValidationServer
        rank: RankValidationServer
        alert: AlertValidationServer
        square: SquareValidationServer
        footstep: FootstepValidationServer
        
    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _team: TeamValidationServer
    _rank: RankValidationServer
    _alert: AlertValidationServer
    _square: SquareValidationServer
    _footstep: FootstepValidationServer
    
    def __init__(
            self,
            team: Optional[TeamValidationServer] | None = None,
            rank: Optional[RankValidationServer] | None = None,
            alert: Optional[AlertValidationServer] | None = None,
            square: Optional[SquareValidationServer] | None = None,
            footstep: Optional[FootstepValidationServer] | None = None,
    ):
        """
        Args:
            team: Optional[TeamValidatorClient]
            rank: Optional[RankValidatorClient]
            alert: Optional[AlertValidationServer]
            square: Optional[SquareValidationServer]
            footstep: Optional[FootstepValidationServer]
        """
        super().__init__()
        self._team = team or TeamValidationServer()
        self._rank = rank or RankValidationServer()
        self._alert = alert or AlertValidationServer()
        self._square = square or SquareValidationServer()
        self._footstep = footstep or FootstepValidationServer()
    
    @property
    def team(self) -> TeamValidationServer:
        return self._team
    
    @property
    def rank(self) -> RankValidationServer:
        return self._rank
    
    @property
    def alert(self) -> AlertValidationServer:
        return self._alert
    
    @property
    def square(self) -> SquareValidationServer:
        return self._square
    
    @property
    def footstep(self) -> FootstepValidationServer:
        return self._footstep