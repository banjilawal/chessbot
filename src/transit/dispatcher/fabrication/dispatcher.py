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


Q = TypeVar("Q", bound="BuildRequest")
W = TypeVar("R", bound="Builder")


class BuildDispatcher(Dispatcher[BuildResult], ABC, Generic[Q, W]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the Build workflow.

    Attributes:
        builder: W

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[T]

    Super Class:
        Dispatcher
    """
    _builder: W
    
    def __init__(self, builder: W):
        """
        Args:
            builder: W
        """
        self._builder = builder

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> BuildResult:
        """
        Verify a candidate is safe to use.
        Args:
            request: Q
        Returns:
            BuildResult[T]
        Raises:
            ModelDispatcherException
        """
        pass
