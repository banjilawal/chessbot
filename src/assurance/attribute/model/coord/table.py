# src/assurance/attrribute/model/coord/table.py

"""
Module: assurance.attrribute.model.coord.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, BoardValidator, NumberValidator, PrimingValidator
from domain import Coord

class CoordHelperTable(AttributeHelperTable[Coord]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators an Coord needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        board_validator: BoardValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _board_validator: BoardValidator
    
    def __init__(
            self,
            board_validator: Optional[BoardValidator] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            board_validator: Optional[BoardValidator]
            number_validator: Optional[NumberValidator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            number_validator=number_validator,
            priming_validator=priming_validator,
        )
        self._board_validator = board_validator or BoardValidator()
    
    @property
    def board_validator(self) -> BoardValidator:
        return self._board_validator
    
