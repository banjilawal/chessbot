# src/blueprint/container/state/blueprint.py

"""
Module: blueprint.container.state.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, Type, TypeVar, cast

from blueprint import ContainerBlueprint
from container import Container, StateContainer

T = TypeVar("T", bound="StateContainer")


class StateContainerBlueprint(ContainerBlueprint[[T]]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a StateContainer object.
         2.  DTO

     Attributes:
         id: Optional[int]
         container_class: Type[StateContainer[T]]
         
     Provides:

     Super Class:
        StateContainerBlueprint
     """
    _id: Optional[int]
    
    def __init__(
            self,
            container_class: Type[StateContainer[T]],
            id: Optional[int] | None = None,
    ):
        """
        Args:
            container_class: Type[Container[T]]
        
        """
        super().__init__(container_class=container_class,)
        self._id = id
    
    @property
    def container_class(self) -> Type[Container[T]]:
        return cast(Type[Container[T]], self.container_class)
    
    @property
    def id(self) -> Optional[int]:
        return self._id
