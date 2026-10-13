# src/exchange/request/validation/struct/binder/team/request.py

"""
Module: exchange.request.validation.struct.binder.team.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import TeamBinder
from exchange import BinderValidationRequest
from transit import TeamBinderCarrier


class TeamBinderValidationRequest(
    BinderValidationRequest[TeamBinder]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a TeamBinderValidator
            needs to run a job.

     Attributes:
         id: int
         item: BinderCarrier[T]

     Provides:
     
     Super Class:
        BinderValidationRequest
     """
    
    def __init__(self, id: int, item: TeamBinderCarrier):
        """
        Args:
            id: int
            item: TeamBinderCarrier
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> TeamBinderCarrier:
        return cast(TeamBinderCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BinderValidationRequest):
            return self.id == other.id
        return False