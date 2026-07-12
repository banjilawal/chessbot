# src/toolkit/register/operand/toolkit.py

"""
Module: toolkit.register.operand.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from blueprint import PointRegisterBlueprint
from err import (
    VectorOperandRegisterBlueprintNullException,
    CartesianRegisterNullException
)
from  import VectorOperand, PointRegister
from toolkit import RegisterToolkit
from validator.register.operand import VectorOperandValidator


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
        : VectorOperandRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    vector_operand_validator: VectorOperandValidator = VectorOperandValidator()
    : PointRegister
    null_exception = CartesianRegisterNullException()
    blueprint_ = PointRegisterBlueprint
    blueprint_null_exception = VectorOperandRegisterBlueprintNullException()
    #
    # @property
    # def (self) -> Type[VectorOperand]:
    #     return Type[VectorOperandRegister]
    #
    # @property
    # def null_exception(self) -> VectorOperandRegisterNullException:
    #     return VectorOperandRegisterNullException()
    #
    # @property
    # def blueprint_(self) -> VectorOperandRegisterBlueprint:
    #     return Type[VectorOperandRegisterBlueprint]
    #
    # @property
    # def blueprint_null_exception(self) -> VectorOperandRegisterBlueprintNullException:
    #     return VectorOperandRegisterBlueprintNullException()
    
