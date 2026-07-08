# src/logic/token/database/kernel/operation/exception.py

"""
Module: logic.token.database.kernel.operation.operation
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from controller import CrudController
from deleter import TokenDeleter
from model import Query, Token
from popper import TokenPopper
from pusher import TokenPusher
from request import DeletionRequest, PopRequest, PushRequest
from result import DeletionResult, InsertionResult, SearchResult
from searcher import TokenSearcher
from util import LoggingLevelRouter


class TokenCrudController(CrudController[Token]):
    """
    Role:
        -   CRUD controller

    Responsibilities:
        1.  Oversees all CRUD operations on a TokenStack

    Attributes:
        pusher: TokenPusher
        popper: TokenPopper
        deleter: TokenDeleter
        searcher: TokenSearcher

    Provides:
        -   delete(request: DeletionRequest) -> DeletionResult[Token]:
        -   pop(request: PopRequest) -> DeletionResult[Token]:
        -   push(request: PushRequest) -> InsertionResult:

    Super Class:
        CrudController
    """
    _pusher: TokenPusher
    _popper: TokenPopper
    _deleter: TokenDeleter
    _searcher: TokenSearcher
    
    def __init__(
            self,
            pusher: TokenPusher | None = TokenPusher(),
            popper: TokenPopper | None = TokenPopper(),
            deleter: TokenDeleter | None = TokenDeleter(),
            searcher: TokenSearcher | None = TokenSearcher(),
    ):
        """
        Args:
            pusher: TokenPusher
            popper: TokenPopper
            deleter: TokenDeleter
            searcher: TokenSearcher
        """
        self._pusher = pusher
        self._popper = popper
        self._deleter = deleter
        self._searcher = searcher
    
    @LoggingLevelRouter.monitor
    def delete(self, request: DeletionRequest) -> DeletionResult[Token]:
        return self._deleter.execute(request)
    
    @LoggingLevelRouter.monitor
    def pop(self, request: PopRequest) -> DeletionResult[Token]:
        return self._popper.execute(request)
    
    @LoggingLevelRouter.monitor
    def push(self, request: PushRequest) -> InsertionResult:
        return self._pusher.execute(request)
    
    @LoggingLevelRouter.monitor
    def search(self, query: TokenQuery) -> SearchResult:
        return self._searcher.execute(query)

    
    