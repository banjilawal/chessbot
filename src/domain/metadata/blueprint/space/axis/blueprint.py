# src/domain/metadata/blueprint/space/axis/blueprint.py

"""
Module: domain.metadata.blueprint.space.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, List, Optional, Type, TypeVar, cast

from domain.metadata.blueprint import SpaceBlueprint
from err import AxisNullException
from domain.model import Vector

T = TypeVar("T", bound="Axis")


class AxisBlueprint(SpaceBlueprint, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating an Axis.

     Attributes:
        origin: Vector
        domain_class: Type[Axis]
        domain_null_exception: Optional[AxisNullException]
         
     Provides:

     Super Class:
        SpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            domain_class: Type[T],
            terminus: Optional[Vector] | None = None,
            domain_null_exception: Optional[AxisNullException] | None = AxisNullException(),
    ):
        """
        Args:
            origin: Vector
            terminus: Optional[Vector]
            domain_class: Type[Axis]
            domain_null_exception: Optional[AxisNullException]
        """
        super().__init__(
            origin=origin,
            terminus=terminus,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )

    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> AxisNullException:
        return cast(AxisNullException, super().domain_null_exception)
    
    @property
    def endpoints_to_list(self) -> List[Vector]:
        return [self._origin, self._terminus]
    
    @property
    def terminus_exists(self) -> bool:
        return self._terminus is not None
    
    @property
    def terminus_does_not_exist(self) -> bool:
        return not self.terminus_exists
    

