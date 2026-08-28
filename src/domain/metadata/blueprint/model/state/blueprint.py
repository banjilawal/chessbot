# src/domain/metadata/blueprint/model/state/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, TypeVar, cast

from domain.metadata.blueprint import ModelBlueprint
from domain.model import Model, StatefulModel

T = TypeVar("T", bound="StatefulModel")


class StateModelBlueprint(ModelBlueprint[[T]]):
    """
     Role:
         -  Metadata

     Responsibilities:
         1.  Provides values for hydrating a StateModel object.
         2.  DTO

     Attributes:
         id: Optional[int]
         domain_class: Type[StateModel[T]]
         
     Provides:

     Super Class:
        StateModelBlueprint
     """
    _id: Optional[int]
    
    def __init__(
            self,
            domain_class: Type[StatefulModel[T]],
            id: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Type[Model[T]]
        
        """
        super().__init__(domain_class=domain_class, )
        self._id = id
    
    @property
    def domain_class(self) -> Type[Model[T]]:
        return cast(Type[Model[T]], super().domain_class)
    
    @property
    def id(self) -> Optional[int]:
        return self._id
