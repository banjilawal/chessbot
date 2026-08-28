# src/operation/toolkit/register/vector/.py

"""
Module: operation.toolkit.register.vector.
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from domain.metadata.blueprint import VectorRegisterBlueprint
from carrier import VectorRegisterCarrier
from err import VectorRegisterBlueprintNullException, VectorRegisterCarrierNullException, VectorRegisterNullException
from domain.structure.searchable.register import VectorRegister
from operation.toolkit.register.vector.toolkit import RegisterToolkit
from transit.dispatcher.validator import VectorValidator


class VectorRegisterToolkit(RegisterToolkit[VectorRegister]):
    """
    Role:
        - Container

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
    
    
