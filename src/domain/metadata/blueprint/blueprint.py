# src/domain/metadata/blueprint/blueprint.py

"""
Module: domain.metadata.blueprint.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Type, TypeVar

from domain import DomainMetadata, DomainObject
from err import BlueprintNullException

T = TypeVar("T", bound="DomainObject")

class Blueprint(DomainMetadata, Generic[T]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating an object


     Attributes:
         model_class: Type[T]
         null_exception: NullException

     Provides:

     Super Class:
        Blueprint
     """
    _model_class: Type[T]
    _null_exception: BlueprintNullException
    
    def __init__(
            self,
            model_class: Type[T],
            null_exception: BlueprintNullException
    ):
        """
        Args:
            model_class: Type[T]
            null_exception: NullException
        """
        self._model_class = model_class
        self._null_exception = null_exception
    
    @property
    def model_class(self) -> Type[T]:
        return self._model_class
    
    @property
    def model_class_name(self) -> str:
        return self._model_class.__class__.__name__
    
    @property
    def null_exception(self) -> BlueprintNullException:
        return self._null_exception
