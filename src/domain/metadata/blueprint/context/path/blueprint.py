# src/domain/metadata/blueprint/context/path/blueprint.py

"""
Module: domain.metadata.blueprint.context.path.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import PathSearchContextNullException
from domain.model import Board, Coord, Formation, PathContext, Blueprint, PathState, Token


@dataclass
class PathContextBlueprint(Blueprint[PathContext]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a PathContext instance.

    Attributes:
        id: Optional[int]
        board: Optional[Board]
        coord: Optional[Coord]
        occupant: Optional[Token]
        state: Optional[State]
        formation: Optional[Formation]
        domain_null_exception: TamContextNullException
        context_model_type = PathContext

    Provides:

    Super Class:
        ContextBlueprint
    """
    id: Optional[int] = None
    board: Optional[Board] = None
    coord: Optional[Coord] = None
    occupant: Optional[Token] = None
    state: Optional[PathState] = None
    formation: Optional[Formation] = None
    domain_null_exception = PathSearchContextNullException()
    context_model_type = PathContext
