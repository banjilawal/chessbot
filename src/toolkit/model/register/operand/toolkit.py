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
from validation import VectorOperandValidator


class VectorOperandRegisterToolkit(RegisterToolkit[VectorOperand]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for VectorOperandRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        vector_operand_validator: VectorOperandValidator
        null_exception = VectorOperandRegisterNullException
        model: VectorOperandRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    vector_operand_validator: VectorOperandValidator = VectorOperandValidator()
    null_exception = VectorOperandRegisterNullException = VectorOperandRegisterNullException()
    model: VectorOperandRegister
    
