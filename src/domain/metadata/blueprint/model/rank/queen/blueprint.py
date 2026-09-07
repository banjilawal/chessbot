# src/domain/metadata/blueprint/model/rank/queen/blueprint.py

"""
Module: domain.metadata.blueprint.model.rank.queen.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Queen, Persona, RankBlueprint
from err import QueenNullException


class QueenBlueprint(RankBlueprint[Queen]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Queen object.

    Attributes:
        persona: Persona.QUEEN
        domain_class: Type[Queen]
        domain_null_exception: QueenNullException
        
    Provides:

     Super Class:
        RankBlueprintNullException
     """
    
    def __init__(
            self,
            persona: Optional[Persona] | None = None,
            domain_class: Optional[Type[Queen]] | None = None,
            domain_null_exception: Optional[QueenNullException]| None = None,
    ):
        """
        Args:
            persona: Persona.QUEEN
            domain_class: Optional[Type[Queen]]
            domain_null_exception: Optional[QueenNullException]
        """
        super().__init__(
            persona=persona or Persona.QUEEN,
            domain_class=domain_class or Type[Queen],
            domain_null_exception=domain_null_exception or QueenNullException(),
        )
        self._persona = persona
    
        
    @property
    def domain_class(self) -> Type[Queen]:
        return cast(Type[Queen], super().domain_class)
    
    @property
    def domain_null_exception(self) -> QueenNullException:
        return cast(QueenNullException, super().domain_null_exception)
