# src/toolkit/register/vector/.py

"""
Module: toolkit.register.vector.
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from blueprint import VectorRegisterBlueprint
from carrier import VectorRegisterCarrier
from err import VectorRegisterBlueprintNullException, VectorRegisterCarrierNullException, VectorRegisterNullException
from register import VectorRegister
from toolkit import RegisterToolkit
from validator import VectorValidator


class VectorRegisterToolkit(RegisterToolkit[VectorRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for VectorRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        vector_validator: VectorValidator
        null_exception: VectorRegisterNullException
        : VectorRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    model: Type[VectorRegister] = (
        VectorRegister
    )
    carrier_model: Type[VectorRegisterCarrier] = (
        VectorRegisterCarrier
    )
    blueprint_model: Type[VectorRegisterBlueprint] = (
        VectorRegisterBlueprint
    )
    
    null_exception: VectorRegisterNullException = (
        VectorRegisterNullException()
    )
    carrier_null_exception: VectorRegisterCarrierNullException = (
        VectorRegisterCarrierNullException()
    )
    blueprint_null_exception: VectorRegisterBlueprintNullException = (
        VectorRegisterBlueprintNullException()
    )
    vector_validator: VectorValidator = VectorValidator()
    
    
