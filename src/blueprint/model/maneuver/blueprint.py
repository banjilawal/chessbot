# src/blueprint/model/maneuver/blueprint.py

"""
Module: blueprint.model.maneuver.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type

from blueprint import Blueprint
from err import ManeuverNullException
from model import Path, Maneuver, Token


@dataclass
class ManeuverBlueprint(Blueprint[Maneuver]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Maneuver object.

    Attributes:
        path: Path
        token: Token
        id: Optional[int]
        null_exception: ManeuverNullException
        model_type: Maneuver
        
    Provides:

     Super Class:
        Blueprint
     """
    path: Path
    token: Token
    id: Optional[int] | None = None
    null_exception: ManeuverNullException = ManeuverNullException()
    owner: Maneuver = Type[Maneuver]
    owner_name: str = type(owner).__name__
