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
    AlertValidationResponseWrapper, RankValidationResponseWrapper,
    SquareValidationResponseWrapper, TeamValidationResponseWrapper, FootstepValidationResponseWrapper
)


class TokenWrapperDependency(ModelWrapperDependency[Token]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy TokenValidator's ResponseWrapper dependencies.

    Attributes:
        team: TeamValidationResponseWrapper
        rank: RankValidationResponseWrapper
        alert: AlertValidationResponseWrapper
        square: SquareValidationResponseWrapper
        footstep: FootstepValidationResponseWrapper
        
    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _team: TeamValidationResponseWrapper
    _rank: RankValidationResponseWrapper
    _alert: AlertValidationResponseWrapper
    _square: SquareValidationResponseWrapper
    _footstep: FootstepValidationResponseWrapper
    
    def __init__(
            self,
            team: Optional[TeamValidationResponseWrapper] | None = None,
            rank: Optional[RankValidationResponseWrapper] | None = None,
            alert: Optional[AlertValidationResponseWrapper] | None = None,
            square: Optional[SquareValidationResponseWrapper] | None = None,
            footstep: Optional[FootstepValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            team: Optional[TeamValidatorClient]
            rank: Optional[RankValidatorClient]
            alert: Optional[AlertValidationResponseWrapper]
            square: Optional[SquareValidationResponseWrapper]
            footstep: Optional[FootstepValidationResponseWrapper]
        """
        super().__init__()
        self._team = team or TeamValidationResponseWrapper()
        self._rank = rank or RankValidationResponseWrapper()
        self._alert = alert or AlertValidationResponseWrapper()
        self._square = square or SquareValidationResponseWrapper()
        self._footstep = footstep or FootstepValidationResponseWrapper()
    
    @property
    def team(self) -> TeamValidationResponseWrapper:
        return self._team
    
    @property
    def rank(self) -> RankValidationResponseWrapper:
        return self._rank
    
    @property
    def alert(self) -> AlertValidationResponseWrapper:
        return self._alert
    
    @property
    def square(self) -> SquareValidationResponseWrapper:
        return self._square
    
    @property
    def footstep(self) -> FootstepValidationResponseWrapper:
        return self._footstep