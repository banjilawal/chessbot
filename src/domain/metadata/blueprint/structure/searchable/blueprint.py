# src/domain/metadata/blueprint/structure/searchable/blueprint.py

"""
Module: domain.metadata.blueprint.structure.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Blueprint, Structure

T = TypeVar("T", bound="Structure")


class SearchableStructureBlueprint(StructureBlueprint[T], ABC, Generic[T]):
    """
     Role:
         -  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Structure .

     Attributes:
         domain_class: Type[T]
         domain_null_exception: StructureNullException
         domain_class_name: str

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(self, domain_class: Type[T], domain_null_exception: StructureNullException,):
        """
        Args:
            domain_class: Type[[T]
            domain_null_exception: StructureNullException
        """
        super().__init__(domain_class=domain_class, domain_null_exception=domain_null_exception)
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> StructureNullException:
        return cast(StructureNullException, super().domain_null_exception)
    
    
