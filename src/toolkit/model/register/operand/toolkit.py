# src/toolkit/model/register/operand/toolkit.py

"""
Module: toolkit.model.register.operand.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from blueprint import VectorOperandRegisterBlueprint
from err import (
    VectorOperandRegisterBlueprintNullException,
    VectorOperandRegisterNullException
)
from model import VectorOperand, VectorOperandRegister
from toolkit import RegisterToolkit
from validator.model.register.operand import VectorOperandValidator


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
    model: Type[VectorOperandRegister]
    null_exception = VectorOperandRegisterNullException()
    blueprint_model = Type[VectorOperandRegisterBlueprint]
    blueprint_null_exception = VectorOperandRegisterBlueprintNullException()
    #
    # @property
    # def model(self) -> Type[VectorOperand]:
    #     return Type[VectorOperandRegister]
    #
    # @property
    # def null_exception(self) -> VectorOperandRegisterNullException:
    #     return VectorOperandRegisterNullException()
    #
    # @property
    # def blueprint_model(self) -> VectorOperandRegisterBlueprint:
    #     return Type[VectorOperandRegisterBlueprint]
    #
    # @property
    # def blueprint_null_exception(self) -> VectorOperandRegisterBlueprintNullException:
    #     return VectorOperandRegisterBlueprintNullException()
    
