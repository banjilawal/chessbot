# src/report/approval/token/report.py

"""
Module: report.approval.token.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from report import OperationApprovalReport, Permission
from token import TokenService

T = TypeVar("T", bound="TokenOperation")


class TokenOperationApprovalReport(OperationApprovalReport, ABC, Generic[T]):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Give details about an operationOperation approval.
        
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
    _token: Optional[TokenService]
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            token: Optional[TokenService] | None = None,
    ):
        super().__init__(permission=permission, exception=exception)
        self._token = token

    @property
    def token(self) -> Optional[TokenService]:
        return self._token
    
    @property
    def is_denied(self) -> bool:
        return (
                self._token is None and
                self._exception is not None and
                self._permission == Permission.DENIED
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._token is not None and
            self._exception is None and
            self._permission == Permission.GRANTED
        )
    
    @classmethod
    @abstractmethod
    def approve(
            cls,
            token: TokenService,
            *args: Optional[tuple[Any, ...]],
            **kwargs: Optional[dict[str, Any]],
    ) -> OperationApprovalReport:
        pass
    
    @classmethod
    def deny(cls, exception: Exception) -> OperationApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )
    
    
