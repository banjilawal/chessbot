# src/assurance/depend/service/model/path/depend.py

"""
Module: assurance.depend.service.model.path.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ServiceDependency
from domain import Path
from exchange import SquareRegisterValidationService


class PathServiceDependency(ServiceDependency[Path]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy PathValidator's ValidationService dependencies.

    Attributes:
        square_register: SquareRegisterValidationService
        
    Provides:

    Super Class:
        Dependency
    """
    
    _square_register: SquareRegisterValidationService
    
    def __init__(
            self,
            square_register: Optional[SquareRegisterValidationService] | None = None,
    ):
        """
        Args:
            square_register: Optional[SquareRegisterValidationService]
        """
        super().__init__()
        self._square_register = square_register or SquareRegisterValidationService()
        
    @property
    def square_register(self) -> SquareRegisterValidationService:
        return self._square_register