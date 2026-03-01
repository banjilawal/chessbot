# src/chess/token/model/concrete/king/king.py

"""
Module: chess.token.model.concrete.king.king
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from chess.rank import King
from chess.team import Team
from chess.token import Token, TokenBoardState, ReadinessState


class KingToken(Token):
    """
    # ROLE: Data-Holder, Abstract Data Type

    # RESPONSIBILITIES:
    1.  Represents a Token with a King's Rank and properties.
    2.  Cannot be captured on placed in check or checkmated.

    # PARENT:
        *   Token

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

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
        *   is_in_check(self) -> bool
        *   is_checkmated(self) -> bool
        *   is_active(self) -> bool
        *   is_disabled(self) -> bool

    # INHERITED METHODS:
        *   See Token class for inherited methods.
    """
    def __init__(
            self,
            id: int,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square_name: str,
    ):
        super().__init__(
            id=id,
            team=team,
            rank=King(),
            designation=designation,
            roster_number=roster_number,
            opening_square_name=opening_square_name,
        )
     
    @property
    def is_in_check(self) -> bool:
        return (
                self.board_state == TokenBoardState.DEPLOYED_ON_BOARD and
                self.readiness_state == ReadinessState.IN_CHECK
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.board_state == TokenBoardState.DEPLOYED_ON_BOARD and
                self.readiness_state == ReadinessState.CHECKMATED
        )
    
    @property
    def is_active(self) -> bool:
        return (
                (ReadinessState.FREE or ReadinessState.IN_CHECK) and
                self.board_state == TokenBoardState.DEPLOYED_ON_BOARD
        )
    
    @property
    def is_disabled(self) -> bool:
        return (
                self.is_checkmated or
                self.board_state == TokenBoardState.NEVER_BEEN_PLACED
        )
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
