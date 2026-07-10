# src/operand/state/path/operand/state/dto.py

"""
Module: operand.state.path.operand.dto
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from operand import Square, Token

@dataclass
class TokenPathDTO:
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Transport resources for a Path factory.

    Attributes:
        token: Token
        origin: Square
        destination: Square
        id: Optional[int]

    Provides:

    Super Class:
        Path
    """
    token: Token
    origin: Square
    destination: Square
    id: Optional[int] = None
        
        
        
    