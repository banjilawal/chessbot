# src/domain/metadata/blueprint/structure/register/square.blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from domain import RegisterBlueprint, SquareRegister
from err import SquareRegisterNullException


class SquareRegisterBlueprint(RegisterBlueprint[SquareRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a SquareRegister.

     Attributes:
         domain_class: Type[SquareRegister]
         domain_null_exception: SquareRegisterNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[SquareRegister],
            domain_null_exception: SquareRegisterNullException,
    ):
        """
        Args:
            domain_class: Type[SquareRegister]
            domain_null_exception: SquareRegisterNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[SquareRegister]:
        return cast(Type[SquareRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SquareRegisterNullException:
        return cast(SquareRegisterNullException, super().domain_null_exception)
    
    
