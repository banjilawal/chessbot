# src/operation/toolkit/model/square/toolkit.py

"""
Module: operation.toolkit.model.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain.metadata.blueprint import SquareBlueprint
from bootstrapper import PrimingValidator
from carrier import SquareCarrier
from sensor.detector import SquareCollider
from err import SquareBlueprintNullException, SquareNullException
from domain.model import Square
from operation.toolkit.model.state.square.toolkit import StateModelToolkit
from transit.dispatcher.validator import BoardValidationDispatcher, CoordValidationDispatcher, TokenValidationDispatcher


@dataclass
class SquareToolkit(StateModelToolkit[Square]):
    """
    Role:
        -  Dependency Management

    Responsibilities:
        1.  Aggregates workers and services a Square requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        model: Square = Square
        blueprint_model = SquareBlueprint
        carrier_model: SquareDtoOperand
        
        null_exception: SquareNullException = SquareNullException()
        blueprint_null_exception: SquareBlueprintNullException = SquareBlueprintNullException()

        token_validator: TokenValidator
        board_validator: BoardValidator
        coord_validator: CoordValidator
        priming_validator: PrimingValidator
        collision_detector: SquareCollisionDetector

    Provides:

    Super Class:
       ModelToolkit
    """
    model: Type[Square] = Square
    blueprint_model: Type[SquareBlueprint] = SquareBlueprint
    carrier_model: Type[SquareCarrier] = SquareCarrier

    null_exception: SquareNullException = SquareNullException()
    blueprint_null_exception: SquareBlueprintNullException = SquareBlueprintNullException()
    
    token_validator: TokenValidationDispatcher = TokenValidationDispatcher()
    board_validator: BoardValidationDispatcher = BoardValidationDispatcher()
    coord_validator: CoordValidationDispatcher = CoordValidationDispatcher()
    priming_validator: PrimingValidator = PrimingValidator()
    collision_detector: SquareCollider = SquareCollider()

