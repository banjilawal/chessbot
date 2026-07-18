# src/blueprint/container/vector/blueprint.py

"""
Module: blueprint.container.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import ContainerBlueprint
from err import VectorNullException
from container import Vector


@dataclass
class VectorSetBlueprint(ContainerBlueprint[Vector]):
    """
    Role:
        -   Container
        -   DTO

    Responsibilities:
        1.  Provides values for instantiating a Vector object.
        2.  DTO

    Attributes:
        x: int
        y: int
            
    Provides:

     Super Class:
        ContainerBlueprint
     """
    """
    Args:
        x: int
        y: int
        null_exception: VectorNullException
        owner: Vector
        owner_name: str
    """
    entr: int
    y: int
    null_exception: VectorNullException = VectorNullException()
    container_class: Vector = Type[Vector]
    owner_name: str = type(owner).__name__