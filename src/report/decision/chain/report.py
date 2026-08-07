# src/report/approval/chain/report.py

"""
Module: report.approval.chain.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from collection import Chain
from report import RequestDecision, Permission


T = TypeVar("T", bound="ChainCrudRequest")


class ChainCrudApprovalReport(RequestDecision, ABC, Generic[T]):
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
    _request: Optional[T]
    _chain: Optional[Chain[T]]
    
    def __init__(
            self,
            permission: Permission,
            request: Optional[T] | None = None,
            chain: Optional[Chain[T]] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        super().__init__(permission=permission, exception=exception)
        self._chain = chain
        self._request = request
    
    @property
    def request(self) -> Optional[T]:
        return cast(T, self._request)
    
    @property
    def request_is_denied(self) -> bool:
        return (
                self._request is None and
                self.exception is not None and
                self._permission == Permission.DENIED
        )
    
    @property
    def request_is_granted(self) -> bool:
        return (
                self.request is not None and
                self._exception is None and
                self._permission == Permission.GRANTED
        )
    
    @classmethod
    def approve(cls, request: T,) -> ChainCrudApprovalReport:
        return cls(request=request, permission=Permission.GRANTED)
    
    @classmethod
    def deny(cls, exception: Exception) -> ChainCrudApprovalReport:
        return cls(exception=exception, permission=Permission.DENIED)
    
