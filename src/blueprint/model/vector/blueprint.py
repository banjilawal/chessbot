# src/blueprint/model/vector/blueprint.py

"""
Module: blueprint.model.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import Blueprint
from err import VectorNullException
from model import Vector


@dataclass
class VectorBlueprint(Blueprint[Vector]):
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
        Blueprint
     """
    """
    Args:
        x: int
        y: int
        null_exception: VectorNullException
        owner: Vector
        owner_name: str
    """
    x: int
    y: int
    null_exception: VectorNullException = VectorNullException()
    owner: Vector = Type[Vector]
    owner_name: str = type(owner).__name__