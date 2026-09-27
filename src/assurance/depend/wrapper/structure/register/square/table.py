# src/assurance/depend/wrapper/structure/register/depend.py

"""
Module: assurance.depend.wrapper.structure.register.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterWrapperDependency, SquareValidatorClient
from domain import SquareRegister


class SquareRegisterHelperTable(RegisterWrapperDependency[SquareRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        square: SquareValidatorClient

    Provides:

    Super Class:
        RegisterHelperTable
    """
    _square: SquareValidatorClient
    
    def __init__(
            self,
            square: Optional[SquareValidatorClient] | None = None,
    ):
        """
        Args:
            square: Optional[SquareValidatorClient]
        """
        super().__init__()
        self._square = square or SquareValidatorClient()
        
    @property
    def square(self) -> SquareValidatorClient:
        return self.square