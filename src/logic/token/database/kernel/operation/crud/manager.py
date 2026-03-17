# src/logic/token/database/kernel/operation/handler.py

"""
Module: logic.token.database.kernel.operation.handler
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.token import TokenStackPopper, TokenStackPusher


class TokenStackCrudManager:
    """
    Role:
        - Utilities Provider

    Responsibilities:
        1.  Manage insertion/deletion operations for TokenStackService.

    Attributes:
        popper: TokenStackPopper
        pusher: TokenStackServicePusher

    Provides:
        -   push(
                    token: Token,
                    token_stack: TokenStackService,
                    rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
                    collision_detector: TokenCollisionDetector = TokenCollisionDetector(),
            ) -> InsertionResult

    Super Class:
    """
    
    _popper: TokenStackPopper
    _pusher: TokenStackPusher
    
    def __init__(
            self,
            popper: TokenStackPopper = TokenStackPopper(),
            pusher: TokenStackPusher = TokenStackPusher(),
    ):
        self._popper = popper
        self._pusher = pusher
        
    @property
    def popper(self) -> TokenStackPopper:
        return self._popper
    
    @property
    def pusher(self) -> TokenStackPusher:
        return self._pusher
    