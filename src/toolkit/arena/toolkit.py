# src/toolkit/arena/toolkit.py

"""
Module: toolkit.arena.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import BoardService, IdentityService
from model import Arena
from toolkit import Toolkit


class ArenaToolkit(Toolkit[Arena]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Arena tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        board_service: BoardService
        identity_service: IdentityService
            
    Provides:

    Super Class:
        Toolkit
    """
    _board_service: BoardService
    _identity_service: IdentityService
    
    def __init__(
            self,
            board_service: BoardService | None = None,
            identity_service: IdentityService | None = None,
    ):
        """
        Args:
            board_service: BoardService
            identity_service: IdentityService
        """
        super().__init__()
        self._board_service = board_service or BoardService()
        self._identity_service = identity_service or IdentityService()
        
    @property
    def board_service(self) -> BoardService:
        return self._board_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
        
    
    