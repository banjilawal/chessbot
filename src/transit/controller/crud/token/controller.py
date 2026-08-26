# src/transit/logic/token/database/kernel/operation/exception.py

"""
Module: logic.token.database.kernel.operation.operation
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from transit.controller import CrudController
from operation import TokenPusher

from domain.model import Token
from operation.crud.delete.stack.popper import TokenPopper
from operation.crud.insert.stack.pusher import TokenPusher
from domain.exchange.request import CollectionDeletionRequest, PopRequest, TokenStackPushRequest, SearchRequest
from artifcat import DeletionResult, InsertionResult, SearchResult
from operation.crud.search import TokenSearcher
from util import LoggingLevelRouter


class TokenCrudController(CrudController[Token]):
    """
    Role:
        -  CRUD controller

    Responsibilities:
        1.  Oversees all CRUD operations on a TokenStack

    Attributes:
        pusher: TokenPusher
        popper: TokenPopper
        deleter: TokenDeleter
        searcher: TokenSearcher

    Provides:
        -  delete(request: DeletionRequest) -> DeletionResult[Token]:
        -  pop(request: PopRequest) -> DeletionResult[Token]:
        -  push(request: PushRequest) -> InsertionResult:

    Super Class:
        CrudController
    """
    _push: TokenPusher
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
        self._push = pusher
        self._popper = popper
        self._deleter = deleter
        self._searcher = searcher
    
    @LoggingLevelRouter.monitor
    def delete(self, request: CollectionDeletionRequest) -> DeletionResult[Token]:
        return self._deleter.execute(request)
    
    @LoggingLevelRouter.monitor
    def pop(self, request: PopRequest) -> DeletionResult[Token]:
        return self._popper.execute(request)
    
    @LoggingLevelRouter.monitor
    def push(self, request: TokenStackPushRequest) -> InsertionResult:
        return self._push.execute(request)
    
    @LoggingLevelRouter.monitor
    def search(self, request: SearchRequest) -> SearchResult:
        return self._searcher.execute(request)

    
    