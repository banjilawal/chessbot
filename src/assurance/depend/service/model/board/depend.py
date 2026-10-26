# src/assurance/depend/service/model/board/depend.py

"""
Module: assurance.depend.service.model.board.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Board
from exchange import TeamBinderValidationService


class BoardDependency(ModelDependency[Board]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy BoardValidator's ResponseService dependencies.

    Attributes:
        binder: TeamBinderValidationService

    Provides:

    Super Class:
        ModelDependency
    """
    
    _binder: TeamBinderValidationService
    
    def __init__(
            self,
            binder: Optional[TeamBinderValidationService] | None = None,
    ):
        """
        Args:
            binder: Optional[TeamBinderValidationService]
        """
        super().__init__()
        self._binder = binder or TeamBinderValidationService()
    
    @property
    def binder(self) -> TeamBinderValidationService:
        return self._binder