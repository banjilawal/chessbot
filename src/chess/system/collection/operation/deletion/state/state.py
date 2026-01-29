# src/chess/system/data/operation/deletion/state/state.py

"""
Module: chess.system.data.operation.deletion.state.state
Author: Banji Lawal
Created: 2026-01-25
Version: 1.0.0
"""

from chess.system import DeletionResultEnum, ResultState

class DeletionResultState(ResultState[DeletionResultEnum]):
    def __init__(self, classification: DeletionResultEnum):
        super().__init__(classification=classification)