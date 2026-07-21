# src/blueprint/space/blueprint.py

"""
Module: blueprint.space.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Optional, Type, TypeVar, cast

from blueprint import Blueprint
from err import SpaceNullException

T = TypeVar("T", bound="Space")

class SpaceBlueprint(Blueprint, Generic[T]):
    """
     Role:
         -   Space
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a Space object
         2.  DTO

     Attributes:
        model_class: Type[T]
        null_exception: Optional[SpaceNullException]
         
     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            model_class: Type[T],
            null_exception: Optional[SpaceNullException] | None = SpaceNullException(),
    ):
        """
        Args:
            model_class: Type[Space[T]]
            null_exception: Optional[SpaceNullException]
        """
        super().__init__(model_class=model_class, null_exception=null_exception,)
        
    
    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], super().model_class)
    
    @property
    def null_exception(self) -> SpaceNullException:
        return cast(SpaceNullException, super().null_exception)