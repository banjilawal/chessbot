# src/operation/toolkit/register/toggle/toolkit.py

"""
Module: operation.toolkit.register.toggle.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from domain.metadata.blueprint import CartesianToggleRegisterBlueprint
from carrier import CartesianToggleRegisterCarrier
from err import (
    CartesianToggleRegisterBlueprintNullException, CartesianToggleRegisterCarrierNullException,
    CartesianToggleRegisterNullException
)
from domain.structure.searchable.register import CartesianToggleRegister
from domain.structure.toggle import CartesianToggle
from operation.toolkit.register.toggle.toolkit import RegisterToolkit
from transit.dispatcher.validator import CartesianToggleValidator


class CartesianToggleRegisterToolkit(RegisterToolkit[CartesianToggle]):
    """
    Role:
        - Container

    Responsibilities:
        1.  Collection of workers and services that are required for CartesianToggleRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        vector_toggle_validator: CartesianToggleValidator
        null_exception = CartesianToggleRegisterNullException
        : CartesianToggleRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    model: Type[CartesianToggleRegister] = (
        CartesianToggleRegister
    )
    carrier_model: Type[CartesianToggleRegisterCarrier] = (
        CartesianToggleRegisterCarrier
    )
    blueprint_model: Type[CartesianToggleRegisterBlueprint] = (
        CartesianToggleRegisterBlueprint
    )
    null_exception: CartesianToggleRegisterNullException = (
        CartesianToggleRegisterNullException()
    )
    carrier_null_exception: CartesianToggleRegisterCarrierNullException = (
        CartesianToggleRegisterCarrierNullException()
    )
    blueprint_null_exception: CartesianToggleRegisterBlueprintNullException = (
        CartesianToggleRegisterBlueprintNullException()
    )
    
    vector_toggle_validator: CartesianToggleValidator = CartesianToggleValidator()