# src/operand/state/operand/state/maneuver.py

"""
Module: operand.state.operand.maneuver
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass


from operand import Path, Token

@dataclass
class Maneuver:
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Transport resources for a Path factory.

    Attributes:
        token: Token
        path: Path
        id: Optional[int]

    Provides:

    Super Class:
        Operand
    """
    token: Token
    path: Path
    id: int
        
        
        
    