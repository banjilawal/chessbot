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
from carrier import RegisterCarrier
from err import RegisterBlueprintNullException, RegisterCarrierNullException, RegisterNullException
from register import Register
from toolkit import Toolkit

T = TypeVar("T", bound="Register")

@dataclass
class RegisterToolkit(Toolkit, Generic[T]):
    """
    Role:
        -   Dependency Management

    Responsibilities:
        1.  Bundles dependencies a worker needs to complete its task.
        2.  Loose Coupling between an operation and its resources.
        3.  Simplify Entry points.

    Attributes:
        model: Type[Register]
        blueprint_model: Type[RegisterBlueprint]
        carrier_model: Type[RegisterDtoOperand]
        
        null_exception: RegisterNullException
        blueprint_null_exception: RegisterBlueprintNullException
        carrier_null_exception: RegisterDtoNullException

    Provides:

    Super Class:
       Toolkit
    """
    model: Type[Register] = Register
    blueprint_model: Type[RegisterBlueprint] = RegisterBlueprint
    carrier_model: Type[RegisterCarrier] = RegisterCarrier
    
    null_exception: RegisterNullException = RegisterNullException()
    blueprint_null_exception: RegisterBlueprintNullException = RegisterBlueprintNullException()
    carrier_null_exception: RegisterCarrierNullException = RegisterCarrierNullException()


    