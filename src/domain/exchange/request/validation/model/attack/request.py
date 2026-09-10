# src/domain/exchange/request/validation/model/attack/request.py

"""
Module: domain.exchange.request.validation.model.attack.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import ModelValidationRequest, Attack
from transit import AttackCarrier


class AttackValidationRequest(ModelValidationRequest[Attack]):
    """
     Role:
         - Messaging
         - Transport

     Responsibilities:
        1. Send job details to a AttackValidator.

     Attributes:
         id: int
         item: AttackCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: AttackCarrier):
        """
        Args:
            id: int
            item: AttackCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> AttackCarrier:
        return cast(AttackCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackValidationRequest):
            return self.id == other.id
        return False