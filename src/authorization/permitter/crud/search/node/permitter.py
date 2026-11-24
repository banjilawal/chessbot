# src/authorization/permitter/crud/search/permitter.py

"""
Module: authorization.permitter.crud.search.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import NodeSearchDecision
from authorization import SearchPermitter
from bootstrap import NodeSearchAuthorizationLoader
from exchange import NodeSearchPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="NodeSearchPermissionRequest")

class NodeSearchPermitter(SearchPermitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a searchDecision about a SearchPermissionRequest then forward
            that searchDecision to a SearchWorker.

    Attributes:
        loader: NodeSearchAuthorizationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> NodeSearchDecision

    Super Class:
        SearchPermitter
    """
    
    def __init__(self, loader: NodeSearchAuthorizationLoader[T]):
        """
        Args:
            loader: NodeSearchAuthorizationLoader[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> NodeSearchAuthorizationLoader[T]:
        return cast(NodeSearchAuthorizationLoader[T], super().loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> NodeSearchDecision:
        """
        Grant permission for a search activity.
        
        Args:
            candidate: Any
        Returns:
           SearchDecision
        Raises:
            SearchPermitterException
        """
        