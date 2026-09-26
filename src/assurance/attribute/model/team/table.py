# src/assurance/attrribute/model/team/table.py

"""
Module: assurance.attrribute.model.team.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelValidationWrapperDict
from responseWrapper import BoardValidationResponseWrapper, PlayerValidationResponseWrapper
from domain import Team


class TeamValidationWrapperDict(ModelValidationWrapperDict[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorResponseWrappers a TeamValidator needs.
        
    Attributes:
        board: BoardValidatorResponseWrapper
        owner: PlayerValidatorResponseWrapper

    Provides:

    Super Class:
        ModelHelperTable
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