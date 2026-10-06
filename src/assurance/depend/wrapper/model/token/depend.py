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
    RankValidationResponseWrapper, TeamValidationResponseWrapper,
    WalkValidationResponseWrapper
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
        walk: WalkValidationResponseWrapper
        
    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _team: TeamValidationResponseWrapper
    _rank: RankValidationResponseWrapper
    _walk: WalkValidationResponseWrapper
    
    def __init__(
            self,
            team: Optional[TeamValidationResponseWrapper] | None = None,
            rank: Optional[RankValidationResponseWrapper] | None = None,
            walk: Optional[WalkValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            team: Optional[TeamValidatorClient]
            rank: Optional[RankValidatorClient]
            walk: Optional[WalkValidationResponseWrapper]
        """
        super().__init__()
        self._team = team or TeamValidationResponseWrapper()
        self._rank = rank or RankValidationResponseWrapper()
        self._walk = walk or WalkValidationResponseWrapper()
    
    @property
    def team(self) -> TeamValidationResponseWrapper:
        return self._team
    
    @property
    def rank(self) -> RankValidationResponseWrapper:
        return self._rank
    
    @property
    def walk(self) -> WalkValidationResponseWrapper:
        return self._walk