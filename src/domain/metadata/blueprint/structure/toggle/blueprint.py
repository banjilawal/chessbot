# src/domain/metadata/blueprint/structure/toggle/blueprint.py

"""
Module: domain.metadata.blueprint.structure.toggle.blueprint.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import SearchableModel, StructureBlueprint, Toggle
from err import ToggleNullException

T = TypeVar("T", bound="SearchableModel")


class ToggleBlueprint(StructureBlueprint[Toggle], ABC, Generic[T]):
    """
    Role:
        - Container
    
    Responsibilities:
        1.  Provides values for hydrating a Toggle.
    
    Attributes:
        domain_class: Type[Toggle]
        domain_null_exception: Optional[ToggleNullException]
        payload_blueprint:Type[T]
    
    Provides:
    
    Super Class:
        StructureBlueprint[Toggle]
    """
    _payload_blueprint: T
    
    
    def __init__(
            self,
            domain_class: Type[Toggle],
            domain_null_exception: ToggleNullException,
            payload_blueprint: T,
    ):
        """
        Args:
            domain_class: Type[Toggle]
            domain_null_exception: Optional[ToggleNullException]
            payload_blueprint:Type[T]
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception,
        )
        self._payload_blueprint = payload_blueprint
    
    @property
    def domain_class(self) -> Type[Toggle]:
        return cast(Type[Toggle], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ToggleNullException:
        return cast(ToggleNullException, super().domain_null_exception)
    
    @property
    def payload_blueprint(self) -> T:
        return self._payload_blueprint
    
    
