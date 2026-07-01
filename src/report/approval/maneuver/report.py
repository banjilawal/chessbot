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


class ManeuverApproval(OperationApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provides details about the outcome of a promote approval request.
        
    Attributes:
        token: T
        origin: Origin
        exception: Optional[Exception]
        permission: Permission
        
    Provides:
        -   def approve(token: T, origin: Origin) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:
        
    Super Class:
        OperationApprovalReport
    """
    _token: Optional[Token]
    _origin: Optional[Square]
    _destination: Optional[Square]
    
    def __init__(
            self,
            permission: Permission,
            token: Optional[Token] | None = None,
            origin: Optional[Square] | None = None,
            destination: Optional[Square] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._token = token
        self._origin = origin
        self._destination = destination
    
    
    @property
    def token(self) -> Optional[Token]:
        return self._token
    
    @property
    def origin(self) -> Optional[Square]:
        return self._origin
    
    @property
    def destination(self) -> Optional[Square]:
        return self._destination
    
    @property
    def is_denied(self) -> bool:
        return (
                self._token is None and
                self._origin is None and
                self.destination is None and
                super().is_denied
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._token is not None and
            self._origin is not None and
            self._destination is not None and
            super().is_granted
        )
    
    @classmethod
    def approve(
            cls, 
            token: Token, 
            origin: Square,
            destination: Square,
    ) -> ManeuverApproval:
        return cls(
            token=token,
            origin=origin,
            destination=destination,
            permission=Permission.GRANTED
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> ManeuverApproval:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )

    
    
