# src/chess/system/data/operation/search/abstract.py

"""
Module: chess.system.data.operation.search.abstract
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC
from typing import TypeVar, Generic

T = TypeVar("T")


class Searcher(ABC, Generic[T]):
    pass