# src/fabrication/builder/toggle/fabrication/builder.py

"""
Module: fabrication.builder.toggle.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from fabrication.builder import Builder
from domain.metadata.blueprint import ToggleBlueprint
from artifcat import BuildResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="Toggle")

class ToggleBuilder(Builder, Generic[T]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a Toggle instance from the safe blueprint.

    Attributes:

    Provides:
        -  def execute(self, blueprint: ToggleBlueprint,) -> BuildResult[Toggle]

    Super Class:
         Builder
    """
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ToggleBlueprint[T],) -> BuildResult[T]:
        pass