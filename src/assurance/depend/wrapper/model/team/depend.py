# src/assurance/depend/wrapper/model/team/depend.py

"""
Module: assurance.depend.wrapper.model.team.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Team
from exchange import (
    BoardValidationService, PlayerValidationService
)


class TeamWrapperDependency(ModelWrapperDependency[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy TeamValidator's ResponseWrapper dependencies.

    Attributes:
        board: BoardValidatorResponseWrapper
        owner: PlayerValidatorResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _board: BoardValidationService
    _owner: PlayerValidationService
    
    def __init__(
            self,
            board: Optional[BoardValidationService] | None = None,
            owner: Optional[PlayerValidationService] | None = None,
    ):
        """
        Args:
            board: Optional[BoardValidatorResponseWrapper]
            owner: Optional[PlayerValidatorResponseWrapper]
        """
        super().__init__()
        self._board = board or BoardValidationService()
        self._owner = owner or PlayerValidationService()
    
    @property
    def board(self) -> BoardValidationService:
        return self._board
    
    @property
    def owner(self) -> PlayerValidationService:
        return self._owner