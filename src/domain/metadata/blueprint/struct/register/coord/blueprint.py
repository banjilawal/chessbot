# src/domain/metadata/blueprint/struct/register/coord.blueprint.py

"""
Module: domain.metadata.blueprint.struct.register.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, Type, cast

from domain import Coord, RegisterBlueprint, CoordRegister
from err import CoordRegisterNullException


class CoordRegisterBlueprint(RegisterBlueprint[CoordRegister, Coord]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a CoordRegister.

     Attributes:
        origin: Coord
        destination: Coord
        Optional[Type[CoordRegister]]
        domain_null_exception: Optional[CoordRegisterNullException]

     Provides:

     Super Class:
        RegisterBlueprint
     """
    
    def __init__(
            self,
            origin: Coord,
            destination: Coord,
            domain_class: Optional[Type[CoordRegister]] | None = None,
            domain_null_exception: Optional[CoordRegisterNullException] | None = None,
    ):
        """
        Args:
            origin: Coord
            destination: Coord
            Optional[Type[CoordRegister]]
            domain_null_exception: Optional[CoordRegisterNullException]
        """
        super().__init__(
            a=origin,
            b=destination,
            domain_class=domain_class or CoordRegister,
            domain_null_exception=domain_null_exception or CoordRegisterNullException(),
        )
    
    @property
    def origin(self) -> Coord:
        return cast(Coord, super().a)
    
    @property
    def a(self) -> Coord:
        return self.origin
    
    @property
    def destination(self) -> Coord:
        return cast(Coord, super().b)
    
    @property
    def b(self) -> Coord:
        return self.destination
    
    @property
    def origin_is_destination(self) -> bool:
        return self.origin == self.destination
    
    @property
    def origin_is_not_destination(self) -> bool:
        return not self.origin_is_destination
    
    @property
    def to_dict(self) -> Dict[str, Coord]:
        return {
            "origin": self.origin,
            "destination": self.destination,
        }
    
    @property
    def domain_class(self) -> Type[CoordRegister]:
        return cast(Type[CoordRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CoordRegisterNullException:
        return cast(CoordRegisterNullException, super().domain_null_exception)
    
    
