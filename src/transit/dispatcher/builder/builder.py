# src/build/build.py

"""
Module: build/build
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import BuildResult
from domain import Blueprint, DomainObject
from fabrication import Assembler
from util import LoggingLevelRouter

T = TypeVar("T", bound="DomainObject")


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
        builder_toolkit: BuilderToolkit[T]
    
    Provides:
        -   def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]
    
    Super Class:
    """
    _assembler: Assembler[T]
    
    def __init__(self, assembler: Assembler[T]):
        """
        Args:
           assembler: BuilderToolkit[T]
        """
        self._assembler = assembler
    
    @property
    def assembler(self) -> Assembler[T]:
        return self._assembler

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
        pass