# src/blueprint/container/rank/blueprint.py

"""
Module: blueprint.container.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import ContainerBlueprint
from container import Rank
from schema import Persona


class RankBlueprint(ContainerBlueprint[Rank]):
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
        ContainerBlueprint
     """
    _persona: Persona
    
    def __init__(
            self,
            persona: Persona,
            container_class: Type[Rank] = Rank,
    ):
        """
        Args:
            persona: Persona
            container_class: Type[Rank]
        """
        super().__init__(container_class=container_class)
        self._persona = persona
        
    @property
    def container_class(self) -> Type[Rank]:
        return cast(Type[Rank], self.container_class)
    
    @property
    def persona(self) -> Persona:
        return self._persona

    
    

        
        