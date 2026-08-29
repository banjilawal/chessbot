# src/domain/metadata/blueprint/model/rank/blueprint.py

"""
Module: domain.metadata.blueprint.model.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import ModelBlueprint, Persona, Rank
from err import RankNullException


class RankBlueprint(ModelBlueprint[Rank]):
    """
     Role:
        1.  Metadata
        
    Responsibilities:
        1.  Provides values for hydrating a Rank object.

        
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
            domain_class: Optional[Type[Rank]] | None = None,
            domain_null_exception: Optional[RankNullException] | None = None,
    ):
        """
        Args:
            persona: Persona
            domain_class: Optional[Type[Rank]]
            domain_null_exception: Optional[RankNullException]
        """
        super().__init__(
            domain_class=domain_class or Type[Rank],
            domain_null_exception=domain_null_exception or RankNullException(),
        )
        self._persona = persona
    
    @property
    def persona(self) -> Persona:
        return self._persona

    
    @property
    def domain_class(self) -> Type[Rank]:
        return cast(Type[Rank], super().domain_class)
    
    @property
    def domain_null_exception(self) -> RankNullException:
        return cast(RankNullException, super().domain_null_exception)
    


    
    

        
        