# src/chess/system/data/operation/search/result/state/classification.py

"""
Module: chess.system.data.operation.search.result.state.classification
Author: Banji Lawal
Created: 2026-01-25
Version: 1.0.0
"""

from enum import Enum, auto


class SearchResultEnum(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    NOTHING_FOUND = auto(),