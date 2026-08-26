# src/authorization/adjudicator/chain/search/request.py

"""
Module: authorization.adjudicator.chain.search.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from authorization import ChainRequest, ChainRequestAdjudicator
from collection import Chain

# src/authorization/adjudicator/chain/search/adjudicator.py

"""
Module: authorization.adjudicator.chain.search.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from artifcat.report import AuthorizationDecision
from util import LoggingLevelRouter

N = TypeVar("N", bound="Node")
R = TypeVar("R", bound="ChainSearchRequest")


class ChainSearchRequestAdjudicator(ChainRequestAdjudicator, Generic[N, R]):
    """
    Role:
        -  Permission Authorization
        -  Checklist Runner
        -  Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Run safety checks on a ChainSearchRequest.

    Attributes:
        node_validator: NodeValidator[N]
        priming_validator: Optional[PrimingValidator]

    Provides:
        -   def execute(self, candidate: Any) -> RequestDecision

    Super Class:
        ChainRequestAdjudicator
    """
    _node_validator: NodeValidator[N]
    
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
        super().__init__(bootstrapper=bootstrapper)
        self._node_validator = node_validator
        self._bootstrapper = bootstrapper
    
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


T = TypeVar("T", bound="Node")


class ChainSearchRequest(ChainRequest, ABC, Generic[T]):
    """
    Role:
        -  Request

    Responsibilities:
        1. Carry information for firing a Node search in a Chain.

    Attributes:
        id: int
        target: T
        chain: Chain[T]

    Provides:

    Super Class:
        ChainRequest
    """
    _target: T
    
    def __init__(self, id: int, target: T, chain: Chain[T],):
        """
        Args:
            id: int
            target: T
            chain: Chain[T]
        """
        super().__init__(id=id, chain=chain,)
        self._target = target
        
    @property
    def target(self) -> T:
        return self._target

