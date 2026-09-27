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
    BoardValidationResponseWrapper, PlayerValidationResponseWrapper
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
    _board: BoardValidationResponseWrapper
    _owner: PlayerValidationResponseWrapper
    
    def __init__(
            self,
            board: Optional[BoardValidationResponseWrapper] | None = None,
            owner: Optional[PlayerValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            board: Optional[BoardValidatorResponseWrapper]
            owner: Optional[PlayerValidatorResponseWrapper]
        """
        super().__init__()
        self._board = board or BoardValidationResponseWrapper()
        self._owner = owner or PlayerValidationResponseWrapper()
    
    @property
    def board(self) -> BoardValidationResponseWrapper:
        return self._board
    
    @property
    def owner(self) -> PlayerValidationResponseWrapper:
        return self._owner