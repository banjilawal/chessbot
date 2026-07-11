# src/toolkit/model/square/toolkit.py

"""
Module: toolkit.model.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import SquareBlueprint
from bootstrapper import PrimingValidator
from detector import SquareCollisionDetector
from err import SquareBlueprintNullException, SquareNullException
from model import Square
from operand import SquareDtoOperand
from toolkit import ModelToolkit
from validator import BoardValidator, CoordValidator, TokenValidator


@dataclass
class SquareToolkit(ModelToolkit[Square]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services a Square requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        model: Square = Square
        blueprint_model = SquareBlueprint
        operand_model: SquareDtoOperand
        
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
    operand_model: Type[SquareDtoOperand] = SquareDtoOperand

    null_exception: SquareNullException = SquareNullException()
    blueprint_null_exception: SquareBlueprintNullException = SquareBlueprintNullException()
    
    token_validator: TokenValidator = TokenValidator()
    board_validator: BoardValidator = BoardValidator()
    coord_validator: CoordValidator = CoordValidator()
    priming_validator: PrimingValidator = PrimingValidator()
    collision_detector: SquareCollisionDetector = SquareCollisionDetector()

