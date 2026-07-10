# src/operand/state/path/operand/state.py

"""
Module: operand.state.path.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from operand import SquareRegister

@dataclass
class Path:
    """
    Role:
        -   Operand
        -   Stateful Data Holder

    Responsibilities:
        1.  Adds a label and cost to a SquareRegister.
        2.  Used in path optimization problems.

    Attributes:
        endpoints: SquareRegister
        cost: Optional[int]
        id: Optional[int]

    Provides:

    Super Class:
        Operand
    """
    endpoints: SquareRegister
    id: Optional[int] = None
    cost: Optional[int] = None

        
        
        
    