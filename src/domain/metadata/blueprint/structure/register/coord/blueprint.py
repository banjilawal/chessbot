# src/domain/metadata/blueprint/structure/register/coord.blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from domain import RegisterBlueprint, CoordRegister
from err import CoordRegisterNullException


class CoordRegisterBlueprint(RegisterBlueprint[CoordRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a CoordRegister.

     Attributes:
         domain_class: Type[CoordRegister]
         domain_null_exception: CoordRegisterNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[CoordRegister],
            domain_null_exception: CoordRegisterNullException,
    ):
        """
        Args:
            domain_class: Type[CoordRegister]
            domain_null_exception: CoordRegisterNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[CoordRegister]:
        return cast(Type[CoordRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CoordRegisterNullException:
        return cast(CoordRegisterNullException, super().domain_null_exception)
    
    
