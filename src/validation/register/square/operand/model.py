# src/model/register/operand/model.py

"""
Module: model.register.operand.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Register, RegisterContentType, VectorOperand


class VectorOperandRegister(Register[VectorOperand]):
    """
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains VectorOperands passed to vector algebra.

    Attributes:
        a: VectorOperand
        b: VectorOperand
        content_type: OperandRegisterContentType
        
        a_is_same_as_b: bool
        a_is_not_same_as_b: bool
        is_vector_register:bool
        is_coord_register: bool
        to_list: List[T]
        to_dict: Dict[str, T]

    Super Class:
        Register
    """
    _content_type: Optional[RegisterContentType]
    
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
        super().__init__(a=a, b=b)
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
    def to_dict(self) -> Dict[str, Any]:
        return {"a": self._a, "v": self._b}
    
    @property
    def a_is_same_as_b(self) -> bool:
        return self._a == self._b
    
    @property
    def a_is_not_ame_as_b(self) -> bool:
        return not self.a_is_same_as_b
    
    @property
    def is_vector_register(self) -> bool:
        return self._a.is_vector and self._b.is_vector
    
    @property
    def is_coord_register(self) -> bool:
        return self._a.is_coord and self._b.is_coord
    
    @property
    def is_inconsistent(self) -> bool:
        return not self._a.is_coord and not self._b.is_coord
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorOperandRegister):
            return (
                    self._a == other.b and
                    self._b == other.b
            )
    
    
    
