# src/domain/metadata/blueprint/model/iden/token/pawn/blueprint.py

"""
Module: domain.metadata.blueprint.model.iden.token.pawn.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import (
    CombatantReadiness, Coord, Formation, HomeSquare, PawnToken, PromotionIdentifiable, Rank,
    Team, Token, TokenBlueprint, TokenDeployment
)
from err import PawnTokenNullException


class PawnTokenBlueprint(TokenBlueprint[PawnToken]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a PawnToken object.

     Attributes:
        rank: Rank
        readiness: CombatantReadiness
        promotion_identifiable: PromotionIdentifiable
        captor: Optional[Token]

     Provides:

     Super Class:
        CombatantBlueprint
     """
    _rank: Rank
    _readiness: CombatantReadiness
    _promotion_identifiable: PromotionIdentifiable
    _captor: Optional[Token]
    
    def __init__(
            self,
            team: Team,
            formation: Formation,
            rank: Optional[Rank] | None = None,
            captor: Optional[Token] | None = None,
            position: Optional[Coord] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            previous_position: Optional[Coord] | None = None,
            deployment: Optional[TokenDeployment] | None = None,
            readiness: Optional[CombatantReadiness] | None = None,
            promotion_identifiable: Optional[PromotionIdentifiable] | None = None,
            domain_class: Optional[Type[PawnToken]] | None = None,
            domain_null_exception: Optional[PawnTokenNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            team: Team,
            formation: Formation
            captor: Optional[Token]
            position: Optional[Coord]
            home_square: Optional[HomeSquare]
            previous_position: Optional[Coord]
            deployment: Optional[TokenDeployment]
            readiness: Optional[CombatantReadiness]
            promotion_identifiable: Optional[PromotionIdentifiable]
            domain_class: Optional[Type[CombatantToken]]
            domain_null_exception: Optional[CombatantNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            team=team,
            position=position,
            formation=formation,
            deployment=deployment,
            home_square=home_square,
            previous_position=previous_position,
            domain_class=domain_class or Type[PawnToken],
            domain_null_exception=domain_null_exception or PawnTokenNullException(),
        )
        self._captor = captor
        self._readiness = readiness
        self._rank = rank or formation.rank
        self._promotion_identifiable = promotion_identifiable or PromotionIdentifiable.NOT_PROMOTED
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def promotion_identifiable(self) -> PromotionIdentifiable:
        return self._promotion_identifiable
    
    @property
    def readiness(self) -> CombatantReadiness:
        return self._readiness
    
    @property
    def captor(self) -> Optional[Token]:
        return self._captor
    
    @property
    def is_captured(self) -> bool:
        return self._captor is not None
    
    @property
    def is_not_captured(self) -> bool:
        return not self.is_captured
    
    @property
    def domain_class(self) -> Type[PawnToken]:
        return cast(Type[PawnToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PawnTokenNullException:
        return cast(PawnTokenNullException, super().domain_null_exception)