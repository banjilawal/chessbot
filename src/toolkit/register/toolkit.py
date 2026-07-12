# src/toolkit/register/toolkit.py

"""
Module: toolkit.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Type, TypeVar

from blueprint import RegisterBlueprint
from err import RegisterBlueprintNullException, RegisterEntityNullException, RegisterNullException
from operand import RegisterCarrier
from register import Register
from toolkit import Toolkit

T = TypeVar("T", bound="Register")

@dataclass
class RegisterToolkit(Toolkit, Generic[T]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services an entity requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        model: Type[Register]
        blueprint_model: Type[RegisterBlueprint]
        operand_model: Type[RegisterDtoOperand]
        
        null_exception: RegisterNullException
        blueprint_null_exception: RegisterBlueprintNullException
        operand_null_exception: RegisterDtoNullException

    Provides:

    Super Class:
       Toolkit
    """
    model: Type[Register] = Register
    blueprint_model: Type[RegisterBlueprint] = RegisterBlueprint
    operand_model: Type[RegisterCarrier] = RegisterCarrier
    
    null_exception: RegisterNullException = RegisterNullException()
    blueprint_null_exception: RegisterBlueprintNullException = RegisterBlueprintNullException()
    operand_null_exception: RegisterEntityNullException = RegisterEntityNullException()


    