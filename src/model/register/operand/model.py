# src/model/state/math/vector/register/category.py

"""
Module: model.state.math.vector.register.category
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, List

from model import OperandRegisterContentType, VectorOperand


class VectorOperandRegister:
    _u: VectorOperand
    _v: VectorOperand
    _content_type: OperandRegisterContentType
    
    def __init__(
            self,
            u: VectorOperand,
            v: VectorOperand,
            content: OperandRegisterContentType
    ):
        self._u = u
        self._v = v
        self._content_type = content
        
    @property
    def a(self) -> VectorOperand:
        return self._u
    
    @property
    def b(self) -> VectorOperand:
        return self._v
    
    @property
    def category(self) -> OperandRegisterContentType:
        return self._content_type
    
    @property
    def to_list(self) -> List[VectorOperand]:
        return [self.a, self.b]
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {"u": VectorOperand, "v": VectorOperand}
