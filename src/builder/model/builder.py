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

from assembler import ModelAssembler
from blueprint import ModelBlueprint
from builder import Builder
from result import BuildResult
from root import ModelRootCertifier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelBuilder(Builder, Generic[T]):
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
        bootstrapper: ModelRootCertifier[T]

    Provides:
        -   def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]

    Super Class:
        Builder
    """
    def __init__(
            self,
            bootstrapper: ModelRootCertifier[T],
            assembler: [ModelAssembler[T]],
    ):
        """
        Args:
            bootstrapper: ModelRootCertifier[T]
            assembler: ModelAssembler[T]
        """
        super().__init__(bootstrapper=bootstrapper, assembler=assembler)
    
    @property
    def bootstrapper(self) -> ModelRootCertifier[T]:
        return cast(ModelRootCertifier[T], super().bootstrapper)
    
    @property
    def assembler(self) -> ModelAssembler[T]:
        return cast(ModelAssembler[T], super().assembler)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ModelBlueprint[T]) -> BuildResult[T]:
        pass
        
        
