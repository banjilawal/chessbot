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
    CoordValidationResponseWrapper, RankValidationResponseWrapper,
    SquareValidationResponseWrapper, TeamValidationResponseWrapper
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
        coord: CoordValidationResponseWrapper
        square: SquareValidationResponseWrapper
        
    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _team: TeamValidationResponseWrapper
    _rank: RankValidationResponseWrapper
    _coord: CoordValidationResponseWrapper
    _square: SquareValidationResponseWrapper
    
    def __init__(
            self,
            team: Optional[TeamValidationResponseWrapper] | None = None,
            rank: Optional[RankValidationResponseWrapper] | None = None,
            coord: Optional[CoordValidationResponseWrapper] | None = None,
            square: Optional[SquareValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            team: Optional[TeamValidatorClient]
            rank: Optional[RankValidatorClient]
            coord: Optional[CoordValidatorClient]
            square: Optional[SquareValidatorClient]
        """
        super().__init__()
        self._team = team or TeamValidationResponseWrapper()
        self._rank = rank or RankValidationResponseWrapper()
        self._coord = coord or CoordValidationResponseWrapper()
        self._square = square or SquareValidationResponseWrapper()
    
    @property
    def team(self) -> TeamValidationResponseWrapper:
        return self._team
    
    @property
    def rank(self) -> RankValidationResponseWrapper:
        return self._rank
    
    @property
    def coord(self) -> CoordValidationResponseWrapper:
        return self._coord
    
    @property
    def square(self) -> SquareValidationResponseWrapper:
        return self._square