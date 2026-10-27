# src/assurance/depend/service/model/board/depend.py

"""
Module: assurance.depend.service.model.board.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ServiceDependency
from domain import Board
from exchange import TeamBinderValidationService


class BoardServiceDependency(ServiceDependency[Board]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy BoardValidator's ValidationService dependencies.

    Attributes:
        binder: TeamBinderValidationService

    Provides:

    Super Class:
        Dependency
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