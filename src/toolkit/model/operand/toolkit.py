# src/toolkit/model/operand/toolkit.py

"""
Module: toolkit.model.operand.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from err import VectorOperandNullException, VectorOperandRegisterNullException
from model import VectorOperand
from suite import CoordOperationSuite, VectorOperationSuite
from toolkit import ModelToolkit


@dataclass
@dataclass
class VectorOperandToolkit(ModelToolkit[VectorOperand]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and validators that are required for VectorOperand tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        coord: CoordOperationSuite
        vector: VectorOperationSuite
        null_exception: VectorOperandNullException
        model: VectorOperand

    Provides:

    Super Class:
        Toolkit
    """
    coord: CoordOperationSuite = CoordOperationSuite()
    vector: VectorOperationSuite = VectorOperationSuite()
    null_exception: VectorOperandNullException = VectorOperandRegisterNullException()
    model: VectorOperand = VectorOperand
    blueprint_model: VectorOperandBlueprint = VectorOperandBlueprint
    null_exception: VectorOperandNullException = VectorOperandNullException()
    blueprint_null_exception: VectorOperandBlueprintNullException = VectorOperandBlueprintNullException()
