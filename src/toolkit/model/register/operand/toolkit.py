# src/toolkit/model/register/operand/toolkit.py

"""
Module: toolkit.model.register.operand.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import VectorOperandRegisterNullException
from model import VectorOperand, VectorOperandRegister
from toolkit import RegisterToolkit
from validation import CoordValidator, ScalarValidator, VectorValidator


class VectorOperandRegisterToolkit(RegisterToolkit[VectorOperand]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for VectorOperandRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        coord_validator: CoordValidator
        scalar_validator: ScalarValidator
        vector_validator: VectorValidator
        null_exception = VectorOperandRegisterNullException
        model: VectorOperandRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    coord_validator: CoordValidator = CoordValidator()
    scalar_validator: ScalarValidator = ScalarValidator()
    vector_validator: VectorValidator = VectorValidator()
    null_exception = VectorOperandRegisterNullException = VectorOperandRegisterNullException()
    model: VectorOperandRegister
    
