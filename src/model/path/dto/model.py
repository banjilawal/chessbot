# src/model/path/model/dto.py

"""
Module: model.path.model.dto
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from model import Square, Token

@dataclass
class TokenPathDTO:
    """
    Role:
        -   Model
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
        
        
        
    