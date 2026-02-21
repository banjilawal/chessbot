# src/chess/system/collection/operation/computation/state/state.py

"""
Module: chess.system.collection.operation.computation.state.state
Author: Banji Lawal
Created: 2026-01-25
Version: 1.0.0
"""

from chess.system import ComputationResultEnum, ResultState


class ComputationResultState(ResultState[ComputationResultEnum]):
    def __init__(self, classification: ComputationResultEnum):
        super().__init__(classification=classification)