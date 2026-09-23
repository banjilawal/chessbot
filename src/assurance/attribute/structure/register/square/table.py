# src/assurance/attrribute/structure/register/table.py

"""
Module: assurance.attrribute.structure.register.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional, cast

from assurance import RegisterHelperTable, SquareValidator
from domain import Square


class SquareRegisterHelperTable(RegisterHelperTable[Square]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        model_validator: SquareValidator

    Provides:

    Super Class:
        RegisterHelperTable
    """
    
    def __init__(
            self,
            model_validator: Optional[SquareValidator] | None = None,
    ):
        """
        Args:
            model_validator: Optional[SquareValidator]
        """
        super().__init__(
            model_validator=model_validator or SquareValidator(),
        )
        
    @property
    def model_validator(self) -> SquareValidator:
        return cast(SquareValidator, super().model_validator)
    
    @property
    def square_validator(self) -> SquareValidator:
        return self.model_validator