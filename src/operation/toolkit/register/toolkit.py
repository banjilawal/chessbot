# src/operation/toolkit/register/toolkit.py

"""
Module: operation.toolkit.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Type, TypeVar

from domain.metadata.blueprint import RegisterBlueprint
from carrier import RegisterCarrier
from err import RegisterBlueprintNullException, RegisterCarrierNullException, RegisterNullException
from domain.structure.searchable.register import Register
from operation.toolkit.register.toolkit import Toolkit

T = TypeVar("T", bound="Register")

@dataclass
class RegisterToolkit(Toolkit, Generic[T]):
    """
    Role:
        - Dependency Management

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


    