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
from microservice import InsertionMicroservice, SearchMicroservice

T = TypeVar("T", bound="DataStruct")

class Repo(ABC, Generic[T]):
    _data: T
    _searcher: SearchMicroservice
    _inserter: InsertionMicroservice
    
    def __init__(
            self,
            data: T,
            searcher: SearchMicroservice,
            inserter: InsertionMicroservice,
    ):
        """
        Args:
            data: T
            searcher: SearchMicroservice,
            inserter: InsertionMicroservice
        """
        self._data = data
        self._searcher = searcher
        self._inserter = inserter
        
    @property
    def data(self) -> T:
        return self._data
    
    @property
    def searcher(self) -> SearchMicroservice:
        return self._searcher
    
    @property
    def inserter(self) -> InsertionMicroservice:
        return self._inserter
    