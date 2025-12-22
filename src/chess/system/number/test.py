# src/chess/system/number/test.py

"""
Module: chess.system.number.test
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from enum import Enum, auto


class TestingLevel(Enum):
    DEFAULT = auto(),
    NOT_NEGATIVE = auto(),
    POSITIVE_ONLY = auto()
    BOUND = auto(),