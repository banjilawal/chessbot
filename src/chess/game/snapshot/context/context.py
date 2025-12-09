# src/chess/game/snapshot/context/context.py

"""
Module: chess.game.snapshot.context.context
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import Context
from chess.game import GameSnapshot


class GameSnapshotContext(Context[GameSnapshot]):
    def to_dict(self) -> dict:
        pass
