# src/request/maneuver/request.py

"""
Module: request.maneuver.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Square, Token
from request import Request


class ManeuverRequest(Request):
    """
     Role:
         -  Request
         -  Data Transport

     Responsibilities:
        1.  Provide information the ManeuverPermitter needs to approve a Token's journey.

     Attributes:
         id: int
         token: Token
         destination: Square

     Provides:
        -   def request(id: int, token: Token, destination: Square) -> ManeuverRequest:

     Super Class:
        Request
     """
    _token: Token
    _destination: Square
    
    def __init__(self, id: int, token: Token, destination: Square):
        """
        Args:
            id: int
            token: Token
            destination: Square
        """
        super().__init__(id=id)
        self._token = token
        self._destination: destination
        
    
    @property
    def token(self) -> T:
        return self._token
    
    @property
    def destination(self) -> Square:
        return self._destination
    
    @classmethod
    def request(cls, id: int, token: T, destination: Square) -> ManeuverRequest:
        return cls(id=id, token=token, destination=destination)