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
        persona: Persona
        domain_class: Type[Queen]
        domain_null_exception: QueenNullException
        
    Provides:

     Super Class:
        RankBlueprintNullException
     """
    _persona: Persona
    
    def __init__(
            self,
            persona: Persona,
            domain_class: Optional[Type[Queen]] | None = None,
            domain_null_exception: Optional[QueenNullException]| None = None,
    ):
        """
        Args:
            persona: Persona
            domain_class: Optional[Type[Queen]]
            domain_null_exception: Optional[QueenNullException]
        """
        super().__init__(
            domain_class=domain_class or Type[Queen],
            domain_null_exception=domain_null_exception or QueenNullException(),
        )
        self._persona = persona
    
    @property
    def persona(self) -> Persona:
        return self._persona
        
    @property
    def domain_class(self) -> Type[Queen]:
        return cast(Type[Queen], super().domain_class)
    
    @property
    def domain_null_exception(self) -> QueenNullException:
        return cast(QueenNullException, super().domain_null_exception)
