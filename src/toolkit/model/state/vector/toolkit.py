# src/toolkit/model/vector/toolkit.py

"""
Module: toolkit.model.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from toolkit import ModelToolkit
from model import VectorOperandRegister
from validation import VectorOperandValidator


class VectorRegisterToolkit(ModelToolkit[VectorOperandRegister]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and validators that are required for VectorRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
        vector_operand_validator: VectorOperandValidator
    
    Provides:
    
    Super Class:
       ModelToolkit
    """
    _vector_operand_validator: VectorOperandValidator
    
    def __init__(
            self,
            vector_operand_validator: VectorOperandValidator | None = None,
    ):
        """
        Args:
            vector_operand_validator: VectorOperandValidator
        """
        super().__init__()
        self._vector_operand_validator = vector_operand_validator or VectorOperandValidator()
        
    @property
    def vector_operand_validator(self) -> VectorOperandValidator:
        return self._vector_operand_validator
