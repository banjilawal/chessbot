# src/exchange/request/authorization/encounter.request.py

"""
Module: exchange.request.authorization.encounter.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import EncounterResult
from domain import Attackable, Token
from exchange import AuthorizationRequest


class EncounterRequest(AuthorizationRequest[EncounterResult]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides information an EncounterAuthorizer needs to execute a Encounter job.

     Attributes:
        applicant: Token
        activity: Attackable

     Provides:

     Super Class:
        AuthorizationRequest
     """
    
    def __init__(self, id: int, applicant: Token, activity: Attackable):
        """
        Args:
            id: int
            applicant: Token
            activity: Attackable
        """
        super().__init__(id=id, applicant=applicant, activity=activity)
    
    @property
    def applicant(self) -> Token:
        return cast(Token, super().applicant)
    
    @property
    def activity(self) -> Attackable:
        return cast(Attackable, super().activity)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EncounterRequest):
            return self.id == other.id
        return False