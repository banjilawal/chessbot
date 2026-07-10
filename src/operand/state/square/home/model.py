# src/operand/state/square/home/operand/state.py

"""
Module: operand.state.square.home/operand/state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from operand import Coord, Formation, Square
from operand.board import Board
from operand.state.square import TokenHomeClaimState


class HomeSquare(Square):
    """
    Role:
        -   Operand
        -   Addressing
        -   Stateful Data Holder

    Responsibilities:
        1.  Square Which a token claims before it can make its home move.

    Attributes:
        id: int
        name: str
        board: Board
        coord: Coord
        state: SquareState
        formation: Formation
        occupant: Optional[Token]
        
    Provides:
        -   def is_empty() -> bool
        -   def is_occupied() -> bool

    Super Class:
        Square
    """
    _formation: Formation
    _token_claim_state: TokenHomeClaimState
    
    
    def __init__(
            self,
            id: int,
            name: str,
            coord: Coord,
            board: Board,
            formation: Formation,
    ):
        """
        Args:
            id: int
            name: str
            board: Board
            coord: Coord
            formation: Formation
        """
        super().__init__(id=id, name=name, coord=coord, board=board)
        self._formation = formation
        self._token_claim_state = TokenHomeClaimState.UNCLAIMED
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def token_claim_state(self) -> TokenHomeClaimState:
        return self._token_claim_state
    
    def record_claim(self):
        self._token_claim_state = TokenHomeClaimState.CLAIMED
        
    @property
    def is_claimed(self) -> bool:
        return self.token_claim_state == TokenHomeClaimState.CLAIMED
    
    @property
    def is_not_claimed(self) -> bool:
        return not self.is_claimed
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Square):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
