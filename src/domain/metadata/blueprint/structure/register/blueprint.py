# src/domain/metadata/blueprint/structure/register/blueprint

"""
Module: domain.metadata.blueprint.structure.register.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Register, SearchableModelBlueprint, StructureBlueprint
from err import RegisterNullException

T = TypeVar("T", bound="SearchableModelBlueprint")


class RegisterBlueprint(StructureBlueprint[Register], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Register object.

     Attributes:
        domain_class: Type[Register]
        domain_null_exception: RegisterNullException
        payload_blueprint: T

     Provides:

     Super Class:
        StructureBlueprint
     """
    _payload_blueprint: T
    
    def __init__(
            self,
            domain_class: Type[Register],
            domain_null_exception: RegisterNullException,
            payload_blueprint: T,
    
    ):
        """
        Args:
            domain_class: Type[Register]
            domain_null_exception: RegisterNullException
            payload_blueprint: T
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
        self._paylod_blueprint = payload_blueprint
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super()._domain_class)
    
    @property
    def domain_null_exception(self) -> RegisterNullException:
        return cast(RegisterNullException, super().domain_null_exception)
    
    @property
    def payload_blueprint(self) -> T:
        return self._paylod_blueprint
    
