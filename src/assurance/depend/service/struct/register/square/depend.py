# src/assurance/depend/service/struct/register/depend.py

"""
Module: assurance.depend.service.struct.register.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterDependency
from domain import SquareRegister
from exchange import SquareValidationService


class SquareRegisterDependency(RegisterDependency[SquareRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        square: SquareValidationService

    Provides:

    Super Class:
        RegisterDependency
    """
    _square: SquareValidationService
    
    def __init__(
            self,
            square: Optional[SquareValidationService] | None = None,
    ):
        """
        Args:
            square: Optional[SquareValidationService]
        """
        super().__init__()
        self._square = square or SquareValidationService()
        
    @property
    def square(self) -> SquareValidationService:
        return self._square