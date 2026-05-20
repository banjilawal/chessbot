# src/blueprint/validation/square/blueprint.py

"""
Module: blueprint.validation.query.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import SquareNullException
from model import Board, Coord, Formation, Square, Blueprint, SquareState, Token


@dataclass
class SquareQueryValidationBlueprint(QueryValidationBlueprint[Square]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a SquareValidation instance.

    Attributes:
        id: Optional[int]
        board: Optional[Board]
        coord: Optional[Coord]
        occupant: Optional[Token]
        state: Optional[State]
        formation: Optional[Formation]
        null_exception: TamNullException
        validation_model_type = SquareValidation

    Provides:

    Super Class:
        QueryValidationBlueprint
    """
    id: Optional[int] = None
    board: Optional[Board] = None
    coord: Optional[Coord] = None
    occupant: Optional[Token] = None
    state: Optional[SquareState] = None
    formation: Optional[Formation] = None
    null_exception = SquareNullException()
    validation_model_type = SquareValidation
