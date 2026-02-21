# src/chess/snapshot.py

"""
Module: chess.snapshot
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional, cast

from chess.agent import PlayerAgent
from chess.arena import Arena
from chess.game import GameState
from chess.system import MethodNotImplementedException, RollbackException, Result


class Snapshot(Result):
    """
    # ROLE:  Persistence, Messanger, Data Transport Object, Error Transport Object,

    # RESPONSIBILITIES:
    1.  Capture a snapshot of the Game by recording Game.arena state after an owner plays their turn.
    2.  Recording the Game winner if the game completed and there was no tie.
    3.  Enforcing mutual exclusion. A Snapshot can either carry payload or exception. Not both.

    # PARENT:
        *   Result

    # PROVIDES:
    Snapshot

    # LOCAL ATTRIBUTES:
        *   arena (Arena)
        *   timestamp (int)
        *   game_state (GameState)
        *   winner (Optional[Player])

    # INHERITED ATTRIBUTES:
        *   See Result class for inherited attributes.
    """
    _arena: Arena
    _timestamp: int
    _game_state: GameState
    _winner: Optional[PlayerAgent]
    
    def __init__(
            self,
            arena: Arena,
            timestamp: int,
            game_state: GameState,
            winner: Optional[PlayerAgent] = None,
            exception: Optional[Exception] = None,
    ):
        super().__init__(payload=arena, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.__init__"
        self._winner = winner
        self._timestamp = timestamp
        self._game_state = game_state
        
    @property
    def arena(self) -> Arena:
        return cast(Arena, self.payload)
    
    @property
    def timestamp(self) -> int:
        return self.timestamp
    
    @property
    def winner(self) -> Optional[PlayerAgent]:
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
    def won(cls, timestamp: int, arena: Arena, winner: PlayerAgent) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, winner=winner, game_state=GameState.WON)
    
    @classmethod
    def aborted(cls, timestamp: int, arena: Arena) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, game_state=GameState.ABORTED)
    
    @classmethod
    def tied(cls, timestamp: int, arena: Arena) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, game_state=GameState.TIED)
    
    @classmethod
    def errored(cls, timestamp: int, arena: Arena, exception: Exception) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, exception=exception, game_state=GameState.FAILURE)
    
    @classmethod
    def rolled_back(cls, timestamp: int, arena: Arena, rollback_exception: RollbackException) -> Snapshot:
        return cls(timestamp=timestamp, arena=arena, exception=rollback_exception, game_state=GameState.ROLLED_BACK)
    
    @classmethod
    def empty(cls) -> Result:
        """Should not be called."""
        method = "Snapshot.empty"
        return Result(
            exception=MethodNotImplementedException(
                f"{method}: {MethodNotImplementedException.DEFAULT_MESSAGE}. Snapshot must "
                f"always have at least a payload and GameState."
            )
        )
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Snapshot):
            return self._timestamp == other.timestamp
        return False
    
    def __hash__(self):
        return hash(self._timestamp)
