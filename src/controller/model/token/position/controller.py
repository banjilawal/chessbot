# src/controller/model/token/position/controller.py

"""
Module: controller.model.token.position.controller
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from operation import TokenPositionPopper, TokenPushCoordProcess


class TokenPositionController:
    """
    Role:
        -   CRUD controller
        -   Consistency provider
        -   Integrity lifecycle manager
        
    Responsibilities:
        1.  Maintain integrity of a token's position schema during pushes and pops.
        
    Attributes:
        _popper: TokenPopCoordProcess
        _pusher: TokenPushCoordProcess
    
    Provides:
    Super Class:
    """
    _popper: TokenPositionPopper
    _pusher: TokenPushCoordProcess
    
    def __init__(
            self,
            popper: TokenPositionPopper,
            pusher: TokenPushCoordProcess,
    ):
        self._popper = popper
        self._pusher = pusher
        
        
    @property
    def pop(self) -> TokenPositionPopper:
        return self._popper
    
    @property
    def push(self) -> TokenPushCoordProcess:
        return self._pusher