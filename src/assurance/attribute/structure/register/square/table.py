# src/assurance/attrribute/structure/register/table.py

"""
Module: assurance.attrribute.structure.register.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterValidationWrapperDict, SquareValidatorClient
from domain import SquareRegister


class SquareRegisterHelperTable(RegisterValidationWrapperDict[SquareRegister]):
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
            square_client: Optional[SquareValidatorClient] | None = None,
    ):
        """
        Args:
            square_client: Optional[SquareValidatorClient]
        """
        super().__init__()
        self._square_client = square_client or SquareValidatorClient()
        
    @property
    def square_client(self) -> SquareValidatorClient:
        return self.square_client