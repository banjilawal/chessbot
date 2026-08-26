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


from artifcat import BuildResult
from domain import BuildRequest
from fabrication import BuilderToolkit
from util import LoggingLevelRouter


T = TypeVar("T")

class Builder(ABC, Generic[T]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create an object from the safe blueprint.

    Attributes:
        toolit: BuildRequest[T]

    Provides:
        -   def execute(blueprint: Blueprint[T]) -> BuildResult[T]

    Super Class:
    """
    _toolkit: BuilderToolkit
    
    def __init__(self):
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: BuildRequest[T],) -> BuildResult[T]:
        pass