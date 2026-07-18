# src/blueprint/container/state/maneuver/blueprint.py

"""
Module: blueprint.container.state.maneuver.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type

from blueprint import StateContainerBlueprint
from err import ManeuverNullException
from container import Path, Maneuver, Token


@dataclass
class ManeuverBlueprint(StateContainerBlueprint[Maneuver]):
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
        container_type: Maneuver
        
    Provides:

     Super Class:
        StateContainerBlueprint
     """
    path: Path
    token: Token
    id: Optional[int] | None = None
    null_exception: ManeuverNullException = ManeuverNullException()
    container_class: Maneuver = Type[Maneuver]
    owner_name: str = type(owner).__name__
