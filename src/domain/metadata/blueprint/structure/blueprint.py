# src/domain/metadata/blueprint/structure/blueprint.py

"""
Module: domain.metadata.blueprint.structure.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from ast import TypeVar
from typing import Generic, Optional, Type, cast

from domain.metadata.blueprint import Blueprint
from err import ModelNullException

T = TypeVar("T", bound="StructuralWrapper")

class StructureBlueprint(Blueprint[T], ABC, Generic[T]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a Model object
         2.  DTO

     Attributes:
         model_class: Type[T]
         null_exception: StructureNullException
         
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
        return cast(ModelNullException, super().null_exception)
    
    
