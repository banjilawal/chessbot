# src/domain/metadata/blueprint/struct/toggle/blueprint.py

"""
Module: domain.metadata.blueprint.struct.toggle.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Toggle, StructBlueprint
from err import ToggleNullException


T = TypeVar("T", bound="Toggle")

class ToggleBlueprint(StructBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Toggle.

     Attributes:
         domain_class: Type[T]
         domain_null_exception: ToggleNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: ToggleNullException,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: ToggleNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ToggleNullException:
        return cast(ToggleNullException, super().domain_null_exception)
    
    
