# src/toolkit/register/operand/toolkit.py

"""
Module: toolkit.register.operand.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from blueprint import VectorToggleRegisterBlueprint
from carrier import VectorToggleRegisterCarrier
from err import (
    VectorToggleRegisterBlueprintNullException, VectorToggleRegisterCarrierNullException,
    VectorToggleRegisterNullException
)
from register import VectorToggleRegister
from toggle import VectorToggle
from toolkit import RegisterToolkit
from validator import VectorToggleValidator


class VectorToggleRegisterToolkit(RegisterToolkit[VectorToggle]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for VectorToggleRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        vector_toggle_validator: VectorToggleValidator
        null_exception = VectorToggleRegisterNullException
        : VectorToggleRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    model: Type[VectorToggleRegister] = (
        VectorToggleRegister
    )
    carrier_model: Type[VectorToggleRegisterCarrier] = (
        VectorToggleRegisterCarrier
    )
    blueprint_model: Type[VectorToggleRegisterBlueprint] = (
        VectorToggleRegisterBlueprint
    )
    null_exception: VectorToggleRegisterNullException = (
        VectorToggleRegisterNullException()
    )
    carrier_null_exception: VectorToggleRegisterCarrierNullException = (
        VectorToggleRegisterCarrierNullException()
    )
    blueprint_null_exception: VectorToggleRegisterBlueprintNullException = (
        VectorToggleRegisterBlueprintNullException()
    )
    

    vector_toggle_validator: VectorToggleValidator = VectorToggleValidator()