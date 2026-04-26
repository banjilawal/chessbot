# src/toolkit/register/toolkit.py

"""
Module: toolkit.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from operation import VectorOperandValidator
from toolkit import Toolkit
from model import VectorRegister


class VectorRegisterToolkit(Toolkit[VectorRegister]):
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
        Toolkit
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
