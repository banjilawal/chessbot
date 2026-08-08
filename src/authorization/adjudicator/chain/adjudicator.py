# src/authorization/adjudicator/chain/adjudicator.py

"""
Module: authorization.adjudicator.chain.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from assurance import NodeValidator, PrimingValidator
from authorization import RequestAdjudicator
from report import RequestDecision
from util import LoggingLevelRouter

N = TypeVar("N", bound="Node")
R = TypeVar("R", bound="ChainRequest")


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
        node_validator: NodeValidator[T]
        priming_validator: Optional[PrimingValidator]

    Provides:
        -    def execute(self, candidate: Any) -> RequestDecision

    Super Class:
        RequestAdjudicator
    """
    _node_validator: NodeValidator[N]
    
    def __init__(
            self,
            node_validator: NodeValidator[N],
            priming_validator: Optional[PrimingValidator] | None = None
    ):
        """
        Args:
            node_validator: NodeValidator[N]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(priming_validator=priming_validator)
        self._node_validator = node_validator
        
    @property
    def node_validator(self) -> NodeValidator[N]:
        return self._node_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> RequestDecision:
        pass