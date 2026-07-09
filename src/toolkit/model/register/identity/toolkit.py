# src/toolkit/model/register/identity/toolkit.py

"""
Module: toolkit.model.register.identity.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from blueprint import IdentityRegisterBlueprint
from err import IdentityRegisterBlueprintNullException, IdentityRegisterNullException
from model import IdentityRegister
from toolkit import RegisterToolkit
from validator import NameValidator, NumberValidator


class IdentityRegisterToolkit(RegisterToolkit[IdentityRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for IdentityRegister tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        number_validator: NumberValidator
        name_validator: NameValidator
        null_exception = IdentityRegisterNullException
        model: IdentityRegister

    Provides:

    Super Class:
       RegisterToolkit
    """
    number_validator: NumberValidator = NumberValidator()
    name_validator: NameValidator = NameValidator()
    null_exception = IdentityRegisterNullException = IdentityRegisterNullException()
    model: Type[IdentityRegister]
    blueprint_model = Type[IdentityRegisterBlueprint]
    blueprint_null_exception = IdentityRegisterBlueprintNullException()
    
