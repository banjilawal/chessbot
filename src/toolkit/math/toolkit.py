# src/toolkit/math/toolit.py

"""
Module: toolkit.math.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from model import VectorRegister
from toolkit import Toolkit
from integrity import CoordBuilder, ScalarBuilder, VectorBuilder
from validation import (
    CoordValidator, NumberValidator, ScalarValidator, VectorOperandValidator,
    VectorRegisterValidator, VectorValidator
)


@dataclass
class MathToolkit(Toolkit):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for VectorOperand tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        coord_validator: CoordValidator
        scalar_validator: ScalarValidator
        number_validator: NumberValidator
        vector_validator: VectorValidator
        vector_register_validator: VectorRegisterValidator
        vector_operand_validator: VectorOperandValidator
        
        coord_builder: CoordBuilder
        scalar_builder: ScalarBuilder
        vector_builder: VectorBuilder
    Provides:

     Super Class:
         Toolkit
     """
    coord_validator: CoordValidator = CoordValidator()
    scalar_validator: ScalarValidator = ScalarValidator()
    number_validator: NumberValidator = NumberValidator()
    vector_validator: VectorValidator = VectorValidator()
    vector_register_validator: VectorRegisterValidator = VectorRegisterValidator()
    vector_operand_validator: VectorOperandValidator = VectorOperandValidator()
    
    coord_builder: CoordBuilder = CoordBuilder()
    scalar_builder: ScalarBuilder = ScalarBuilder()
    vector_builder: VectorBuilder = VectorBuilder()
