# src/operand/state/dto/operand/state/dto.py

"""
Module: operand.state.dto.operand.dto
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from operand import Dto, Square, Token


class TokenPathDTO(Dto):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Transport resources for a TokenPath factory.

    Attributes:
        token: Token
        origin: Square
        destination: Square
        id: Optional[int]

    Provides:

    Super Class:
        Dto
    """
    token: Token
    origin: Square
    destination: Square
    id: Optional[int] = None
        
        
        
    