# src/domain/model/searchable/state/walk/model.py

"""
Module: domain.model.searchable.state.walk.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC


from domain import StatefulModel


class Walk(StatefulModel, ABC):
    """
    Role:
        - Stateful Model

    Responsibilities:
        1. Represents properties and states owned by a walk.

    Attributes:
        
    Provides:

    Super Class:
        StatefulModel
    """
    _traveler: Token
    _path: SquareRegister
    _id: Optional[int]
    
    def __init__(self, id: int):
        self._id = id
        
    
    @property
    def id(self) -> int:
        return self._id