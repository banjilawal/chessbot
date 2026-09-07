# src/domain/metadata/blueprint/model/searchable/state/token/combatant/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.token.combatant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from collection import CoordDatabase
from domain import CombatantToken, Formation, HomeSquare, Rank, Team, TokenBlueprint
from err import CombatantNullException


class CombatantBlueprint(TokenBlueprint):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a CombatantToken object.

     Attributes:
        team: Team,
        formation: Formation
        rank: Optional[Rank]
        positions: Optional[CoordDatabase]
        id: Optional[int]

        domain_class: Type[CombatantToken]
        domain_null_exception: CombatantNullException

     Provides:

     Super Class:
        TokenBlueprint
     """

    
    def __init__(
            self,
            team: Team,
            formation: Formation,
            rank: Optional[Rank] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            positions: Optional[CoordDatabase] | None = None,
            domain_class: Optional[Type[CombatantToken]] | None = None,
            domain_null_exception: Optional[CombatantNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            team: Team,
            formation: Formation
            rank: Optional[Rank]
            positions: Optional[CoordDatabase]
            domain_class: Optional[Type[CombatantToken]]
            domain_null_exception: Optional[CombatantNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            team=team,
            rank=rank,
            formation=formation,
            positions=positions,
            home_square=home_square,
            domain_class=domain_class or Type[CombatantToken],
            domain_null_exception=domain_null_exception or CombatantNullException(),
        )
    
    @property
    def domain_class(self) -> Type[CombatantToken]:
        return cast(Type[CombatantToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CombatantNullException:
        return cast(CombatantNullException, super().domain_null_exception)
    


        
        