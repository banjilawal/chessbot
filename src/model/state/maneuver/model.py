# src/model/state/model/state/maneuver.py

"""
Module: model.state.model.maneuver
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass


from model import Path, Token

@dataclass
class Maneuver:
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
    """
    token: Token
    path: Path
    id: int
        
        
        
    