# src/result/search/state.py
"""
Module: result.search.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from enum import Enum, auto

class SearchState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    NOTHING_FOUND = auto(),