# src/domain/metadata/blueprint/structure/blueprint.py

"""
Module: domain.metadata.blueprint.structure.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Blueprint, StructuralWrapper

T = TypeVar("T", bound="StructuralWrapper")


class StructureBlueprint(Blueprint[T], ABC, Generic[T]):
    """
     Role:
         -   Metadata

     Responsibilities:
         1.  Provide attribute-value tuples for hydrating a StructuralWrapper.

     Attributes:
         model_class: Type[T]
         null_exception: StructureNullException
         model_class_name: str

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(self, model_class: Type[T], null_exception: StructureNullException,):
        """
        Args:
            model_class: Type[[T]
            null_exception: StructureNullException
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
    
    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], super().model_class)
    
    @property
    def null_exception(self) -> StructureNullException:
        return cast(StructureNullException, super().null_exception)
    
    
