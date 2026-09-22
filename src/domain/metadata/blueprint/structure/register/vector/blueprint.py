# src/domain/metadata/blueprint/structure/register/vector.blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from domain import RegisterBlueprint, VectorRegister
from err import VectorRegisterNullException


class VectorRegisterBlueprint(RegisterBlueprint[VectorRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a VectorRegister.

     Attributes:
         domain_class: Type[VectorRegister]
         domain_null_exception: VectorRegisterNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[VectorRegister],
            domain_null_exception: VectorRegisterNullException,
    ):
        """
        Args:
            domain_class: Type[VectorRegister]
            domain_null_exception: VectorRegisterNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[VectorRegister]:
        return cast(Type[VectorRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> VectorRegisterNullException:
        return cast(VectorRegisterNullException, super().domain_null_exception)
    
    
