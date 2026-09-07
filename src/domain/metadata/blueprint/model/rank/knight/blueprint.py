# src/domain/metadata/blueprint/model/rank/knight/blueprint.py

"""
Module: domain.metadata.blueprint.model.rank.knight.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Knight, Persona, RankBlueprint
from err import KnightNullException


class KnightBlueprint(RankBlueprint[Knight]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Knight object.

    Attributes:
        persona: Persona.KNIGHT
        domain_class: Type[Knight]
        domain_null_exception: KnightNullException
        
    Provides:

     Super Class:
        RankBlueprintNullException
     """
    
    def __init__(
            self,
            persona: Optional[Persona] | None = None,
            domain_class: Optional[Type[Knight]] | None = None,
            domain_null_exception: Optional[KnightNullException]| None = None,
    ):
        """
        Args:
            persona: Persona.KNIGHT
            domain_class: Optional[Type[Knight]]
            domain_null_exception: Optional[KnightNullException]
        """
        super().__init__(
            persona=persona or Persona.KNIGHT,
            domain_class=domain_class or Type[Knight],
            domain_null_exception=domain_null_exception or KnightNullException(),
        )
        self._persona = persona
    
        
    @property
    def domain_class(self) -> Type[Knight]:
        return cast(Type[Knight], super().domain_class)
    
    @property
    def domain_null_exception(self) -> KnightNullException:
        return cast(KnightNullException, super().domain_null_exception)
