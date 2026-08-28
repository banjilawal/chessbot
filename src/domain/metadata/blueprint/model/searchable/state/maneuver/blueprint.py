# src/domain/metadata/blueprint/model/searchable/state/maneuver/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.maneuver.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type

from domain.metadata.blueprint import StateModelBlueprint
from err import ManeuverNullException
from domain.model import Path, Maneuver, Token


@dataclass
class ManeuverBlueprint(StateModelBlueprint[Maneuver]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Maneuver object.

    Attributes:
        path: Path
        token: Token
        id: Optional[int]
        domain_null_exception: ManeuverNullException
        model_type: Maneuver
        
    Provides:

     Super Class:
        StateModelBlueprint
     """
    path: Path
    token: Token
    id: Optional[int] | None = None
    domain_null_exception: ManeuverNullException = ManeuverNullException()
    domain_class: Maneuver = Type[Maneuver]
    owner_name: str = type(owner).__name__
