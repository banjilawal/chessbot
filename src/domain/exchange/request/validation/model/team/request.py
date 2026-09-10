# src/domain/exchange/request/validation/model/team/request.py

"""
Module: domain.exchange.request.validation.model.team.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import ModelValidationRequest, Team
from transit import TeamCarrier


class TeamValidationRequest(ModelValidationRequest[Team]):
    """
     Role:
         - Messaging
         - Transport

     Responsibilities:
        1. Send job details to a TeamValidator.

     Attributes:
         id: int
         item: TeamCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: TeamCarrier):
        """
        Args:
            id: int
            item: TeamCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> TeamCarrier:
        return cast(TeamCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TeamValidationRequest):
            return self.id == other.id
        return False