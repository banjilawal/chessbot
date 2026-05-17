# src/model/blueprint/vector/model.py

"""
Module: model.blueprint.vector.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from err import VectorNullException
from model import Blueprint, Vector

@dataclass
class VectorBlueprint(Blueprint[Vector]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Vector object.

    Attributes:
        x: int
        y: int
        model_type: Vector
        null_exception: VectorNullException
            
    Provides:

     Super Class:
        Blueprint
     """
    x: int
    y: int
    model_type = Vector
    null_exception = VectorNullException()
