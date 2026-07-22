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
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Creation process owners.
        2.  Assure objects comply with business logic at point of creation.
        3.  Ensure stateful data-holding build resources satisfy contracts.
    
    Attributes:
        root_certifier: RootCertifier[T]

    Provides:
        -   def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]
        
    Super Class:
    """
    _builder_toolkit: BuilderToolkit[T]
    
    def __init__(self, builder_toolkit: BuilderToolkit[T]):
        """
        Args:
           builder_toolkit: BuilderToolkit[T
        """
        self._builder_toolkit = builder_toolkit
    
    @property
    def build_toolkit(self) -> BuilderToolkit[T]:
        return self._builder_toolkit

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
        pass