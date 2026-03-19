# src/logic/token/service/operation/coord/handler.py

"""
Module: logic.token.service.operation.coord.handler
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from logic.token import TokenPopCoordProcess, TokenPushCoordProcess


class TokenPositionController:
    """
    Role:
        -   CRUD controller
        -   Consistency provider
        -   Integrity lifecycle manager
        
    Responsibilities:
        1.  Maintain integrity of a token's position stack during pushes and pops..
        
    Attributes:
        _pop_process: TokenPopCoordProcess
        _push_process: TokenPushCoordProcess
    
    Provides:
    Super Class:
    """
    _pop_process: TokenPopCoordProcess
    _push_process: TokenPushCoordProcess
    
    def __init__(
            self,
            pop_process: TokenPopCoordProcess,
            push_process: TokenPushCoordProcess,
    ):
        self._pop_process = pop_process
        self._push_process = push_process
        
        
    @property
    def pop(self) -> TokenPopCoordProcess:
        return self._pop_process
    
    @property
    def push(self) -> TokenPushCoordProcess:
        return self._push_process