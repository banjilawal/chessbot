# src/assurance/attrribute/model/vector/table.py

"""
Module: assurance.attrribute.model.vector.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, NumberValidator, PrimingValidator
from domain import Vector


class VectorHelperTable(AttributeHelperTable[Vector]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators an Vector needs for its primitive and upstream relational partners attributes.

    Attributes:

    Provides:

    Super Class:
        AttributeHelperTable
    """
    
    def __init__(
            self,
            number_validator: Optional[NumberValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            number_validator: Optional[NumberValidator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            number_validator=number_validator,
            priming_validator=priming_validator,
        )