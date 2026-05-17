# src/model/blueprint/coord/model.py

"""
Module: model.blueprint.coord.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from err import CoordNullException
from model import Blueprint, Coord

@dataclass
class CoordBlueprint(Blueprint[Coord]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Coord object.

    Attributes:
        row: int
        column: int
        model_type: Coord
        null_exception: CoordNullException
        
    Provides:

     Super Class:
        Blueprint
     """
    row: int
    column: int
    model_type: Coord = Coord
    null_exception: CoordNullException = CoordNullException()
