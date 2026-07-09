# src/blueprint/model/register/identity/blueprint.py

"""
Module: blueprint.model.register.identity.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type, cast

from blueprint import RegisterBlueprint
from err import IdentityRegisterNullException
from model import IdentityRegister


@dataclass
class IdentityRegisterBlueprint(RegisterBlueprint[IdentityRegister]):
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
    
    def __init__(
            self,
            id: int,
            name: str,
            null_exception: IdentityRegisterNullException | None = IdentityRegisterNullException(),
            owner: IdentityRegister | None = Type[IdentityRegister],
            owner_name: str | None = type(IdentityRegister).__name__,
    ):
        """
        Args:
            id: int
            name: int
            null_exception: IdentityRegisterNullException
            owner: IdentityRegister
            owner_name: str
        """
        super().__init__(
            a=id,
            b=name,
            owner=owner,
            null_exception=null_exception,
            owner_name=owner_name,
        )
    
    @property
    def id(self) -> int:
        return cast(int, self.a)
    
    @property
    def name(self) -> str:
        return cast(str, self.b)
    
    @property
    def model(self):
        return Type[IdentityRegister]
    
    @property
    def null_exception(self) -> IdentityRegisterNullException:
        return IdentityRegisterNullException()
