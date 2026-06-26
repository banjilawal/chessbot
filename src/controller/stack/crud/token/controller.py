# src/logic/token/database/kernel/operation/exception.py

"""
Module: logic.token.database.kernel.operation.operation
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from search.token.resource import TokenQueryService
from worker.stack.token.pop import TokenStackPop
from operation.push.token import TokenPusher


class TokenStackCrudController:
    """
    Role:
        -   CRUD controller
        -   Consistency provider
        -   Integrity lifecycle manager

    Responsibilities:
        1.  Manage insertion/deletion operations for TokenStackService.

    Attributes:
        pop: TokenStackPop
        push: TokenStackServicePush

    Provides:
        -   push(
                    token: Token,
                    token_stack: TokenStackService,
                    rank_quota_analyzer: RankQuotaAnalysis = RankQuotaAnalysis(),
                    collision_detector: TokenCollisionAnalyst = TokenCollisionAnalyst(),
            ) -> InsertionResult

    Super Class:
    """
    
    _pop: TokenStackPop
    _push: TokenPusher
    _query: TokenQueryService
    
    def __init__(
            self,
            pop: TokenStackPop = TokenStackPop(),
            query: TokenQueryService = TokenQueryService(),
            push: TokenPusher = TokenPusher(),
    ):
        self._pop = pop
        self._push = push
        self._query = query
        
    @property
    def pop(self) -> TokenStackPop:
        return self._pop
    
    @property
    def push(self) -> TokenPusher:
        return self._push
    
    @property
    def query(self) -> TokenQueryService:
        return self._query
    
    
    