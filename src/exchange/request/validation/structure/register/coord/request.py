# src/exchange/request/validation/struct/register/coord/request.py

"""
Module: exchange.request.validation.struct.register.coord.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import CoordRegister
from exchange import RegisterValidationRequest
from transit import CoordRegisterCarrier


class CoordRegisterValidationRequest(
    RegisterValidationRequest[CoordRegister]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a CoordRegisterValidator
            needs to run a job.

     Attributes:
         id: int
         item: Any

     Provides:
     
     Super Class:
        RegisterValidationRequest
     """
    
    def __init__(self, id: int, item: CoordRegisterCarrier):
        """
        Args:
            id: int
            item: CoordRegister
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> CoordRegisterCarrier:
        return cast(CoordRegisterCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RegisterValidationRequest):
            return self.id == other.id
        return False