# src/transit/dispatcher/fabrication/dispatcher.py

"""
Module: transit.dispatcher.fabrication.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from fabrication import Builder
from artifcat import BuildResult
from transit import Dispatcher
from util import LoggingLevelRouter


T = TypeVar("T")


class BuildDispatcher(Dispatcher[BuildResult], ABC, Generic[T]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the Build workflow.

    Attributes:
        builder: Builder[T]

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[T]

    Super Class:
        Dispatcher
    """
    _builder: Builder[T]
    
    def __init__(self, builder: Builder[T]):
        """
        Args:
            builder: Builder[T]
        """
        self._builder = builder
        
    @property
    def builder(self) -> Builder[T]:
        return self._builder

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[T]:
        """
        Verify a candidate is safe to use.
        Args:
            job: Any
        Returns:
            BuildResult[T]
        Raises:
            ModelDispatcherException
        """
        pass
