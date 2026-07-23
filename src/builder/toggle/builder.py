# src/builder/builder/toggle/builder.py

"""
Module: builder.toggle.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast


from blueprint.toggle import ToggleBlueprint
from builder import Builder
from result import BuildResult
from toolkit import BuilderToolkit, ToggleBuilderToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Toggle")


class ToggleBuilder(Builder, Generic[T]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Toggle instance is born safe and reliable.

    Attributes:
            builder_toolkit: [ToggleBuilderToolkit[T]]

    Provides:
        -   def execute(self, blueprint: ToggleBlueprint[T]) -> BuildResult[T]

     Super Class:
         Builder
     """
    def __init__(self, builder_toolkit: ToggleBuilderToolkit[T]):
        """
        Args:
            builder_toolkit: ToggleBuilderToolkit[T]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> BuilderToolkit[T]:
        return cast(ToggleBuilderToolkit[T], super().builder_toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ToggleBlueprint[T]) -> BuildResult[T]:
        pass
        
        
