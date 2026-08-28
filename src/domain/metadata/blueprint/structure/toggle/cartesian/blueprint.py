# src/domain/metadata/blueprint/structure/toggle/cartesian/blueprint.py

"""
Module: domain.metadata.blueprint.structure.toggle.cartesian.blueprint.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain.metadata.blueprint.structure import ToggleBlueprint
from domain.model import Coord, Cartesian
from domain.structure.toggle import CartesianToggle


class CartesianToggleBlueprint(ToggleBlueprint[CartesianToggle]):
    """
    Role:
        - Container
    
    Responsibilities:
        1.  Provides values for hydrating a CartesianToggle object.
    
    Attributes:
        cartesian: Optional[Cartesian]
        coord: Optional[Coord]
        domain_class: Type[CartesianToggle]
    
    Provides:
    
    Super Class:
        ToggleBlueprint
    """
    _cartesian: Optional[Cartesian]
    _coord: Optional[Coord]
    
    def __init__(
            self,
            coord: Optional[Coord] | None = None,
            cartesian: Optional[Cartesian] | None = None,
            domain_class: Type[CartesianToggle] = CartesianToggle,
    ):
        """
        Args:
            cartesian: Optional[Cartesian]
            coord: Optional[Coord]
            domain_class: Type[CartesianToggle]
        """
        super().__init__(domain_class=domain_class)
        self._coord = coord
        self._cartesian = cartesian
    
    @property
    def domain_class(self) -> Type[CartesianToggle]:
        return cast(Type[CartesianToggle], super().domain_class)
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def cartesian(self) -> Optional[Cartesian]:
        return self._cartesian
    
    @property
    def excess_active_toggles(self) -> bool:
        return self.enabled_toggles_count > self.max_enabled_toggles
    
    @property
    def no_active_toggles(self) -> bool:
        return self.enabled_toggles_count == 0
    
    @property
    def enabled_toggles_count(self) -> int:
        return len([self._coord, self._cartesian])
    
    @property
    def for_cartesian_toggle(self) -> bool:
        return (
            self._cartesian is not None and
            self._coord is None and
            isinstance(self._cartesian, Cartesian)
        )
    
    @property
    def for_coord_toggle(self) -> bool:
        return (
                not self.for_cartesian_toggle and
                isinstance(self._coord, Coord)
        )
    
    
    

