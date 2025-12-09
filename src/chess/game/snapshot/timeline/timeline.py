# src/chess/game/snapshot/timeline/timeline.py

"""
Module: chess.game.snapshot.timeline.timeline
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional, cast

from chess.game import GameSnapshot
from chess.system import DeletionResult, InsertionResult, ResultStack


class GameTimeLine(ResultStack[GameSnapshot]):
    def __init__(self):
        super().__init__()
        
    def commit_player_move(self, update: GameSnapshot) -> InsertionResult[GameSnapshot]:
        method = "GameTimeLine.commit_player_move"
        try:
            if not isinstance(update, GameSnapshot):
                raise TypeError(f"Expected GameResult, got {type(update).__name__} instead.")
            return self.push_result(update)
        except Exception as ex:
            return InsertionResult.failed(
                GameTimeLineException(ex=ex, message=f"{method}: {GameTimeLineException.DEFAULT_MESSAGE}")
            )
    
    def undo_last_turn(self) -> DeletionResult[GameSnapshot]:
        method = "GameTimeLine.undo_last_turn"
        try:
            result = self.undo_result_push()
            if result.is_failure:
                return DeletionResult.failure(result.exception)
            return DeletionResult.success(cast(GameSnapshot, result.payload))
        except Exception as ex:
            return DeletionResult.failure(
                GameTimeLineException(ex=ex, message=f"{method}: {GameTimeLineException.DEFAULT_MESSAGE}")
            )
    
    def last_turn(self) -> Optional[GameSnapshot]:
        return cast(GameSnapshot, self.last_result)