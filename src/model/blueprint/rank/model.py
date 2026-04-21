# src/model/blueprint/rank/model.py

"""
Module: model.blueprint.rank.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Blueprint, Persona, Rank


class RankBlueprint(Blueprint[Rank]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Rank object.

    Attributes:
        id: int
        persona: Persona
            
    Provides:

     Super Class:
        Blueprint
     """
    _persona: Persona
    _id: Optional[int]
    
    
    def __init__(
            self,
            persona: Persona,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            persona: Persona
        """
        self._persona = persona
        self._id = id
        
    @property
    def persona(self) -> Persona:
        return self._persona
    
    @property
    def id(self) -> Optional[int]:
        return self._id