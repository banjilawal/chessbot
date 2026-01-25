# src/chess/system/data/operation/computation/state/state.py

"""
Module: chess.system.data.operation.computation.state.state
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""
from chess.system import DataResultEnum, ResultState


class ComputationResultState(ResultState[DataResultEnum]):
    def __init__(self, state: DataResultEnum):
        self.state = state