# src/domain/metadata/blueprint/model/rank/bishop/blueprint.py

"""
Module: domain.metadata.blueprint.model.rank.bishop.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Bishop, Persona, RankBlueprint
from err import BishopNullException


class BishopBlueprint(RankBlueprint[Bishop]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Bishop object.

    Attributes:
        persona: Persona
        domain_class: Type[Bishop]
        domain_null_exception: BishopNullException
        
    Provides:

     Super Class:
        RankBlueprintNullException
     """
    _persona: Persona
    
    def __init__(
            self,
            persona: Persona,
            domain_class: Optional[Type[Bishop]] | None = None,
            domain_null_exception: Optional[BishopNullException]| None = None,
    ):
        """
        Args:
            persona: Persona
            domain_class: Optional[Type[Bishop]]
            domain_null_exception: Optional[BishopNullException]
        """
        super().__init__(
            domain_class=domain_class or Type[Bishop],
            domain_null_exception=domain_null_exception or BishopNullException(),
        )
        self._persona = persona
    
    @property
    def persona(self) -> Persona:
        return self._persona
        
    @property
    def domain_class(self) -> Type[Bishop]:
        return cast(Type[Bishop], super().domain_class)
    
    @property
    def domain_null_exception(self) -> BishopNullException:
        return cast(BishopNullException, super().domain_null_exception)
