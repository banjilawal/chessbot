# src/model/register/operand/model.py

"""
Module: model.register.operand.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional

from model import RegisterContentType, VectorOperand


class VectorOperandRegister:
    """
    Role:
        -   State

    Responsibilities:
        1.  Describes What type of operands are in the Vecregister.

    Attributes:
            u: VectorOperand,
            v: VectorOperand,
            content_type: OperandRegisterContentType
    Provides:

    Super Class:
        Enum
    """
    _a: VectorOperand
    _b: VectorOperand
    _content_type: RegisterContentType
    
    def __init__(
            self,
            a: VectorOperand,
            b: VectorOperand,
            content_type: Optional[RegisterContentType] | None = None,
    ):
        """
        Args:
            a: VectorOperand
            b: VectorOperand
            content_type: OperandRegisterContentType
        """
        self._a = a
        self._b = b
        self._content_type = content_type
        
    @property
    def a(self) -> VectorOperand:
        return self._a
    
    @property
    def b(self) -> VectorOperand:
        return self._b
    
    @property
    def category(self) -> Optional[RegisterContentType]:
        return self._content_type
    
    @property
    def to_list(self) -> List[VectorOperand]:
        return [self.a, self.b]
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {"u": VectorOperand, "v": VectorOperand}
    
    @property
    def is_vector_register(self) -> bool:
        return self._a.is_vector and self._b.is_vector
    
    @property
    def is_coord_register(self) -> bool:
        return self._a.is_coord and self._b.is_coord
    
    @property
    def is_inconsistent(self) -> bool:
        return not self._a.is_coord and not self._b.is_coord
    
