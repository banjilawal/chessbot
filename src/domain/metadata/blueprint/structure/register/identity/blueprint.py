# src/domain/metadata/blueprint/structure/register/identity.blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.identity.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from domain import RegisterBlueprint, IdentityRegister
from err import IdentityRegisterNullException


class IdentityRegisterBlueprint(RegisterBlueprint[IdentityRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a IdentityRegister.

     Attributes:
         domain_class: Type[IdentityRegister]
         domain_null_exception: IdentityRegisterNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[IdentityRegister],
            domain_null_exception: IdentityRegisterNullException,
    ):
        """
        Args:
            domain_class: Type[IdentityRegister]
            domain_null_exception: IdentityRegisterNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[IdentityRegister]:
        return cast(Type[IdentityRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> IdentityRegisterNullException:
        return cast(IdentityRegisterNullException, super().domain_null_exception)
    
    
