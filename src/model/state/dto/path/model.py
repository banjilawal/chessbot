# src/model/state/dto/model/state/dto.py

"""
Module: model.state.dto.model.dto
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Dto, Square, Token


class TokenPathDTO(Dto):
    """
    Role:
        -   Model
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
        
        
        
    