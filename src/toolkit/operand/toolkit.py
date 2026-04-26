# src/toolkit/operand/toolkit.py

"""
Module: toolkit.operand.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from operation import CoordValidator, ScalarValidator, VectorValidator
from toolkit import Toolkit
from model import VectorOperand


class VectorOperandToolkit(Toolkit[VectorOperand]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and validators that are required for VectorOperand tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
        coord_validator: CoordValidator
        vector_validator: VectorValidator
        scalar_validator: ScalarValidator
    
    Provides:
    
    Super Class:
        Toolkit
    """
    _coord_validator: CoordValidator
    _vector_validator: VectorValidator
    _scalar_validator: ScalarValidator
    
    def __init__(
            self,
            coord_validator: CoordValidator | None = None,
            vector_validator: VectorValidator | None = None,
            scalar_validator: ScalarValidator | None = None,
    ):
        """
        Args:
            coord_validator: CoordValidator
            vector_validator: VectorValidator
            scalar_validator: ScalarValidator
        """
        super().__init__()
        self._coord_validator = coord_validator or CoordValidator()
        self._vector_validator = vector_validator or VectorValidator()
        self._scalar_validator = scalar_validator or ScalarValidator()
        
    @property
    def coord_validator(self) -> CoordValidator:
        return self._coord_validator
    
    @property
    def vector_validator(self) -> VectorValidator:
        return self._vector_validator
    
    @property
    def scalar_validator(self) -> ScalarValidator:
        return self._scalar_validator
    
