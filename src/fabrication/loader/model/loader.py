# src/fabrication/loader/model/loader.py

"""
Module: fabrication.loader.model.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import BuildResult
from domain import Model, ModelBlueprint
from exchange import BuildRequest, ModelBuildRequest, ModelValidationService
from fabrication import BuildLoader
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelBuildLoader(BuildLoader[T], ABC, Generic[T]):
    """
    Role
        -   Authorization
        -   Bootstrapper
        
    Responsibilities:
        1.  Bootstraps the Build process by assuring the request is valid and its
            inspecting the job's requirements.

    Attributes:
        validator: ModelValidationService[T]
        
    Provides:
        -   def execute(request: BuildRequest[T]) -> BuildResult[ModelBlueprint[T]]

    Super Class:
        BuildLoader
    """

    
    def __init__(self, validator: ModelValidationService[T]):
        """
        Args:
            validator: ModelValidationService[T]
        """
        super().__init__(validator=validator)
    
    @property
    def validator(self) -> ModelValidationService[T]:
        return cast(ModelValidationService[T], super().validator)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ModelBuildRequest[T]) -> BuildResult[ModelBlueprint[T]]:
        """
        Prepare a ModelBlueprint which is used to build a safe product.

        Args:
            request: ModelBuildRequest[T]
        Returns:
            BuildResult[ModelBlueprint[T]]
        Raises:
            ModelBuildLoaderException
        """
        pass