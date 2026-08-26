# src/domain/model/collectable/state/model.py

"""
Module: domain.model.collectable.state.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import CollectableModel


class StatefulModel(CollectableModel):
    """
    Role:
        - Stateful Model

    Responsibilities:
        1. Represents a CollectableModel which posses an id and state.

    Attributes:
        id: int
        
    Provides:

    Super Class:
        CollectableModel
    """
    _id: int
    
    def __init__(self, id: int):
        self._id = id
        
    
    @property
    def id(self) -> int:
        return self._id