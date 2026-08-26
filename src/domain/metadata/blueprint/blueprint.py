# src/domain/metadata/blueprint/blueprint.py

"""
Module: domain.metadata.blueprint.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar

from domain import DomainMetadata, DomainDataObject

T = TypeVar("T", bound="DomainDataObject")


class Blueprint(DomainMetadata, ABC, Generic[T]):
    """
     Role:
         -  Metadata

     Responsibilities:
         1.  Provide attribute-value tuples for hydrating a DomainObject.


     Attributes:
         model_class: Type[T]
         null_exception: NullException
         model_class_name: str

     Provides:

     Super Class:
     """
    _model_class: Type[T]
    _null_exception: DomainObjectNullException
    
    def __init__(
            self,
            model_class: Type[T],
            null_exception: DomainObjectNullException
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
    def null_exception(self) -> DomainObjectNullException:
        return  self._null_exception
    
    @property
    def model_class_name(self) -> str:
        return self._model_class.__class__.__name__

