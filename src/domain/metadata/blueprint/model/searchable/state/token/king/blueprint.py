# src/domain/metadata/blueprint/model/searchable/state/token/king/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.token.king.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from collection import CoordDatabase
from domain import KingToken, Formation, HomeSquare, Rank, Team, TokenBlueprint
from err import KingTokenNullException


class KingTokenBlueprint(TokenBlueprint):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a KingToken object.

     Attributes:
        team: Team,
        formation: Formation
        rank: Optional[Rank]
        positions: Optional[CoordDatabase]
        id: Optional[int]

        domain_class: Type[KingToken]
        domain_null_exception: KingTokenNullException

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
            domain_class: Optional[Type[KingToken]] | None = None,
            domain_null_exception: Optional[KingTokenNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            team: Team,
            formation: Formation
            rank: Optional[Rank]
            positions: Optional[CoordDatabase]
            domain_class: Optional[Type[KingToken]]
            domain_null_exception: Optional[KingTokenNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            team=team,
            rank=rank,
            formation=formation,
            positions=positions,
            home_square=home_square,
            domain_class=domain_class or Type[KingToken],
            domain_null_exception=domain_null_exception or KingTokenNullException(),
        )
    
    @property
    def domain_class(self) -> Type[KingToken]:
        return cast(Type[KingToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> KingTokenNullException:
        return cast(KingTokenNullException, super().domain_null_exception)
    


        
        