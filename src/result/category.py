# src/result/category.py

"""
Module: result.category
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from enum import Enum, auto

class MethodResultType(Enum):
    ANALYSIS_RESULT = auto(),
    BUILD_RESULT = auto(),
    COMPUTATION_RESULT = auto(),
    DELETION_RESULT = auto(),
    INSERTION_RESULT = auto(),
    SEARCH_RESULT = auto(),
    UPDATE_RESULT = auto(),
    VALIDATION_RESULT = auto(),
    MOVE_RESULT = auto()
    EVENT_RESULT = auto(),
    