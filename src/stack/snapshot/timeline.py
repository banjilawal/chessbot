# src/logic/snapshot/timeline/timeline.py

"""
Module: logic.snapshot.timeline.timeline
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional, cast

from model.game import Snapshot, GameTimelineException
from system import DeletionResult, InsertionResult, ResultStack


class GameTimeline(ResultStack[Snapshot]):
    """
    Role:Persistence, Unique Result Stack CRUD Controller.

    Responsibilities:
    1.  Ensure all snapshots in managed by GameTimeline are unique.
    2.  Guarantee consistency of records in GameTimeline.

    # PROVIDES:
        *   GameTimeline
        *   No duplicates


    # INHERITED ATTRIBUTES:
    See ResultStack class for inherited attributes.
    """
    
    def __init__(self):
        super().__init__()
        
    def commit_player_move(self, snapshot: Snapshot) -> InsertionResult[Snapshot]:
        method = "GameTimeline.commit_player_move"
        try:
            if not isinstance(snapshot, Snapshot):
                raise TypeError(f"Expected GameResult, got {type(snapshot).__name__} instead.")
            return self.push_result(snapshot)
        except Exception as ex:
            return InsertionResult.failed(
                GameTimelineException(ex=ex, msg=f"{method}: {GameTimelineException.MSG}")
            )
    
    def undo_last_turn(self) -> DeletionResult[Snapshot]:
        method = "GameTimeline.undo_last_turn"
        try:
            result = self.undo_result_push()
            if result.is_failure:
                return DeletionResult.failure(result.exception)
            return DeletionResult.success(cast(Snapshot, result.payload))
        except Exception as ex:
            return DeletionResult.failure(
                GameTimelineException(ex=ex, msg=f"{method}: {GameTimelineException.MSG}")
            )
    
    def previous_move(self) -> Optional[Snapshot]:
        return cast(Snapshot, self.last_result)