# src/chess/system/collectionoperation/search/abstract.py

"""
Module: chess.system.collection.operation.search.abstract
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC
from typing import TypeVar, Generic

T = TypeVar("T")


class AbstractSearcher(ABC, Generic[T]):
    pass