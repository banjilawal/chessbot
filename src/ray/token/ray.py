# src/ray/token/ray.py

"""
Module: ray.token.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Token
from ray import SquareRay


class TokenSquareRay:
    """
    Role:
        -   DTO, Data Holder
        -   Transform

    Responsibilities:
        1.  Squares a token can visit if the token were at the TokenSquareRay's origin.
        2.  No guarantee that the Token owns the SquareRay.

    Attributes:
        token: Token
        square_ray: SquareRay
        token_owns_ray: bool
        token_does_not_own_ray: bool

    Provides:

    Super Class:
    """
    _token: Token
    _square_ray: SquareRay
    
    def __init__(self, token: Token, square_ray: SquareRay):
        """
        Args:
            token: Token
            square_ray: SquareRay
        """
        self._token = token
        self._square_ray = square_ray
        
    @property
    def token(self) -> Token:
        return self._token
    
    @property
    def square_ray(self) -> SquareRay:
        return self._square_ray
    
    @property
    def token_owns_ray(self) -> bool:
        if self._token is None or self._square_ray is None:
            return False
        if self._square_ray.is_empty:
            return False
        return self._square_ray.origin.occupant == self.token
    
    @property
    def token_does_not_own_ray(self) -> bool:
        return not self.token_owns_ray
        
    
        