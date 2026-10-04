# src/domain/metadata/blueprint/struct/blueprint.py

"""
Module: domain.metadata.blueprint.struct.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Blueprint, Struct
from err import StructNullException


T = TypeVar("T", bound="Struct")

class StructBlueprint(Blueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Struct.

     Attributes:
         domain_class: Type[T]
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
            domain_class: Type[T]
            domain_null_exception: StructNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> StructNullException:
        return cast(StructNullException, super().domain_null_exception)
    
    
