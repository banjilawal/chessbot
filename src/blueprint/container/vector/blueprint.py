# src/blueprint/container/vector/blueprint.py

"""
Module: blueprint.container.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Tuple, Type, cast

from blueprint import ContainerBlueprint
from container import VectorSet
from err import VectorSetNullException
from model import Vector


class VectorSetBlueprint(ContainerBlueprint[Vector]):
    """
    Role:
        -   Container
        -   DTO

    Responsibilities:
        1.  Provides values for instantiating a Vector object.
        2.  DTO

    Attributes:
        items: Tuple[Vector, ...],
        container_class: Type[VectorSet],
        null_exception: VectorSetNullException
            
    Provides:

     Super Class:
        ContainerBlueprint
     """
    
    def __init__(
            self,
            entries: Tuple[Vector],
            container_class: Type[VectorSet] = VectorSet,
            null_exception: VectorSetNullException | None = VectorSetNullException(),
    ):
        """
        Args:
            entries: Tuple[Vector, ...],
            container_class: Type[VectorSet],
            null_exception: VectorSetNullException
        """
        super().__init__(
            entries=entries,
            container_class=container_class,
            null_exception=null_exception,
        )
        
    @property
    def entries(self) -> Tuple[Vector]:
        return cast(Tuple[Vector], self.entries)
    
    @property
    def container_class(self) -> VectorSet:
        return cast(VectorSet, self.container_class)
    
    @property
    def null_exception(self) -> VectorSetNullException:
        return cast(VectorSetNullException, super().null_exception)
