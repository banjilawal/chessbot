# src/model/blueprint/context/square/blueprint.py

"""
Module: model.blueprint.context.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import SquareContextNullException
from model import Board, Coord, Formation, SquareContext, Blueprint, SquareState, Token


@dataclass
class SquareContextBlueprint(Blueprint[SquareContext]):
    board: Optional[Board] = None
    coord: Optional[Coord] = None
    occupant: Optional[Token] = None
    state: Optional[SquareState] = None
    formation: Optional[Formation] = None
    null_exception = SquareContextNullException()
    model_type = SquareContext
