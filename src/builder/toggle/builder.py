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


from assembler import ToggleAssembler
from blueprint.toggle import ToggleBlueprint
from builder import Builder
from result import BuildResult
from err.root import ToggleRootCertifier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Toggle")


class ToggleBuilder(Builder, Generic[T]):
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
        bootstrapper: ToggleRootCertifier[T]
        assembler: ToggleAssembler[T]

    Provides:
        -   def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]

    Super Class:
    """
    def __init__(
            self,
            bootstrapper: ToggleRootCertifier[T],
            assembler: [ToggleAssembler[T]],
    ):
        """
        Args:
            bootstrapper: ToggleRootCertifier[T]
            assembler: ToggleAssembler[T]
        """
        super().__init__(bootstrapper=bootstrapper, assembler=assembler)
    
    @property
    def bootstrapper(self) -> ToggleRootCertifier[T]:
        return cast(ToggleRootCertifier[T], super().bootstrapper)
    
    @property
    def assembler(self) -> ToggleAssembler[T]:
        return cast(ToggleAssembler[T], super().assembler)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ToggleBlueprint[T]) -> BuildResult[T]:
        pass
        
        
