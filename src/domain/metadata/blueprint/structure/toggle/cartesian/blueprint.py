# src/domain/metadata/blueprint/struct/toggle/cartesian.blueprint.py

"""
Module: domain.metadata.blueprint.struct.toggle.cartesian.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type, cast

from domain import CartesianToggle, ToggleBlueprint
from err import CartesianToggleNullException


class CartesianToggleBlueprint(ToggleBlueprint[CartesianToggle]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a CartesianPointToggle.

     Attributes:
         domain_class: Type[CartesianPointToggle]
         domain_null_exception: CartesianPointToggleNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[CartesianToggle],
            domain_null_exception: CartesianToggleNullException,
    ):
        """
        Args:
            domain_class: Type[CartesianPointToggle]
            domain_null_exception: CartesianPointToggleNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[CartesianToggle]:
        return cast(Type[CartesianToggle], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CartesianToggleNullException:
        return cast(CartesianToggleNullException, super().domain_null_exception)
    
    
