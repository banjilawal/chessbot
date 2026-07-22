# src/space/builder/register/__init__.py

"""
Module: space.builder.register.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from blueprint import RegisterBlueprint
from builder import Builder
from result import BuildResult
from toolkit import RegisterBuildToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")


class RegisterBuilder(Builder, Generic[T]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Register instance is born safe and reliable.

    Attributes:
            builder_toolkit: [RegisterBuilderToolkit[T]]

    Provides:
        -   def execute(self, blueprint: RegisterBlueprint[T]) -> BuildResult[Register]

     Super Class:
         Builder
     """
    
    def __init__(self, builder_toolkit: [RegisterBuildToolkit[T]]):
        """
        Args:
            builder_toolkit: [RegisterBuilderToolkit[T]]
        """
        super().__init__(builder_toolkit=builder_toolkit)
        
    @property
    def build_toolkit(self) -> RegisterBuildToolkit[T]:
        return cast([RegisterBuildToolkit[T]], super().build_toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: RegisterBlueprint[T]) -> BuildResult[T]:
        pass