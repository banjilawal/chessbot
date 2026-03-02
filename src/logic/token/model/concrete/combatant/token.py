# src/logic/token/model/concrete/combatant/occupant.py

"""
Module: logic.token.model.concrete.combatant.occupant
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from logic.team import Team
from logic.rank import Rank
from logic.token import Token, TokenBoardState, ReadinessState


class CombatantToken(Token):
    """
    # ROLE: Data-Holder

    # RESPONSIBILITIES:
    1.  Represents piece which can be captured by an enemy.
    2.  CombatantTokens can have Ranks: Paw, Knight, Bishop, Rook, or Queen.

    # PARENT:
        *   Token

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   captor (Optional[Toke])
        *   id (int)
        *   team (Team)
        *   rank (Rank)
        *   designation (str)
        *   roster_number (int)
        *   positions (CoordStack)
        *   opening_square_name (str)
        *   current_position (Optional[Coord])
        *   previous_address (Optional[Coord])
        *   token_board_state (TokenBoardState)
        *   readiness_state (ReadinessState)

    # INHERITED ATTRIBUTES:
        *   See Token class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   id (int)
        *   team (Team)
        *   rank (Rank)
        *   designation (str)
        *   roster_number (int)
        *   opening_square_name (str)

    # LOCAL METHODS:
        *   has_entered_hostage_process(self) -> bool
        *   being_processed_as_hostage(self) -> bool
        *   recorded_as_hostage(self) -> bool

    # INHERITED METHODS:
        *   See Token class for inherited methods.
    """

    _captor: Optional[Token]
    
    def __init__(
            self,
            id: int,
            rank: Rank,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square_name: str,
    ):
        """
        Args:
            id: int
            team: Team
            rank: Rank
            designation: str
            roster_number: int
            opening_square_name: str
        """
        super().__init__(
            id=id,
            team=team,
            rank=rank,
            designation=designation,
            roster_number=roster_number,
            opening_square_name=opening_square_name,
        )
        self._captor = None
    
    @property
    def is_active(self) -> bool:
        return (
                self._captor is None and
                self.readiness_state == ReadinessState.FREE and
                self.board_state == TokenBoardState.DEPLOYED_ON_BOARD
        )
    
    @property
    def is_disabled(self) -> bool:
        return not self.is_active

    @property
    def has_entered_hostage_process(self) -> bool:
        return (
                self._captor is not None and
                self.board_state == TokenBoardState.DEPLOYED_ON_BOARD and
                self.readiness_state == ReadinessState.CAPTURE_ACTIVATED
        )
    
    @property
    def being_processed_as_hostage(self) -> bool:
        return (
                self._captor is not None and
                self.board_state == TokenBoardState.REMOVED_FROM_BOARD and
                self.readiness_state == ReadinessState.HOSTAGE_CREATED
        )
    
    @property
    def recorded_as_hostage(self) -> bool:
        return (
                self._captor is not None and
                self.board_state == TokenBoardState.REMOVED_FROM_BOARD and
                self.readiness_state == ReadinessState.HOSTAGE_IN_DATABASE
        )
    
    @property
    def captor(self) -> Optional[Token]:
        return self._captor
    
    @captor.setter
    def captor(self, captor: Token):
        self._captor = captor
        
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, CombatantToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)