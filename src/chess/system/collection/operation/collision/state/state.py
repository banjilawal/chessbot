# src/chess/system/collection/operation/collision/state/state.py

"""
Module: chess.system.collection.operation.collision.state.state
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from chess.system import CollisionResultEnum, ResultState


class CollisionResultState(ResultState[CollisionResultEnum]):
    def __init__(self, classification: CollisionResultEnum):
        super().__init__(classification=classification)