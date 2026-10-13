# src/domain/metadata/blueprint/struct/blueprint.py

"""
Module: domain.metadata.blueprint.struct.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Type, TypeVar, cast

from domain import Blueprint, Model, Struct
from err import StructNullException


S = TypeVar("S", bound="Struct")
M = TypeVar("M", bound="Model")

class StructBlueprint(Blueprint[S], ABC, Generic[S, M]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Struct.

     Attributes:
         domain_class: Type[S]
         domain_null_exception: StructNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[Struct],
            domain_null_exception: StructNullException,
    ):
        """
        Args:
            domain_class: Type[S]
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
    def is_balanced(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_not_balanced(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, M]:
        pass
    
    @property
    def domain_class(self) -> Type[S]:
        return cast(Type[S], super().domain_class)
    
    @property
    def domain_null_exception(self) -> StructNullException:
        return cast(StructNullException, super().domain_null_exception)
    
    
