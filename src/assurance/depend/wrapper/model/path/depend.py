# src/assurance/depend/wrapper/model/path/depend.py

"""
Module: assurance.depend.wrapper.model.path.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Path
from exchange import SquareRegisterValidationResponseWrapper


class PathWrapperDependency(ModelWrapperDependency[Path]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy PathValidator's ResponseWrapper dependencies.

    Attributes:
        square_register: SquareRegisterValidationResponseWrapper
        
    Provides:

    Super Class:
        ModelWrapperDependency
    """
    
    _square_register: SquareRegisterValidationResponseWrapper
    
    def __init__(
            self,
            square_register: Optional[SquareRegisterValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            square_register: Optional[SquareRegisterValidationResponseWrapper]
        """
        super().__init__()
        self._square_register = square_register or SquareRegisterValidationResponseWrapper()
        
    @property
    def square_register(self) -> SquareRegisterValidationResponseWrapper:
        return self._square_register