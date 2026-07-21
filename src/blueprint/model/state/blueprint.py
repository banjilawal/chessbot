# src/blueprint/model/state/blueprint.py

"""
Module: blueprint.model.state.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, Type, TypeVar, cast

from blueprint import ModelBlueprint
from model import Model, StateModel

T = TypeVar("T", bound="StateModel")


class StateModelBlueprint(ModelBlueprint[[T]]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a StateModel object.
         2.  DTO

     Attributes:
         id: Optional[int]
         model_class: Type[StateModel[T]]
         
     Provides:

     Super Class:
        StateModelBlueprint
     """
    _id: Optional[int]
    
    def __init__(
            self,
            model_class: Type[StateModel[T]],
            id: Optional[int] | None = None,
    ):
        """
        Args:
            model_class: Type[Model[T]]
        
        """
        super().__init__(model_class=model_class,)
        self._id = id
    
    @property
    def model_class(self) -> Type[Model[T]]:
        return cast(Type[Model[T]], super().model_class)
    
    @property
    def id(self) -> Optional[int]:
        return self._id
