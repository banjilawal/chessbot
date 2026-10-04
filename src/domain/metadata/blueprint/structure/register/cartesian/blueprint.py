# src/domain/metadata/blueprint/struct/register/cartesian.blueprint.py

"""
Module: domain.metadata.blueprint.struct.register.cartesian.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from domain import RegisterBlueprint
from err import CartesianToggleRegisterNullException


class CartesianToggleRegisterBlueprint(RegisterBlueprint[CartesianToggleRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a CartesianToggleRegister.

     Attributes:
         domain_class: Type[CartesianToggleRegister]
         domain_null_exception: CartesianToggleRegisterNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[CartesianToggleRegister],
            domain_null_exception: CartesianToggleRegisterNullException,
    ):
        """
        Args:
            domain_class: Type[CartesianToggleRegister]
            domain_null_exception: CartesianToggleRegisterNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[CartesianToggleRegister]:
        return cast(Type[CartesianToggleRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CartesianToggleRegisterNullException:
        return cast(CartesianToggleRegisterNullException, super().domain_null_exception)
    
    
