# src/assurance/attrribute/structure/register/table.py

"""
Module: assurance.attrribute.structure.register.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterHelperTable, VectorValidator
from domain import VectorRegister


class VectorRegisterHelperTable(RegisterHelperTable[VectorRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        vector_validator: VectorValidator

    Provides:

    Super Class:
        RegisterHelperTable
    """
    _vector_validator: VectorValidator
    
    def __init__(
            self,
            vector_validator: Optional[VectorValidator] | None = None,
    ):
        """
        Args:
            vector_validator: Optional[VectorValidator]
        """
        super().__init__()
        self._vector_validator = vector_validator or VectorValidator()
        
    @property
    def vector_validator(self) -> VectorValidator:
        return self.vector_validator