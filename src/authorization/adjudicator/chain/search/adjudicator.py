# src/authorization/request/chain/search/request.py

"""
Module: authorization.request.chain.search.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from authorization import ChainRequest
from collection import Chain

# src/authorization/adjudicator/chain/search/adjudicator.py

"""
Module: authorization.adjudicator.chain.search.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from assurance import PrimingValidator
from authorization import RequestAdjudicator
from report import RequestDecision
from util import LoggingLevelRouter

N = TypeVar("N", bound="Node")
R = TypeVar("R", bound="ChainSearchRequest")


class ChainSearchRequestAdjudicator(ChainRequestAdjudicator, Generic[N, R]):
    """
    Role:
        -   Permission Authorization
        -   Checklist Runner
        -   Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Run safety checks on a ChainSearchRequest.

    Attributes:
        node_validator: NodeValidator[N]
        priming_validator: Optional[PrimingValidator]

    Provides:
        -    def execute(self, candidate: Any) -> RequestDecision

    Super Class:
        ChainRequestAdjudicator
    """
    
    def __init__(
            self,
            node_validator: NodeValidator[N],
            priming_validator: Optional[PrimingValidator] | None = None):
        """
        Args:
            node_validator: NodeValidator[N]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(node_validator=node_validator, priming_validator=priming_validator)


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

