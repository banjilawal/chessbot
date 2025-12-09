# src/chess/game/result/result.py

"""
Module: chess.game.result.result
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional, reveal_type

from chess.agent import Agent
from chess.arena import Arena
from chess.game import GameState, GameSnapshot
from chess.system import NotImplementedException, RollbackException, Result


class GameSnapshot(Result):
    """
    # ROLE:  Persistence, Messanger, Data Transport Object, Error Transport Object,

    # RESPONSIBILITIES:
    1.  Capture a snapshot of the Game by recording Game.arena state after an agent plays their turn.
    2.  Recording the Game winner if the game completed and there was no tie.
    3.  Enforcing mutual exclusion. A GameSnapshot can either carry payload or exception. Not both.

    # PARENT
        *   Result

    # PROVIDES:
    GameSnapshot

    # LOCAL ATTRIBUTES:
        *   arena (Arena)
        *   timestamp (int)
        *   game_state (GameState)
        *   winner (Optional[Agent])

    # INHERITED ATTRIBUTES:
        *   See Result class for inherited attributes.
    """
    _arena: Arena
    _timestamp: int
    _game_state: GameState
    _winner: Optional[Agent]
    
    def __init__(
            self,
            arena: Arena,
            timestamp: int,
            game_state: GameState,
            winner: Optional[Agent] = None,
            exception: Optional[Exception] = None,
    ):
        super().__init__(payload=arena, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.__init__"
        self._winner = winner
        self._timestamp = timestamp
        self._game_state = game_state
    
    @property
    def timestamp(self) -> int:
        return self.timestamp
    
    @property
    def winner(self) -> Optional[Agent]:
        return self._winner
    
    @property
    def game_state(self) -> Optional[GameState]:
        return self._game_state
    
    @property
    def game_is_ready(self) -> bool:
        return self.exception is None and self._winner is None and self._game_state == GameState.CREATED
    
    @property
    def game_is_running(self) -> bool:
        return self.exception is None and self._winner is None and self._game_state == GameState.RUNNING
    
    @property
    def game_is_aborted(self) -> bool:
        return self.exception is None and self._winner is None and self._game_state == GameState.ABORTED
    
    @property
    def game_is_won(self) -> bool:
        """Return True if the game is won."""
        return self.exception is None and self._winner is not None and self._game_state == GameState.WON
    
    @property
    def game_is_tied(self) -> bool:
        """Return True if the game is tied."""
        return self.exception is None and self.winner is None and self._game_state == GameState.TIED
    
    @property
    def game_failed(self) -> bool:
        """Return True if the game raised an exception."""
        return (
                self.exception is not None and
                (self._game_state == GameState.FAILURE or self._game_state == GameState.ROLLED_BACK)
        )
    
    @classmethod
    def won(cls, timestamp: int, arena: Arena, winner: Agent) -> GameSnapshot:
        return cls(timestamp=timestamp, arena=arena, winner=winner, game_state=GameState.WON)
    
    @classmethod
    def aborted(cls, timestamp: int, arena: Arena) -> GameSnapshot:
        return cls(timestamp=timestamp, arena=arena, game_state=GameState.ABORTED)
    
    @classmethod
    def tied(cls, timestamp: int, arena: Arena) -> GameSnapshot:
        return cls(timestamp=timestamp, arena=arena, game_state=GameState.TIED)
    
    @classmethod
    def errored(cls, timestamp: int, arena: Arena, exception: Exception) -> GameSnapshot:
        return cls(timestamp=timestamp, arena=arena, exception=exception, game_state=GameState.FAILURE)
    
    @classmethod
    def rolled_back(cls, timestamp: int, arena: Arena, rollback_exception: RollbackException) -> GameSnapshot:
        return cls(timestamp=timestamp, arena=arena, exception=rollback_exception, game_state=GameState.ROLLED_BACK)
    
    @classmethod
    def empty(cls) -> Result:
        """Should not be called."""
        method = "GameSnapshot.empty"
        return Result(
            exception=NotImplementedException(
                f"{method}: {NotImplementedException.DEFAULT_MESSAGE}. GameSnapshot must "
                f"always have at least a payload and GameState."
            )
        )
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, GameSnapshot):
            return self._timestamp == other.timestamp
        return False
    
    def __hash__(self):
        return hash(self._timestamp)
