# src/domain/metadata/blueprint/model/searchable/state/player/human/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.player.human.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import HumanPlayer, PlayerBlueprint
from err import HumanNullException
from game import GameAdviser


class HumanBlueprint(PlayerBlueprint):
    """
    Role:
        1.  Metadata
    
    Responsibilities:
        1.  Provides values for hydrating a HumanPlayer object.
    
    Attributes:
        name: str
        adviser: Optional[GameAdviser]
        id: Optional[int]
        
        domain_class: Type[HumanPlayer]
        domain_null_exception: HumanNullException
    
    Provides:
    
    Super Class:
        PlayerBlueprint
    """
    
    def __init__(self,
            name: str,
            adviser: Optional[GameAdviser] | None = None,
            domain_class: Optional[Type[HumanPlayer]] | None = None,
            domain_null_exception: Optional[HumanNullException] | None = None,
            id: Optional[int] | None = None,
        ):
        """
        Args:
            name: str
            adviser: Optional[GameAdviser]
            domain_class: Optional[Type[HumanPlayer]]
            domain_null_exception: Optional[HumanNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            name=name,
            adviser=adviser,
            domain_class=domain_class or HumanPlayer,
            domain_null_exception=domain_null_exception or HumanNullException(),
        )
        

    @property
    def domain_class(self) -> Type[HumanPlayer]:
        return cast(Type[HumanPlayer], super().domain_class)
    
    @property
    def domain_null_exception(self) -> HumanNullException:
        return cast(HumanNullException, super().domain_null_exception)