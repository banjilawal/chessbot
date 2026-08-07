# src/report/approval/chain/insertion/report.py

"""
Module: report.approval.chain.insertion.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Optional

from collection import Chain
from node import Node
from report import NodeInsertionApprovalReport, Permission



class InsertionOffsetApprovalReport(NodeInsertionApprovalReport):
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
    _offset: Optional[int]
    
    def __init__(
            self,
            permission: Permission,
            offset: Optional[int] | None = None,
            node: Optional[Node] | None = None,
            chain: Optional[Chain] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        super().__init__(node=node, chain=chain, permission=permission, exception=exception)
        self._offset = offset
    
    @property
    def offset(self) -> Optional[int]:
        return self._offset
    
    
    @property
    def request_is_denied(self) -> bool:
        return (
                super().request_is_denied and self._offset is None
        )
    
    @property
    def request_is_granted(self) -> bool:
        return (
                super().request_is_granted and self._offset is not None
        )
    
    @classmethod
    def approve(cls, node: Node, chain: Chain, offset: int, ) -> InsertionOffsetApprovalReport:
        return cls(offset=offset, node=node, chain=chain, permission=Permission.GRANTED)
    
    @classmethod
    def deny(cls, exception: Exception) -> InsertionOffsetApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )
    
    
