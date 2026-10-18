# src/fabrication/builder/builder.py

"""
Module: fabrication.builder.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import BuildResult
from exchange import BuildRequest
from fabrication import BuildLoader
from transit import BuildRouter
from util import LoggingLevelRouter

T = TypeVar("T")


class BuildFactory(ABC, Generic[T]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create an object from the safe blueprint.

    Attributes:
       loader: BuildLoader[T]
       router: BuildRouter[T]

    Provides:
        -   def execute(request: BuildRequest[T]) -> BuildResult[T]

    Super Class:
    """
    _loader: BuildLoader[T]
    _router: BuildRouter[T]
    
    def __init__(
            self,
            loader: BuildLoader[T],
            router: BuildRouter[T],
    ):
        """
        Args:
            loader: BuildLoader[T]
            router: BuildRouter[T]
        """
        self._loader = loader
        self._router = router
    
    @property
    def loader(self) -> BuildLoader[T]:
        return self._loader
    
    @property
    def router(self) -> BuildRouter[T]:
        return self._router
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: BuildRequest[T]) -> BuildResult[T]:
        """
        Assemble an Object from the Blueprint's contents.

        Args:
            request: BuildRequest[T]
        Returns:
            BuildResult[T]
        Raises:
            BuilderException
        """
        pass