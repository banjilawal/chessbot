# src/exchange/responder/attack/fatal/responder.py

"""
Module: exchange.responder.attack.fatal.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import KillResult
from exchange import AttackResponder, KillRequest
from util import LoggingLevelRouter


class KillResponder(AttackResponder[KillResult]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Fatal attack Request-Response workflow.

    Attributes:
        dispatcher: KillDispatcher

    Provides:
        -   def execute(request: KillRequest) -> KillResponse

    Super Class:
        AttackResponder
    """
    
    def __init__(self, dispatcher: Optional[KillDispatcher] | None = None):
        """
        Args:
            dispatcher: Optional[KillDispatcher]
        """
        super().__init__(dispatcher=dispatcher or KillDispatcher())
        
    @property
    def dispatcher(self) -> KillDispatcher:
        return cast(KillDispatcher, super().dispatcher)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: KillRequest) -> KillResponse:
        """
        Args:
            request: KillRequest
        Result:
            KillResponse
        Raises:
            KillResponderException
        """
        pass