# src/blueprint/model/register/operand/blueprint.py

"""
Module: blueprint.model.register.operand.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import RegisterBlueprint
from err import VectorOperandRegisterNullException
from model import VectorOperand, PointRegister



@dataclass
class PointRegisterBlueprint(RegisterBlueprint[PointRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a VectorOperandRegister object.

    Attributes:
        a: VectorOperand
        b: VectorOperand
        null_exception: VectorOperandRegisterNullException
        owner: VectorOperandRegister
        owner_name: str
            
    Provides:

     Super Class:
        ModelBlueprint
     """
    """
    Args:
        a: VectorOperand
        b: VectorOperand
        null_exception: VectorOperandRegisterNullException
        owner: VectorOperandRegister
        owner_name: str
    """
    a: VectorOperand
    b: VectorOperand
    null_exception: VectorOperandRegisterNullException = VectorOperandRegisterNullException()
    model_class: PointRegister = Type[PointRegister]
    owner_name: str = type(owner).__name__
    
    

