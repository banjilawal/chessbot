# src/client/request/validation/structure/register/square/request.py

"""
Module: client.request.validation.structure.register.square..request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from client import RegisterValidationRequest, SquareRegister


class SquareRegisterValidationRequest(RegisterValidationRequest[SquareRegister]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a SquareRegisterValidator
            needs to run a job.

     Attributes:
         id: int
         item: Any

     Provides:
     
     Super Class:
        RegisterValidationRequest
     """
    
    def __init__(self, id: int, item: SquareRegister):
        """
        Args:
            id: int
            item: SquareRegister
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> SquareRegister:
        return cast(SquareRegister, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RegisterValidationRequest):
            return self.id == other.id
        return False