# src/blueprint/model/register/blueprint.py

"""
Module: blueprint.model.register.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Type

from blueprint import Blueprint
from err import RegisterNullException
from model import Register


@dataclass
class RegisterBlueprint(Blueprint[Register]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides magnitude value for instantiating a Register object.

    Attributes:
        a: Any
        b: Any
        model_type: Register
        null_exception: RegisterNullException
    Provides:

     Super Class:
        Blueprint
     """
    a: Any
    b: Any
    null_exception: RegisterNullException = RegisterNullException()
    owner: Register = Type[Register]
    owner_name: str = type(owner).__name__
