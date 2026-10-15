# src/domain/metadata/blueprint/struct/blueprint.py

"""
Module: domain.metadata.blueprint.struct.blueprint
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Type, TypeVar, cast

from domain import Blueprint, Struct
from err import StructNullException

T = TypeVar("T", bound="Struct")
M = TypeVar("M")


class StructBlueprint(Blueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Struct.

     Attributes:
         domain_class: Type[T]
         domain_null_exception: StructNullException

     ProvideT:

     Super class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: StructNullException,
    ):
        """
        ArgT:
            domain_class: Type[T]
            domain_null_exception: StructNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> StructNullException:
        return cast(StructNullException, super().domain_null_exception)

    