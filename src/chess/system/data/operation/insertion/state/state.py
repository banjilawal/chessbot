# src/chess/system/insertion/operation/insertion/state/state.py

"""
Module: chess.system.insertion.operation.insertion.state.state
Author: Banji Lawal
Created: 2026-01-25
Version: 1.0.0
"""
from chess.system import InsertionResultEnum, ResultState


class InsertionResultState(ResultState[InsertionResultEnum]):
    def __init__(self, classification: InsertionResultEnum):
        super().__init__(classification=classification)