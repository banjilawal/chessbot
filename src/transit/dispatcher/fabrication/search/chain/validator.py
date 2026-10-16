# src/transit/dispatcher/fabrication/search/chain/dispatcher.py

"""
Module: transit.dispatcher.fabrication.search.chain.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import BuildResult
from fabrication import ContextBuilder, ChainContextBuilder
from domain import ChainContext
from util import LoggingLevelRouter


T = TypeVar("T", bound="ChainContext")


class ChainContextBuilder(ContextBuilder[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a ChainContext instance is safe before use.

    Attributes:
        builder: ChainContextChecker[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[T]

    Super Class:
        ContextBuilder
    """
    
    def __init__(self, builder: ChainContextBuilder[T]):
        """
        Args:
            builder: ChainContextChecker
        """
        super().__init__(builder=builder)
    
    
    @property
    def builder(self) -> ChainContextBuilder[T]:
        return cast(ChainContextBuilder[T], super().builder)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[T]:
        """
        Verify a candidate is a safe ChainContext.
        Args:
            candidate: Any
        Returns:
            BuildResult[T]
        Raises:
            ChainSearchContexBuilderException
        """
        pass
    
    
