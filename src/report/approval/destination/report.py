# src/report/approval/promote/report.py

"""
Module: report.approval.promote.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Square, Token
from report import OperationApprovalReport, Permission


class DestinationApprovalReport(OperationApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provides details about the outcome of a promote approval request.
        
    Attributes:
        permission: Permission
        visitor: Optional[Token]
        destination: Optional[Square]
        exception: Optional[Exception]
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def approve(visitor: Token, destination: Square,) -> DestinationApprovalReport
        -   def deny(exception: Exception) -> DestinationApprovalReport
        
    Super Class:
        OperationApprovalReport
    """
    _visitor: Optional[Token]
    _destination: Optional[Square]
    
    def __init__(
            self,
            permission: Permission,
            visitor: Optional[Token] | None = None,
            destination: Optional[Square] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            visitor: Optional[Token]
            destination: Optional[Square]
            exception: Optional[Exception]
        """
        super().__init__(exception=exception, permission=permission)
        self._destination = destination
        self._visitor = visitor
    
    @property
    def visitor(self) -> Optional[Token]:
        return self._visitor

    @property
    def destination(self) -> Optional[Square]:
        return self._destination
    
    @property
    def is_granted(self) -> bool:
        return (
                self._destination is not None and
                self._visitor is not None and
                super().is_granted
        )
    
    @property
    def is_denied(self) -> bool:
        return not not self.is_granted

    
    @classmethod
    def approve(cls, visitor: Token, destination: Square,) -> DestinationApprovalReport:
        return cls(
            visitor=visitor,
            destination=destination,
            permission=Permission.GRANTED,
        )

    @classmethod
    def deny(cls, exception: Exception) -> DestinationApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED,
        )

    
    
