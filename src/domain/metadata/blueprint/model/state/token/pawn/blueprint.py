# src/domain/metadata/blueprint/model/state/token/pawn/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.token.pawn.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import (
    Bishop, CombatantReadiness, Coord, Formation, HomeSquare, Knight, Pawn, PawnToken, Persona, PromotionState, Queen,
    Rank,
    Rook, Team, Token, TokenBlueprint, TokenDeployment, Footstep
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
        promotion_state: PromotionState

        
        domain_class: Optional[Type[CombatantToken]]
        domain_null_exception: Optional[CombatantNullException]

     Provides:

     Super Class:
        CombatantBlueprint
     """
    
    _rank: Rank
    _promotion_persona: Persona
    _readiness: CombatantReadiness
    _promotion_state: PromotionState
    _captor: Optional[Token]
    
    def __init__(
            self,
            team: Team,
            footstep: Footstep,
            formation: Formation,
            home_square: Optional[HomeSquare] | None = None,
            deployment: Optional[TokenDeployment] | None = None,
            readiness: Optional[CombatantReadiness] | None = None,
            promotion_state: Optional[PromotionState] | None = None,
            promotion_persona: Optional[Persona] | None = None,
            captor: Optional[Token] | None = None,
            rank: Optional[Rank] | None = None,
            id: Optional[int] | None = None,
            domain_class: Optional[Type[PawnToken]] | None = None,
            domain_null_exception: Optional[PawnTokenNullException] | None = None,
    ):
        """
        Args:
            team: Team
            footstep: Footstep
            formation: Formation
            home_square: Optional[HomeSquare]
            deployment: Optional[TokenDeployment]
            readiness: Optional[CombatantReadiness]
            promotion_state: Optional[PromotionState]
            promotion_persona: Optional[Persona]
            captor: Optional[Token]
            rank: Optional[Rank]
            id: Optional[int]
            domain_class: Optional[Type[CombatantToken]]
            domain_null_exception: Optional[CombatantNullException]
        """
        super().__init__(
            id=id,
            team=team,
            footstep=footstep,
            formation=formation,
            home_square=home_square,
            deployment=deployment or TokenDeployment.NOT_DEPLOYED,
            domain_class=domain_class or Type[PawnToken],
            domain_null_exception=domain_null_exception or PawnTokenNullException(),
        )
        self._captor = captor
        self._rank = rank or formation.rank
        self._readiness = readiness or CombatantReadiness.OFF_BOARD
        self._promotion_state = promotion_state or PromotionState.NOT_PROMOTED
        self._promotion_persona = promotion_persona or Persona.PAWN
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def promotion_state(self) -> PromotionState:
        return self._promotion_state
    
    @property
    def readiness(self) -> CombatantReadiness:
        return self._readiness
    
    @property
    def captor(self) -> Optional[Token]:
        return self._captor
    
    @property
    def promotion_persona(self) -> Persona:
        return self._promotion_persona
    
    @property
    def is_captured(self) -> bool:
        return (
                self._captor is not None and
                self._readiness == CombatantReadiness.CAPTURED
        )
    
    @property
    def is_not_captured(self) -> bool:
        return not self.is_captured
    
    @property
    def is_promoted(self) -> bool:
        return (
                isinstance(self._rank, PawnToken.PROMOTION_RANKS) and
                self._promotion_state == PromotionState.PROMOTED
        )
    
    @property
    def is_not_promoted(self) -> bool:
        return (
                isinstance(self._rank, Pawn) and
                self._promotion_state == PromotionState.NOT_PROMOTED
        )
    
    @property
    def promotion_consistency_exists(self) -> bool:
        if (
                self._promotion_persona != self._rank.persona
        ):
            return False
        if (
                isinstance(self._rank, Pawn) and
                self._promotion_state == PromotionState.PROMOTED
        ):
            return False
        if (
                isinstance(self._rank, PawnToken.PROMOTION_RANKS) and
                self._promotion_state == PromotionState.NOT_PROMOTED
        ):
            return False
        if (
                self._promotion_persona == Persona.PAWN and
                self._promotion_state == PromotionState.PROMOTED
        ):
            return False
        if (
                self._promotion_persona in PawnToken.PROMOTION_PERSONAS and
                self._promotion_state == PromotionState.NOT_PROMOTED
        ):
            return False
        return True
    
    @property
    def promotion_is_not_consistent(self) -> bool:
        return (
                self._rank is None or
                self._promotion_state is None or
                self._promotion_persona is None or
                not self.promotion_consistency_exists
        )
    
    @property
    def domain_class(self) -> Type[PawnToken]:
        return cast(Type[PawnToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PawnTokenNullException:
        return cast(PawnTokenNullException, super().domain_null_exception)