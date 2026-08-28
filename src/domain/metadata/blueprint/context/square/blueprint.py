# src/domain/metadata/blueprint/context/square/blueprint.py

"""
Module: domain.metadata.blueprint.context.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import SquareSearchContextNullException
from domain.model import Board, Coord, Formation, SquareContext, Blueprint, SquareState, Token


@dataclass
class SquareContextBlueprint(Blueprint[SquareContext]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a SquareContext instance.

    Attributes:
        id: Optional[int]
        board: Optional[Board]
        coord: Optional[Coord]
        occupant: Optional[Token]
        state: Optional[State]
        formation: Optional[Formation]
        domain_null_exception: TamContextNullException
        context_model_type = SquareContext

    Provides:

    Super Class:
        ContextBlueprint
    """
    id: Optional[int] = None
    board: Optional[Board] = None
    coord: Optional[Coord] = None
    occupant: Optional[Token] = None
    state: Optional[SquareState] = None
    formation: Optional[Formation] = None
    domain_null_exception = SquareSearchContextNullException()
    context_model_type = SquareContext
