# src/blueprint/model/rank/blueprint.py

"""
Module: blueprint.model.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import ModelBlueprint
from model import Rank
from schema import Persona


class RankBlueprint(ModelBlueprint[Rank]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating a Rank object.
        2.  DTO
        
    Attributes:
        persona: Persona
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    _persona: Persona
    
    def __init__(
            self,
            persona: Persona,
            model_class: Type[Rank] = Rank,
    ):
        """
        Args:
            persona: Persona
            model_class: Type[Rank]
        """
        super().__init__(model_class=model_class)
        self._persona = persona
        
    @property
    def model_class(self) -> Type[Rank]:
        return cast(Type[Rank], super().model_class)
    
    @property
    def persona(self) -> Persona:
        return self._persona

    
    

        
        