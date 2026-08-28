# src/domain/metadata/blueprint/model/rank/blueprint.py

"""
Module: domain.metadata.blueprint.model.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type, cast

from domain.metadata.blueprint import ModelBlueprint
from domain.model import Rank
from domain.schema import Persona


class RankBlueprint(ModelBlueprint[Rank]):
    """
    Role:
        - Container
        -  DTO
        
    Responsibilities:
        1.  Provides values for hydrating a Rank object.
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
            domain_class: Type[Rank] = Rank,
    ):
        """
        Args:
            persona: Persona
            domain_class: Type[Rank]
        """
        super().__init__(domain_class=domain_class)
        self._persona = persona
        
    @property
    def domain_class(self) -> Type[Rank]:
        return cast(Type[Rank], super().domain_class)
    
    @property
    def persona(self) -> Persona:
        return self._persona

    
    

        
        