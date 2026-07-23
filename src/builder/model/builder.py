# src/builder/model/builder/model/builder.py

"""
Module: builder.model.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from blueprint import ModelBlueprint
from result import BuildResult
from util import LoggingLevelRouter
from builder import Builder
from toolkit import ModelBuilderToolkit

T = TypeVar("T", bound="Model")


class ModelBuilder(Builder, Generic[T]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Model instance is born safe and reliable.

    Attributes:
            builder_toolkit: ModelBuilderToolkit[T]

    Provides:
        -   def execute(self, blueprint: ModelBlueprint[T]) -> BuildResult[T]

     Super Class:
         Builder
     """
    def __init__(self, builder_toolkit: [ModelBuilderToolkit[T]]):
        """
        Args:
            builder_toolkit: [ModelBuilderToolkit[T]]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> ModelBuilderToolkit[T]:
        return cast(ModelBuilderToolkit[T], super().builder_toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ModelBlueprint[T]) -> BuildResult[T]:
        pass
        
        
