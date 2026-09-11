# src/domain/metadata/blueprint/model/searchable/state/token/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from collection import CoordDatabase
from domain import (
    CombatantToken, Coord, TokenDeployment, Formation, HomeSquare, KingToken, PawnToken,
    Rank, StateModelBlueprint, Team, Token
)
from err import (
    CombatantNullException, KingTokenNullException, PawnTokenNullException, TokenNullException
)



class TokenBlueprint(StateModelBlueprint[Token]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Token object.

     Attributes:
        team: Team,
        formation: Formation
        rank: Optional[Rank]
        positions: Optional[CoordDatabase]
        id: Optional[int]

        domain_class: Type[Token]
        domain_null_exception: TokenNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _team: Team
    _formation: Formation
    _positions: CoordDatabase
    _deployment: TokenDeployment
    _position: Optional[Coord]
    _previous_position: Optional[Coord]
    _home_square: Optional[HomeSquare]




    
    def __init__(
            self,
            team: Team,
            formation: Formation,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            positions: Optional[CoordDatabase] | None = None,
            deployment: Optional[TokenDeployment] | None = None,
            domain_class: Optional[Type[Token]] | None = None,
            domain_null_exception: Optional[TokenNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            team: Team,
            formation: Formation
            positions: Optional[CoordDatabase]
            domain_class: Optional[Type[Token]]
            domain_null_exception: Optional[TokenNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or CombatantToken,
            domain_null_exception=domain_null_exception or TokenNullException(),
        )
        self._team = team
        self._formation = formation
        self._home_square = home_square
        self._position = position
        self._previous_position = previous_position
        self._deployment = deployment or TokenDeployment.NOT_DEPLOYED
        self._positions = positions or CoordDatabase()
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def positions(self) -> CoordDatabase:
        return self._positions
    
    @property
    def deployment(self) -> TokenDeployment:
        return self._deployment
    
    @property
    def home_square(self) -> Optional[HomeSquare]:
        return self._home_square
    
    @property
    def captor(self) -> Optional[Token]:
        return self._captor
    
    @property
    def position(self) -> Optional[Coord]:
        return self._position
    
    @property
    def previous_position(self) -> Optional[Coord]:
        return self._previous_position
    
    @property
    def domain_class(self) -> Type[Token]:
        # Case that rank is King.
        if isinstance(self._formation.rank, KingToken):
            return cast(
                Type[KingToken],
                super().domain_class
            )
        # Case that rank is Pawn
        if isinstance(self._formation.rank, PawnToken):
            return cast(
                Type[PawnToken],
                super().domain_class
            )
        # All other ranks
        return cast(Type[CombatantToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TokenNullException:
        if self.is_king_token_blueprint:
            return cast(KingTokenNullException, super().domain_null_exception)
        if self.is_pawn_token_blueprint:
            return cast(PawnTokenNullException, super().domain_null_exception)
        return cast(CombatantNullException, super().domain_null_exception)
    
    @property
    def is_pawn_token_blueprint(self) -> bool:
        return isinstance(self._domain_class, PawnToken)
    
    @property
    def is_king_token_blueprint(self) -> bool:
        return isinstance(self._domain_class, KingToken)
    
    @property
    def has_king_captor_inconsistency(self) -> bool:
        return self.is_king_token_blueprint and self._captor is not None
    
    @property
    def has_promotion_inconsistency(self) -> bool:
        return not self.is_pawn_token_blueprint and self._captor is not None
    


        
        