# src/logic/system/collection/operation/search/result/state/state.py

"""
Module: logic.system.collection.operation.search.result.state.state
Author: Banji Lawal
Created: 2026-01-25
Version: 1.0.0
"""

from logic.system import ResultState, SearchResultEnum

class SearchResultState(ResultState[SearchResultEnum]):
    def __init__(self, classification: SearchResultEnum):
        super().__init__(classification)