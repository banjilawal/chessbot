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
        persona: Persona.KING
        domain_class: Type[King]
        domain_null_exception: KingNullException
        
    Provides:

     Super Class:
        RankBlueprintNullException
     """
    
    def __init__(
            self,
            persona: Optional[Persona] | None = None,
            domain_class: Optional[Type[King]] | None = None,
            domain_null_exception: Optional[KingNullException]| None = None,
    ):
        """
        Args:
            persona: Persona.KING
            domain_class: Optional[Type[King]]
            domain_null_exception: Optional[KingNullException]
        """
        super().__init__(
            persona=persona or Persona.KING,
            domain_class=domain_class or Type[King],
            domain_null_exception=domain_null_exception or KingNullException(),
        )
        self._persona = persona
    
        
    @property
    def domain_class(self) -> Type[King]:
        return cast(Type[King], super().domain_class)
    
    @property
    def domain_null_exception(self) -> KingNullException:
        return cast(KingNullException, super().domain_null_exception)
