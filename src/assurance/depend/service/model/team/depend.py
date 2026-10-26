# src/assurance/depend/service/model/team/depend.py

"""
Module: assurance.depend.service.model.team.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Team
from exchange import (
    BoardValidationService, PlayerValidationService
)


class TeamDependency(ModelDependency[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy TeamValidator's ResponseService dependencies.

    Attributes:
        board: BoardValidatorResponseService
        owner: PlayerValidatorResponseService

    Provides:

    Super Class:
        ModelDependency
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
            board: Optional[BoardValidatorResponseService]
            owner: Optional[PlayerValidatorResponseService]
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