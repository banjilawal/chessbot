# src/transit/dispatcher/fabrication/context/dispatcher.py

"""
Module: transit.dispatcher.fabrication.context.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import BuildResult
from fabrication import ContextBuilder, Builder
from domain import Context
from util import LoggingLevelRouter


T = TypeVar("T", bound="Context")


class ContextBuilder(Builder[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Context instance is safe before use.

    Attributes:
        builder: ContextChecker[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[T]

    Super Class:
        Builder
    """
    
    def __init__(self, builder: ContextBuilder[T]):
        """
        Args:
            builder: ContextChecker
        """
        super().__init__(builder=builder)
    
    
    @property
    def builder(self) -> ContextBuilder[T]:
        return cast(ContextBuilder[T], super().builder)
   
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[T]:
        """
        Verify a candidate is a safe Context.
        Args:
            candidate: Any
        Returns:
            BuildResult[T]
        Raises:
            SearchContexBuilderException
        """
        pass
    
    
