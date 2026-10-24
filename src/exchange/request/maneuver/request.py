# src/exchange/request/maneuver/request.py

"""
Module: exchange.request.maneuver.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from artifcat import ManeuverResult
from domain import Path, Token
from exchange import Request

class ManeuverRequest(Request[ManeuverResult]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a maneuver job.

     Attributes:
        token: Token
        path: Elevatable

     Provides:
     
     Super Class:
        Request
     """
    _token: Token
    _path: Path
    
    def __init__(
            self,
            id: int,
            token: Token,
            path: Path,
    ):
        """
        Args:
            id: int
            token: Token
            path: Path
        """
        super().__init__(id=id)
        self._token = token
        self._path = path
        
    @property
    def token(self) -> Token:
        return self._token
    
    @property
    def path(self) -> Path:
        return self._path
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverRequest):
            return self.id == other.id
        return False