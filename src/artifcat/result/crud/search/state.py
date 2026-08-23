# src/artifact/result/crud/search/state.py
"""
Module: artfifact.result.crud.search.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from enum import Enum, auto

class SearchState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    NOTHING_FOUND = auto(),
    SOMETHING_FOUND = auto(),