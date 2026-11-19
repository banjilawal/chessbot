# src/repo/repo.py

"""
Module: repo.repo
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import DataStruct
from transit import InsertionDispatcher, SearchDispatcher

T = TypeVar("T", bound="DataStruct")

class Repo(ABC, Generic[T]):
    _data: T
    _searcher: SearchDispatcher
    _inserter: InsertionDispatcher
    
    def __init__(
            self,
            data: T,
            searcher: SearchDispatcher,
            inserter: InsertionDispatcher,
    ):
        """
        Args:
            data: T
            searcher: SearchDispatcher
            inserter: InsertionDispatcher
        """
        self._data = data
        self._searcher = searcher
        self._inserter = inserter
        
    @property
    def data(self) -> T:
        return self._data
    
    @property
    def searcher(self) -> SearchDispatcher:
        return self._searcher
    
    @property
    def inserter(self) -> InsertionDispatcher:
        return self._inserter
    