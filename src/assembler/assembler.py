# src/assembler/assembler.py

"""
Module: assembler.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from blueprint import Blueprint
from result import BuildResult
from util import LoggingLevelRouter


T = TypeVar("T")

class Assembler(ABC, Generic[T]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create an object from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(blueprint: Blueprint[T]) -> BuildResult[T]

    Super Class:
    """
    
    def __init__(self):
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T],) -> BuildResult[T]:
        pass