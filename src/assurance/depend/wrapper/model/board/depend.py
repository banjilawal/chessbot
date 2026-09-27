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
from exchange import ArenaValidationResponseWrapper


class BoardWrapperDependency(ModelWrapperDependency[Board]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy BoardValidator's ResponseWrapper dependencies.

    Attributes:
        arena: ArenaValidationResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    
    _arena: ArenaValidationResponseWrapper
    
    def __init__(
            self,
            arena: Optional[ArenaValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            arena: Optional[ArenaValidatorClient]
        """
        super().__init__()
        self._arena = arena or ArenaValidationResponseWrapper()
    
    @property
    def arena(self) -> ArenaValidationResponseWrapper:
        return self._arena