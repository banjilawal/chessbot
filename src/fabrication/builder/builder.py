# src/fabrication/builder/fabrication/builder.py

"""
Module: fabrication.builder.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from domain.metadata.blueprint import Blueprint
from artifcat import BuildResult
from util import LoggingLevelRouter


T = TypeVar("T")

class Builder(ABC, Generic[T]):
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