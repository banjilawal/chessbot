# src/blueprint/model/register/identity/blueprint.py

"""
Module: blueprint.model.register.identity.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import Blueprint
from model import IdentityRegister


@dataclass
class IdentityRegisterBlueprint(Blueprint[IdentityRegister]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a IdentityRegister object.

    Attributes:
        id: Int
        name: Str
        null_exception: IdentityRegisterNullException
        owner: IdentityRegister
        owner_name: str
            
    Provides:

     Super Class:
        Blueprint
     """
    """
    Args:
        id: int
        name: str
        null_exception: IdentityRegisterNullException
        owner: IdentityRegister
        owner_name: str
    """
    id: int
    name: str
    null_exception: IdentityRegisterNullException = IdentityRegisterNullException()
    owner: IdentityRegister = Type[IdentityRegister]
    owner_name: str = type(owner).__name__
