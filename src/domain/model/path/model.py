# src/dossier/model/state/path/dossier/model/state.py

"""
Module: domain.model.state.path.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from domain.model import Model
from domain.structures.register import SquareRegister


@dataclass
class Path(Model):
    """
    Role:
        -   Model
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
        Model
    """
    endpoints: SquareRegister
    id: Optional[int] = None
    cost: Optional[int] = None

        
        
        
    