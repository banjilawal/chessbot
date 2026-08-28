# src/domain/metadata/blueprint/model/blueprint.py

"""
Module: domain.metadata.blueprint.model.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Blueprint, Model
from err import ModelNullException


T = TypeVar("T", bound="Model")

class ModelBlueprint(Blueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Model.

     Attributes:
         domain_class: Type[T]
         domain_null_exception: StructureNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[Model],
            domain_null_exception: ModelNullException,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: ModelNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ModelNullException:
        return cast(ModelNullException, super().domain_null_exception)
    
    
