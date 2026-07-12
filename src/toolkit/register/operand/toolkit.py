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
    CartesianRegisterBlueprintNullException,
    CartesianRegisterNullException
)
from  import VectorOperand, PointRegister
from toolkit import RegisterToolkit
from validator.register.operand import VectorOperandValidator


class CartesianRegisterToolkit(RegisterToolkit[VectorOperand]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for CartesianRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        cartesian_validator: VectorOperandValidator
        null_exception = CartesianRegisterNullException
        : CartesianRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    cartesian_validator: VectorOperandValidator = VectorOperandValidator()
    : PointRegister
    null_exception = CartesianRegisterNullException()
    blueprint_ = PointRegisterBlueprint
    blueprint_null_exception = CartesianRegisterBlueprintNullException()
    #
    # @property
    # def (self) -> Type[VectorOperand]:
    #     return Type[CartesianRegister]
    #
    # @property
    # def null_exception(self) -> CartesianRegisterNullException:
    #     return CartesianRegisterNullException()
    #
    # @property
    # def blueprint_(self) -> CartesianRegisterBlueprint:
    #     return Type[CartesianRegisterBlueprint]
    #
    # @property
    # def blueprint_null_exception(self) -> CartesianRegisterBlueprintNullException:
    #     return CartesianRegisterBlueprintNullException()
    
