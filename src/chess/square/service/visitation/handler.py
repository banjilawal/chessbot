# src/chess/square/service/visitation/handlerpy

"""
Module: chess.square.service.visitation.__init__
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from chess.token import TokenService


class TokenVisitHandler:
    _token_service: TokenService
    
    def __init__(self, token_service: TokenService):
        self._token_service = token_service
        
    @property
    def token_service(self) -> TokenService:
        return self._token_service