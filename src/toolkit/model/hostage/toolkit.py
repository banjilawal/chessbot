# src/toolkit/model/hostage/toolkit.py

"""
Module: toolkit.model.hostage.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import IdentityService, SquareService, TokenService
from model import Hostage
from toolkit import Toolkit


class HostageToolkit(Toolkit[Hostage]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Arena tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        token_service: TokenService
        square_service: SquareService
        identity_service: IdentityService
        
    Provides:

     Super Class:
         Toolkit
     """
    _token_service: TokenService
    _square_service: SquareService | None = None
    _identity_service: IdentityService | None = None

    def __init__(
            self,
            token_service: TokenService | None = None,
            square_service: SquareService | None = None,
            identity_service: IdentityService | None = None,
    ):
        """
        Args:
            token_service: TokenService
            square_service: SquareService
            identity_service: IdentityService
        """
        self._token_service = token_service
        self._square_service = square_service
        self._identity_service = identity_service
        
    @property
    def token_service(self) -> TokenService:
        return self._token_service
    
    @property
    def square_service(self) -> SquareService:
        return self._square_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service