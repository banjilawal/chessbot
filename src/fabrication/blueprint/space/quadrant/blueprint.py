# src/blueprint/space/quadrant/blueprint.py

"""
Module: blueprint.space.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from fabrication.blueprint import SpaceBlueprint
from err import QuadrantNullException
from model import Vector


T = TypeVar("T", bound="Quadrant")


class QuadrantBlueprint(SpaceBlueprint, ABC, Generic[T]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating an Quadrant.

     Attributes:
        origin: Vector
        model_class: Type[QuadrantSpace]
        null_exception: Optional[QuadrantNullException]
         
     Provides:

     Super Class:
        SpaceBlueprint
     """
    _origin: Vector
    
    def __init__(
            self,
            origin: Vector,
            null_exception: QuadrantNullException,
            model_class: Type[T] = T,
            terminus: Optional[Vector] | None = None,
    ):
        """
        Args:
            origin: Vector
            model_class: Type[QuadrantSpace]
            null_exception: Optional[QuadrantNullException]
        """
        super().__init__(origin=origin, terminus=terminus, model_class=model_class, null_exception=null_exception)

    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], super().model_class)
    
    @property
    def null_exception(self) -> QuadrantNullException:
        return cast(QuadrantNullException, super().null_exception)

    

