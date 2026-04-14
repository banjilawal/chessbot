# src/model/math/register/model.py

"""
Module: model.math.register.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List

from model import VectorOperand


@dataclass
class VectorRegister:
    u: VectorOperand
    v: VectorOperand
    
    @property
    def to_list(self) -> List[VectorOperand]:
        return [self.u, self.v]
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {"u": VectorOperand, "v": VectorOperand}
