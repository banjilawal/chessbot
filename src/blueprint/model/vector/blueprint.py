# src/blueprint/model/vector/blueprint.py

"""
Module: blueprint.model.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from blueprint import Blueprint
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
    x: int
    y: int
