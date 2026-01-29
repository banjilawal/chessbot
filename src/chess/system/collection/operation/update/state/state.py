# src/chess/system/collectionoperation/update/state/state.py

"""
Module: chess.system.collection.operation.update.state.state
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import UpdateResultEnum, ResultState


class UpdateResultState(ResultState[UpdateResultEnum]):
    def __init__(self, classification: UpdateResultEnum):
        super().__init__(classification=classification)