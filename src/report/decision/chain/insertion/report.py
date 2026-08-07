# src/report/approval/chain/insertion/report.py

"""
Module: report.approval.chain.insertion.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar, cast

from collection import Chain
from node import Node
from report import ChainCrudApprovalReport, RequestDecision, Permission


T = TypeVar("T", bound="NodeInserter")


class NodeInsertionApprovalReport(ChainCrudApprovalReport, ABC, Generic[T]):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Give details about a ChainOperationOperation approval.
        
    Attributes:
        exception: Optional[Exception]
        permission: Permission
        is_denied: bool
        is_granted: bool
        
    Provides:
        -   def approve(*args, **kwargs) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:

    Super Class:
        OperationApprovalReport
    """
    _node: Optional[Node]
    
    def __init__(
            self,
            permission: Permission,
            node: Optional[Node],
            exception: Optional[Exception] | None = None,
            chain: Optional[Chain] | None = None,
    ):
        super().__init__(chain=chain, permission=permission, exception=exception)
        self._node = node

    @property
    def chain(self) -> Optional[Chain]:
        return cast(Chain, super().chain)
    
    @property
    def node(self) -> Optional[Node]:
        return self._node
    
    @property
    def request_is_denied(self) -> bool:
        return (
                self.chain is None and
                self._node is None and
                self.exception is not None and
                self._permission == Permission.DENIED
        )
    
    @property
    def request_is_granted(self) -> bool:
        return (
            self.chain is not None and
            self.node is not None and
            self._exception is None and
            self._permission == Permission.GRANTED
        )
    
    @classmethod
    def approve(
            cls,
            node: T,
            chain: Chain[T],
            *args: Optional[tuple[Any, ...]] | None,
            **kwargs: Optional[dict[str, Any]] | None,
    ) -> ChainCrudApprovalReport:
        return cls(
            node=node,
            chain=chain,
            permission=Permission.GRANTED
        )
        
    @classmethod
    def deny(cls, exception: Exception) -> RequestDecision:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )
    
    
