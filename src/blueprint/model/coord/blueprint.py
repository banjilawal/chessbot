# src/blueprint/model/coord/blueprint.py

"""
Module: blueprint.model.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Type

from blueprint import ModelBlueprint
from err import CoordNullException
from model import Coord


@dataclass
class CoordBlueprint(ModelBlueprint[Coord]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Coord object.

    Attributes:
        row: int
        column: int
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    row: int
    column: int
    null_exception: CoordNullException = CoordNullException()
    model_class: Coord = Type[Coord]
    owner_name: str = type(owner).__name__
