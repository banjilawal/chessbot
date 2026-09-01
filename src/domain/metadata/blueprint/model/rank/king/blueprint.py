# src/domain/metadata/blueprint/model/rank/king/blueprint.py

"""
Module: domain.metadata.blueprint.model.rank.king.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import King, Persona, RankBlueprint
from err import KingNullException


class KingBlueprint(RankBlueprint[King]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a King object.

    Attributes:
        persona: Persona
        domain_class: Type[King]
        domain_null_exception: KingNullException
        
    Provides:

     Super Class:
        RankBlueprintNullException
     """
    _persona: Persona
    
    def __init__(
            self,
            persona: Persona,
            domain_class: Optional[Type[King]] | None = None,
            domain_null_exception: Optional[KingNullException]| None = None,
    ):
        """
        Args:
            persona: Persona
            domain_class: Optional[Type[King]]
            domain_null_exception: Optional[KingNullException]
        """
        super().__init__(
            domain_class=domain_class or Type[King],
            domain_null_exception=domain_null_exception or KingNullException(),
        )
        self._persona = persona
    
    @property
    def persona(self) -> Persona:
        return self._persona
        
    @property
    def domain_class(self) -> Type[King]:
        return cast(Type[King], super().domain_class)
    
    @property
    def domain_null_exception(self) -> KingNullException:
        return cast(KingNullException, super().domain_null_exception)
