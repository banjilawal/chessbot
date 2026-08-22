# src/toolkit/register/toggle/toolkit.py

"""
Module: toolkit.register.toggle.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from domain.metadata.blueprint import VectorToggleRegisterBlueprint
from carrier import VectorToggleRegisterCarrier
from err import (
    VectorToggleRegisterBlueprintNullException, VectorToggleRegisterCarrierNullException,
    VectorToggleRegisterNullException
)
from domain.structure.register import CartesianToggleRegister
from domain.structure.toggle import CartesianToggle
from toolkit.register.toggle.toolkit import RegisterToolkit
from assurance.validator import VectorToggleValidator


class VectorToggleRegisterToolkit(RegisterToolkit[CartesianToggle]):
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
    model: Type[CartesianToggleRegister] = (
        CartesianToggleRegister
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