# src/domain/metadata/blueprint/structure/register/square.blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import RegisterBlueprint, Square, SquareRegister
from err import SquareRegisterNullException


class SquareRegisterBlueprint(RegisterBlueprint[SquareRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a SquareRegister.

     Attributes:
        origin: Square
        destination: Square
        Optional[Type[SquareRegister]]
        domain_null_exception: Optional[SquareRegisterNullException]

     Provides:

     Super Class:
        RegisterBlueprint
     """
    _origin: Square
    _destination: Square
    
    def __init__(
            self,
            origin: Square,
            destination: Square,
            domain_class: Optional[Type[SquareRegister]] | None = None,
            domain_null_exception: Optional[SquareRegisterNullException] | None = None,
    ):
        """
        Args:
            origin: Square
            destination: Square
            Optional[Type[SquareRegister]]
            domain_null_exception: Optional[SquareRegisterNullException]
        """
        super().__init__(
            domain_class=domain_class or SquareRegister,
            domain_null_exception=domain_null_exception or SquareRegisterNullException(),
        )
        self._origin = origin
        self._destination = destination
        
    @property
    def origin(self) -> Square:
        return self._origin
    
    @property
    def destination(self) -> Square:
        return self._destination
    
    @property
    def domain_class(self) -> Type[SquareRegister]:
        return cast(Type[SquareRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SquareRegisterNullException:
        return cast(SquareRegisterNullException, super().domain_null_exception)
    
    
