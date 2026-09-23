# src/assurance/attrribute/structure/register/table.py

"""
Module: assurance.attrribute.structure.register.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import RegisterHelperTable, CoordValidator
from domain import CoordRegister


class CoordRegisterHelperTable(RegisterHelperTable[CoordRegister]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Register needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        coord_validator: CoordValidator

    Provides:

    Super Class:
        RegisterHelperTable
    """
    _coord_validator: CoordValidator
    
    def __init__(
            self,
            coord_validator: Optional[CoordValidator] | None = None,
    ):
        """
        Args:
            coord_validator: Optional[CoordValidator]
        """
        super().__init__()
        self._coord_validator = coord_validator or CoordValidator()
        
    @property
    def coord_validator(self) -> CoordValidator:
        return self.coord_validator