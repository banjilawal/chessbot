# src/domain/metadata/blueprint/model/rank/rook/blueprint.py

"""
Module: domain.metadata.blueprint.model.rank.rook.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Rook, Persona, RankBlueprint
from err import RookNullException


class RookBlueprint(RankBlueprint[Rook]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Rook object.

    Attributes:
        persona: Persona.ROOK
        domain_class: Type[Rook]
        domain_null_exception: RookNullException
        
    Provides:

     Super Class:
        RankBlueprintNullException
     """
    
    def __init__(
            self,
            persona: Optional[Persona] | None = None,
            domain_class: Optional[Type[Rook]] | None = None,
            domain_null_exception: Optional[RookNullException]| None = None,
    ):
        """
        Args:
            persona: Persona.ROOK
            domain_class: Optional[Type[Rook]]
            domain_null_exception: Optional[RookNullException]
        """
        super().__init__(
            persona=persona or Persona.ROOK,
            domain_class=domain_class or Type[Rook],
            domain_null_exception=domain_null_exception or RookNullException(),
        )
        self._persona = persona
    
        
    @property
    def domain_class(self) -> Type[Rook]:
        return cast(Type[Rook], super().domain_class)
    
    @property
    def domain_null_exception(self) -> RookNullException:
        return cast(RookNullException, super().domain_null_exception)
