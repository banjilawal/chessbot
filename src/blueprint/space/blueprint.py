# src/blueprint/space/blueprint.py

"""
Module: blueprint.space.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, Type, cast

from blueprint import Blueprint
from err import SpaceNullException
from space import Space


class SpaceBlueprint(Blueprint[Space]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a Space object
         2.  DTO

     Attributes:
         space_class: Type[Space]
         null_exception: Optional[SpaceNullException]
         
     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            model_class: Type[Space],
            null_exception: Optional[SpaceNullException] | None = SpaceNullException(),
    ):
        """
        Args:
            model_class: Type[Space[T]]
            null_exception: Optional[SpaceNullException]
        """
        super().__init__(
            model_class=model_class,
            null_exception=null_exception
        )
    
    @property
    def space_class(self) -> Type[Space]:
        return cast(Type[Space], super().model_class)
    
    @property
    def null_exception(self) -> SpaceNullException:
        return cast(SpaceNullException, super().null_exception)
    
    
