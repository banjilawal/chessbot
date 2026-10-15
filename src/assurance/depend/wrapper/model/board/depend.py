# src/assurance/depend/wrapper/model/board/depend.py

"""
Module: assurance.depend.wrapper.model.board.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Board
from exchange import TeamBinderValidationResponseWrapper


class BoardWrapperDependency(ModelWrapperDependency[Board]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy BoardValidator's ResponseWrapper dependencies.

    Attributes:
        binder: TeamBinderValidationResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    
    _binder: TeamBinderValidationResponseWrapper
    
    def __init__(
            self,
            binder: Optional[TeamBinderValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            binder: Optional[TeamBinderValidationResponseWrapper]
        """
        super().__init__()
        self._binder = binder or TeamBinderValidationResponseWrapper()
    
    @property
    def binder(self) -> TeamBinderValidationResponseWrapper:
        return self._binder