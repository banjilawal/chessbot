# src/toolkit/model/operand/toolkit.py

"""
Module: toolkit.model.operand.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import CartesianOperandBlueprint
from err import CartesianOperandNullException, CartesianRegisterNullException
from operand import CartesianOperand

from suite import CoordOperationSuite, CartesianOperationSuite, VectorOperationSuite
from toolkit import Toolkit


@dataclass
@dataclass
class CartesianOperandToolkit(Toolkit[CartesianOperand]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and validators that are required for CartesianOperand tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        coord: CoordOperationSuite
        cartesian: CartesianOperationSuite
        null_exception: CartesianOperandNullException
        model: CartesianOperand

    Provides:

    Super Class:
        Toolkit
    """
    model: Type[CartesianOperand] = CartesianOperand
    blueprint_model: CartesianOperandBlueprint = CartesianOperandBlueprint
    
    null_exception: CartesianOperandNullException = CartesianRegisterNullException()
    null_exception: CartesianOperandNullException = CartesianOperandNullException()
    blueprint_null_exception: CartesianOperandBlueprintNullException = CartesianOperandBlueprintNullException()
    
    coord: CoordOperationSuite = CoordOperationSuite()
    vector: VectorOperationSuite = VectorOperationSuite()

