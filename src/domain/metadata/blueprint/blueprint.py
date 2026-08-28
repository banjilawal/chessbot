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

from domain import DomainMetadata
from err import NullException

T = TypeVar("T")


class Blueprint(DomainMetadata, ABC, Generic[T]):
    """
     Role:
         -  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a DomainObject.


     Attributes:
        domain_class: Type[T]
        domain_class_mane: str
        domain_null_exception: NullException

     Provides:

     Super Class:
     """
    _domain_class: Type[T]
    _domain_null_exception: NullException
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: NullException
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: NullException
        """
        self._domain_class = domain_class
        self._domain_null_exception = domain_null_exception
    
    @property
    def domain_class(self) -> Type[T]:
        return self._domain_class
    
    @property
    def domain_null_exception(self) -> NullException:
        return  self._domain_null_exception
    
    @property
    def domain_class_name(self) -> str:
        return self._domain_class.__class__.__name__

