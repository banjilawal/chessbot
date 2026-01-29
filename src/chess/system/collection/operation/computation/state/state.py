# src/chess/system/collectionoperation/computation/state/state.py

"""
Module: chess.system.collection.operation.computation.state.state
Author: Banji Lawal
Created: 2026-01-25
Version: 1.0.0
"""

from chess.system import DataResultEnum, ResultState


class ComputationResultState(ResultState[DataResultEnum]):
    def __init__(self, classification: DataResultEnum):
        super().__init__(classification=classification)