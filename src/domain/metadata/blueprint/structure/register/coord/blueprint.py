# src/domain/metadata/blueprint/structure/register/coord.blueprint.py

"""
Module: domain.metadata.blueprint.structure.register.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Coord, RegisterBlueprint, CoordRegister
from err import CoordRegisterNullException


class CoordRegisterBlueprint(RegisterBlueprint[CoordRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a CoordRegister.

     Attributes:
        origin: Coord
        terminus: Coord
        Optional[Type[CoordRegister]]
        domain_null_exception: Optional[CoordRegisterNullException]

     Provides:

     Super Class:
        RegisterBlueprint
     """
    _origin: Coord
    _terminus: Coord
    
    def __init__(
            self,
            origin: Coord,
            terminus: Coord,
            domain_class: Optional[Type[CoordRegister]] | None = None,
            domain_null_exception: Optional[CoordRegisterNullException] | None = None,
    ):
        """
        Args:
            origin: Coord
            terminus: Coord
            Optional[Type[CoordRegister]]
            domain_null_exception: Optional[CoordRegisterNullException]
        """
        super().__init__(
            domain_class=domain_class or CoordRegister,
            domain_null_exception=domain_null_exception or CoordRegisterNullException(),
        )
        self._origin = origin
        self._terminus = terminus
        
    @property
    def origin(self) -> Coord:
        return self._origin
    
    @property
    def terminus(self) -> Coord:
        return self._terminus
    
    @property
    def domain_class(self) -> Type[CoordRegister]:
        return cast(Type[CoordRegister], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CoordRegisterNullException:
        return cast(CoordRegisterNullException, super().domain_null_exception)
    
    
