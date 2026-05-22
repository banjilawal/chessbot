# src/model/math/vector/register/category.py

"""
Module: model.math.vector.register.category
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, List

from model import RegisterCategory, VectorOperand


class VectorRegister:
    _u: VectorOperand
    _v: VectorOperand
    _category: RegisterCategory
    
    def __init__(
            self,
            u: VectorOperand,
            v: VectorOperand,
            category: RegisterCategory
    ):
        self._u = u
        self._v = v
        self._category = category
        
    @property
    def a(self) -> VectorOperand:
        return self._u
    
    @property
    def b(self) -> VectorOperand:
        return self._v
    
    @property
    def category(self) -> RegisterCategory:
        return self._category
    
    @property
    def to_list(self) -> List[VectorOperand]:
        return [self.a, self.b]
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {"u": VectorOperand, "v": VectorOperand}
