# src/domain/metadata/blueprint/model/vector/blueprint.py

"""
Module: domain.metadata.blueprint.model.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from err import VectorNullException
from fabrication import ModelBlueprint

from domain.model import Vector



class VectorBlueprint(ModelBlueprint[Vector]):
    """
    Role:
        - Container
        -  DTO

    Responsibilities:
        1.  Provides values for hydrating a Vector object.
        2.  DTO

    Attributes:
        x: int
        y: int
        domain_class: Type[Vector]
        domain_null_exception: Optional[VectorModelNullException]
            
    Provides:

     Super Class:
        ModelBlueprint
     """
    _x: int
    _y: int
    
    def __init__(
            self,
            x: int,
            y: int,
            domain_class: Type[Vector] = Vector,
            domain_null_exception: Optional[VectorNullException] | None = None,
    ):
        """
        Args:
            x: int
            y: int
            domain_class: Type[Vector]
            domain_null_exception: Optional[VectorModelNullException]
        """
        super().__init__(domain_class=domain_class, domain_null_exception=domain_null_exception or VectorNullException())
        self._x = x
        self._y = y
        
    @property
    def domain_class(self) -> Type[Vector]:
        return cast(type[Vector], super()._domain_class)
    
    @property
    def domain_null_exception(self) -> VectorNullException:
        return cast(VectorNullException, super().domain_null_exception)
    
    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y