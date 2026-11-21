# src/request/validation/context/team/request.py

"""
Module: request.validation.context.team.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import TeamContext
from request import ContextValidationRequest
from transit import TeamContextCarrier


class TeamContextValidationRequest(ContextValidationRequest[TeamContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about an TeamContextValidation job.

     Attributes:
         id: int
         item: TeamContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: TeamContextCarrier):
        """
        Args:
            id: int
            item: TeamContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> TeamContextCarrier:
        return cast(TeamContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TeamContextValidationRequest):
            return self.id == other.id
        return False