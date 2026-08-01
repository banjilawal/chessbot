# src/build/build.py

"""
Module: build/build
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


from blueprint import Blueprint
from result import BuildResult
from toolkit import BuilderToolkit
from util import LoggingLevelRouter

T = TypeVar("T")


class Builder(ABC, Generic[T]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner
    
    Responsibilities:
        1.  Ensure a new T instance is born safe and reliable.
    
    Attributes:
        builder_toolkit: [BuilderToolkit[T]]
    
    Provides:
        -   def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]
    
    Super Class:
    """
    _builder_toolkit: BuilderToolkit[T]
    
    def __init__(self, builder_toolkit: BuilderToolkit[T]):
        """
        Args:
           builder_toolkit: BuilderToolkit[T]
        """
        self._builder_toolkit = builder_toolkit
    
    @property
    def builder_toolkit(self) -> BuilderToolkit[T]:
        return self._builder_toolkit

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
        pass