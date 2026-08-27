# src/transit/dispatcher/builder/model/dispatcher/builder/model/dispatcher/builder.py

"""
Module: transit.dispatcher.builder.model.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from domain import Model
from fabrication import Builder

T = TypeVar("T", bound="Model")


class ModelBuildDispatcher(Builder[T], ABC, Generic[T]):
    """
    Role
        -  Build Pipeline
        -  Integrity Management
        -  Consistency Assurance
        -  Workflow Owner

   Responsibilities:
        1.  Ensure a new Model instance is born safe and reliable.

    Attributes:
            builder_toolkit: ModelBuilderToolkit[T]

    Provides:
        - def execute(self, blueprint: ModelBlueprint[T]) -> BuildResult[T]

     Super Class:
         Builder
     """
    def __init__(self, assembler: [ModelBuilderToolkit[T]]):
        """
        Args:
            assembler: [ModelBuilderToolkit[T]]
        """
        super().__init__(assembler=assembler)
    
    @property
    def assembler(self) -> ModelBuilderToolkit[T]:
        return cast(ModelBuilderToolkit[T], super().assembler)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ModelBlueprint[T]) -> BuildResult[T]:
        pass
        
        
