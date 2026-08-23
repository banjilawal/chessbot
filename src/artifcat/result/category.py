# src/artifact/result/category.py

"""
Module: artfifact.result.category
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from enum import Enum, auto

class MethodResultType(Enum):
    ANALYSIS_RESULT = auto(),
    BUILD_RESULT = auto(),
    COMPUTATION_RESULT = auto(),
    DELETION_RESULT = auto(),
    INSERTION_RESULT = auto(),
    INTERPRETATION_RESULT = auto(),
    PARSE_RESULT = auto(),
    SEARCH_RESULT = auto(),
    UPDATE_RESULT = auto(),
    VALIDATION_RESULT = auto(),
    MOVE_RESULT = auto()
    EVENT_RESULT = auto(),
    