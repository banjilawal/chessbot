# src/domain/metadata/blueprint/context/maneuver/blueprint.py

"""
Module: domain.metadata.blueprint.context.maneuver.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import ManeuverSearchContextNullException
from domain.model import Board, Coord, Formation, ManeuverContext, Blueprint, ManeuverState, Token


@dataclass
class ManeuverContextBlueprint(Blueprint[ManeuverContext]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a ManeuverContext instance.

    Attributes:
        id: Optional[int]
        board: Optional[Board]
        coord: Optional[Coord]
        occupant: Optional[Token]
        state: Optional[State]
        formation: Optional[Formation]
        domain_null_exception: TamContextNullException
        context_model_type = ManeuverContext

    Provides:

    Super Class:
        ContextBlueprint
    """
    id: Optional[int] = None
    board: Optional[Board] = None
    coord: Optional[Coord] = None
    occupant: Optional[Token] = None
    state: Optional[ManeuverState] = None
    formation: Optional[Formation] = None
    domain_null_exception = ManeuverSearchContextNullException()
    context_model_type = ManeuverContext
