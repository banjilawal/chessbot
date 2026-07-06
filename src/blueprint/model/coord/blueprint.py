# src/blueprint/model/coord/blueprint.py

"""
Module: blueprint.model.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from blueprint import Blueprint
from err import CoordNullException
from model import Coord


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
        
    Provides:

     Super Class:
        Blueprint
     """
    row: int
    column: int
