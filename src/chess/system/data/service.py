# src/chess/system/data/service.py

"""
Module: chess.system.data.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import DataResult, SearchContext, SearchResult, Service

T = TypeVar("T")


class DataService(ABC, Service[Generic[T]]):
    """"""
    
    @abstractmethod
    def add_data(self, data: T) -> DataResult[T]:
        """"""
        pass
    
    
    def search(self, search_context: SearchContext) -> SearchResult[[T]]:
        """"""
        pass