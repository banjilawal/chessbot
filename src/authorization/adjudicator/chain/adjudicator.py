# src/authorization/adjudicator/chain/adjudicator.py

"""
Module: authorization.adjudicator.chain.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from assurance import NodeValidator
from authorization import ChainAdjudicationBootstrapper, RequestAdjudicator
from artifcat.report import AuthorizationDecision
from util import LoggingLevelRouter

N = TypeVar("N", bound="Node")
T = TypeVar("R", bound="ChainRequest")


class ChainRequestAdjudicator(RequestAdjudicator, ABC, Generic[N, R]):
    """
    Role:
        -   Permission Authorization
        -   Checklist Runner
        -   Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Run safety checks on a ChainRequest.

    Attributes:
        node_validator: NodeValidator[N]
        bootstrapper: Optional[ChainAdjudicationBootstrapper]

    Provides:
        -    def execute(self, candidate: Any) -> RequestDecision

    Super Class:
        RequestAdjudicator
    """
    _node_validator: NodeValidator[N]
    _bootstrapper: Optional[ChainAdjudicationBootstrapper]
    
    def __init__(
            self,
            node_validator: NodeValidator[N],
            bootstrapper: Optional[ChainAdjudicationBootstrapper] | None = None
    ):
        """
        Args:
            node_validator: NodeValidator[N]
            bootstrapper: Optional[ChainAdjudicationBootstrapper]
        """
        super().__init__()
        self._node_validator = node_validator
        self._bootstrapper = bootstrapper or ChainAdjudicationBootstrapper()
        
    @property
    def bootstrapper(self) -> ChainAdjudicationBootstrapper:
        return self._bootstrapper
        
    @property
    def node_validator(self) -> NodeValidator[N]:
        return self._node_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AuthorizationDecision:
        pass