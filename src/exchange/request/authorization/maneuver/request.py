# src/exchange/request/authorization/maneuver.request.py

"""
Module: exchange.request.authorization.maneuver.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ManeuverResult
from domain import Maneuverable, Token
from exchange import AuthorizationRequest


class ManeuverRequest(AuthorizationRequest[ManeuverResult]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides information a ManeuverAuthorizer needs to execute a Maneuver job.

     Attributes:
        actor: Token
        activity: Maneuverable

     Provides:

     Super Class:
        AuthorizationRequest
     """
    
    def __init__(self, id: int, actor: Token, activity: Maneuverable):
        """
        Args:
            id: int
            actor: Token
            activity: Maneuverable
        """
        super().__init__(id=id, actor=actor, activity=activity)
    
    @property
    def actor(self) -> Token:
        return cast(Token, super().actor)
    
    @property
    def activity(self) -> Maneuverable:
        return cast(Maneuverable, super().activity)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverRequest):
            return self.id == other.id
        return False