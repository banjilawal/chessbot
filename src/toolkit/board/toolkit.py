# src/integrity/toolkit/board/toolkit.py

"""
Module: integrity.toolkit.board.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import ArenaService, BoardService, IdentityService
from model import Board
from toolkit import Toolkit


class BoardToolkit(Toolkit[Board]):
    """
    Role:
        -   Container
        
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        arena_service: ArenaService
        identity_service: IdentityService
        
    Provides:

     Super Class:
         Toolkit
     """
    _arena_service: ArenaService
    _identity_service: IdentityService

    def __init__(
            self,
            arena_service: ArenaService | None = None,
            identity_service: IdentityService | None = None,
    ):
        """
        Args:
            arena_service: ArenaService
            identity_service: IdentityService
        """
        super().__init__()
        self._arena_service = arena_service or BoardService()
        self._identity_service = identity_service or IdentityService()
        
    @property
    def arena_service(self) -> ArenaService:
        return self._arena_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service