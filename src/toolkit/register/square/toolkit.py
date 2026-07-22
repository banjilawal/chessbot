# src/toolkit/register/square/.py

"""
Module: toolkit.register.square.
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import SquareRegisterBlueprint
from carrier import SquareRegisterCarrierToggle
from err import (
    SquareRegisterBlueprintNullException, SquareRegisterCarrierNullException, SquareRegisterNullException
)
from register import SquareRegister
from toolkit import RegisterToolkit
from validator import SquareValidator


class SquareRegisterToolkit(RegisterToolkit[SquareRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for SquareRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        square_validator: SquareValidator
        null_exception: SquareRegisterNullException
        : SquareRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    model: Type[SquareRegister] = (
        SquareRegister
    )
    carrier_model: Type[SquareRegisterCarrierToggle] = (
        SquareRegisterCarrierToggle
    )
    blueprint_model: Type[SquareRegisterBlueprint] = (
        SquareRegisterBlueprint
    )
    
    null_exception: SquareRegisterNullException = (
        SquareRegisterNullException()
    )
    carrier_null_exception: SquareRegisterCarrierNullException = (
        SquareRegisterCarrierNullException()
    )
    blueprint_null_exception: SquareRegisterBlueprintNullException = (
        SquareRegisterBlueprintNullException()
    )

    square_validator: SquareValidator = SquareValidator()
    
