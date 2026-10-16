# src/fabrication/builder/model/builder.py

"""
Module: fabrication.builder.model.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import BuildResult
from domain import Model
from exchange import ModelBuildRequest
from fabrication import Builder, ModelBuildLoader
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelBuilder(Builder[T], ABC, Generic[T]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create an object from the safe blueprint.

    Attributes:
       loader: ModelBuildLoader[T]

    Provides:
        -   def execute(request: ModelBuildRequest[T]) -> BuildResult[T]

    Super Class:
    """
    _loader: ModelBuildLoader[T]
    
    def __init__(self, loader: ModelBuildLoader[T]):
        """
        Args:
            loader: ModelBuildLoader[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> ModelBuildLoader[T]:
        return cast(ModelBuildLoader, super().loader)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ModelBuildRequest[T]) -> BuildResult[T]:
        """
        Assemble a Model from the Blueprint's contents.

        Args:
            request: ModelBuildRequest[T]
        Returns:
            BuildResult[T]
        Raises:
            ModelBuilderException
        """
        pass