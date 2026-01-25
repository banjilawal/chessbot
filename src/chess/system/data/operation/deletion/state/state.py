# src/chess/system/data/operation/deletion/state/state.py

"""
Module: chess.system.data.operation.deletion.state.state
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import DataResultEnum, DeletionResultEnum, ResultState


class DeletionResultState(ResultState[DeletionResultEnum]):
    def __init__(self, state: DeletionResultEnum):
        super().__init__(state=state)