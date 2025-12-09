# src/chess/game/result/result.py

"""
Module: chess.game.result.result
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from typing import Optional

from chess.agent import Agent
from chess.arena.arena import Arena
from chess.system import NotImplementedException, RollbackException
from chess.system.result import Result
from chess.game import GameState, GameResult



class GameResult(Result):
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
        self.timestamp = timestamp
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
    def is_ready(self) -> bool:
        return self.exception is None and self._winner is None and self._game_state == GameState.CREATED
    
    @property
    def is_running(self) -> bool:
        return self.exception is None and self._winner is None and self._game_state == GameState.RUNNING
    
    @property
    def is_aborted(self) -> bool:
        return self.exception is None and self._winner is None and self._game_state == GameState.ABORTED
    
    @property
    def is_won(self) -> bool:
        return self.exception is None and self._winner is not None and self._game_state == GameState.WON
    
    @property
    def is_tied(self) -> bool:
        return self.exception is None and self.winner is None and self._game_state == GameState.TIED
    
    @property
    def is_failure(self) -> bool:
        return (
                self.exception is not None and
                (self._game_state == GameState.FAILURE or self._game_state == GameState.ROLLED_BACK)
        )
    
    @classmethod
    def won(cls, timestamp: int, arena: Arena, winner: Agent) -> GameResult:
        return cls(timestamp=timestamp, arena=arena, winner=winner, game_state=GameState.WON)
    
    @classmethod
    def aborted(cls, timestamp: int, arena: Arena) -> GameResult:
        return cls(timestamp=timestamp, arena=arena, game_state=GameState.ABORTED)
    
    @classmethod
    def tied(cls, timestamp: int, arena: Arena) -> GameResult:
        return cls(timestamp=timestamp, arena=arena, game_state=GameState.TIED)
    
    @classmethod
    def errored(cls, timestamp: int, arena: Arena, exception: Exception) -> GameResult:
        return cls(timestamp=timestamp, arena=arena, exception=exception, game_state=GameState.FAILURE)
    
    @classmethod
    def rolled_back(cls, timestamp: int, arena: Arena, rollback_exception: RollbackException) -> GameResult:
        return cls(timestamp=timestamp, arena=arena, exception=rollback_exception, game_state=GameState.ROLLED_BACK)
    
    @classmethod
    def empty(cls) -> Result:
        method = "GameResult.empty"
        return Result(
            exception=NotImplementedException(
                f"{method}: {NotImplementedException.DEFAULT_MESSAGE}. GameResult must "
                f"always have at least a payload and GameState."
            )
        )
