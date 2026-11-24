# src/controller/chain/controller.py

"""
Module: controller.chain.controller
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import Chain
from controller import Controller
from err import searchRouterException
from microservice import ChainTrimMicroservice, DeletionMicroservice, InsertionMicroservice, SearchMicroservice

T = TypeVar("T", bound="Chain")

class ChainController(Controller[T], ABC, Generic[T]):
    _chain: T
    _searcher: SearchMicroservice
    _inserter: InsertionMicroservice
    _deleter: DeletionMicroservice
    _trimmer: ChainTrimMicroservice

    
    def __init__(
            self,
            chain: T,
            searcher: SearchMicroservice,
            inserter: InsertionMicroservice,
            deleter: DeletionMicroservice,
            trimmer: ChainTrimMicroservice,
    ):
        """
        Args:
            chain: T,
            searcher: SearchMicroservice
            inserter: InsertionMicroservice
            deleter: DeletionMicroservice
            trimmer: ChainTrimMicroservice
        """
        self._chain = chain
        self._searcher = searcher
        self._inserter = inserter
        self._deleter = deleter
        self._trimmer = trimmer
        
    @property
    def chain(self) -> T:
        return self._chain
    
    @property
    def searcher(self) -> SearchMicroservice:
        return self._searcher
    
    @property
    def inserter(self) -> InsertionMicroservice:
        return self._inserter
    
    @property
    def deleter(self) -> DeletionMicroservice:
        return self._deleter
    
    @property
    def trimmer(self) -> ChainTrimMicroservice:
        return self._trimmer
    