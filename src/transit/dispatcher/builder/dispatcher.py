# src/transit/dispatcher/builder/dispatcher.py

"""
Module: transit.dispatcher.builder.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import BuildResult
from domain import BuildRequest
from fabrication import Builder
from transit import Dispatcher
from util import LoggingLevelRouter

T = TypeVar("T")


class BuildDispatcher(Dispatcher, ABC, Generic[T]):
    """
    Role
        -  Build Pipeline
        -  Integrity Management
        -  Consistency Assurance
        -  Workflow Owner
    
    Responsibilities:
        1.  Ensure a new T instance is born safe and reliable.
    
    Attributes:
        builder_toolkit: BuilderToolkit[T]
    
    Provides:
        -  def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]
    
    Super Class:
    """
    _assembler: Builder[T]
    
    def __init__(self, assembler: Builder[T]):
        """
        Args:
           assembler: BuilderToolkit[T]
        """
        self._assembler = assembler
    
    @property
    def assembler(self) -> Builder[T]:
        return self._assembler

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: BuildRequest[T]) -> BuildResult[T]:
        pass