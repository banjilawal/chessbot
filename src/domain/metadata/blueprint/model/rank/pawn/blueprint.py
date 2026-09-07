# src/domain/metadata/blueprint/model/rank/pawn/blueprint.py

"""
Module: domain.metadata.blueprint.model.rank.pawn.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Pawn, Persona, RankBlueprint
from err import PawnNullException


class PawnBlueprint(RankBlueprint[Pawn]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Pawn object.

    Attributes:
        persona: Persona.PAWN
        domain_class: Type[Pawn]
        domain_null_exception: PawnNullException
        
    Provides:

     Super Class:
        RankBlueprintNullException
     """
    
    def __init__(
            self,
            persona: Optional[Persona] | None = None,
            domain_class: Optional[Type[Pawn]] | None = None,
            domain_null_exception: Optional[PawnNullException]| None = None,
    ):
        """
        Args:
            persona: Persona.PAWN
            domain_class: Optional[Type[Pawn]]
            domain_null_exception: Optional[PawnNullException]
        """
        super().__init__(
            persona=persona or Persona.PAWN,
            domain_class=domain_class or Type[Pawn],
            domain_null_exception=domain_null_exception or PawnNullException(),
        )
        self._persona = persona
    
        
    @property
    def domain_class(self) -> Type[Pawn]:
        return cast(Type[Pawn], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PawnNullException:
        return cast(PawnNullException, super().domain_null_exception)
