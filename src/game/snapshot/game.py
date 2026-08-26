# src/game/snapshot/game.py

"""
Module: game.snapshot.game
Created: 2026-04-03
version: 0.0.2
"""

from typing import Optional

from domain import Game


class Snapshot:
    """
    Role: Persistence, Messanger, Data Transport Object, Error Transport Object,

    Responsibilities:
    1.  Capture a snapshot of the Game by recording Game.arena state after an owner plays their turn.
    2.  Recording the Game winner if the game completed and there was no tie.
    3.  Enforcing mutual exclusion. A Snapshot can either carry payload or exception. Not both.

    Super Class:
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
    _game: Game
    _timestamp: int

    
    def __init__(
            self,
            game: Game,
            timestamp: int,
    ):
        """
        Args:
            game: Game,
            timestamp: int
        """
        self._timestamp = timestamp
        self._game = game
    
    @property
    def timestamp(self) -> int:
        return self.timestamp
    
    @property
    def game(self) -> Game:
        return self._game
    
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
            exception=MethodImplementationException(
                f"{method}: {MethodImplementationException.MSG}. Snapshot must "
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
