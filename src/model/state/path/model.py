# src/model/state/path/model/state.py

"""
Module: model.state.path.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from model.state.square import Square

@dataclass
class Path:
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Provide the endpoints of a token's step.

    Attributes:
        id: int
        origin: Square
        destination: Square
        cost: Optional[int]

    Provides:

    Super Class:
    """
    id: int
    origin: Square
    destination: Square
    cost: Optional[int] = None
        
        
        
    