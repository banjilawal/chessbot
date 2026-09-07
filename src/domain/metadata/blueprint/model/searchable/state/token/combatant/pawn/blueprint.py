# src/domain/metadata/blueprint/model/searchable/state/token/combatant/pawn/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.token.combatant.pawn.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from collection import CoordDatabase
from domain import Formation, HomeSquare, PawnToken, Rank, Team, CombatantBlueprint, Token
from err import PawnTokenNullException



class PawnTokenBlueprint(CombatantBlueprint):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a PawnToken object.

     Attributes:
        previous_rank: Optional[Rank]

     Provides:

     Super Class:
        CombatantBlueprint
     """
    _previous_rank: Optional[Rank]

    
    def __init__(
            self,
            team: Team,
            formation: Formation,
            rank: Optional[Rank] | None = None,
            previous_rank: Optional[Rank] | None = None,
            captor: Optional[Token] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            positions: Optional[CoordDatabase] | None = None,
            domain_class: Optional[Type[PawnToken]] | None = None,
            domain_null_exception: Optional[PawnTokenNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            team: Team,
            formation: Formation
            rank: Optional[Rank]
            positions: Optional[CoordDatabase]
            domain_class: Optional[Type[PawnToken]]
            domain_null_exception: Optional[PawnTokenNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            team=team,
            rank=rank,
            captor=captor,
            formation=formation,
            positions=positions,
            home_square=home_square,
            domain_class=domain_class or PawnToken,
            domain_null_exception=domain_null_exception or PawnTokenNullException(),
        )
        self._previous_rank = previous_rank
        
    @property
    def previous_rank(self) -> Optional[Rank]:
        return self._previous_rank
    
    @property
    def domain_class(self) -> Type[PawnToken]:
        return cast(Type[PawnToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PawnTokenNullException:
        return cast(PawnTokenNullException, super().domain_null_exception)
    
    @property
    def is_promoted(self) -> bool:
        return self._previous_rank is not None
    
    @property
    def is_not_promoted(self) -> bool:
        return not self.is_promoted
    


        
        