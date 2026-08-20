# src/authorization/authorization.py

"""
Module: authorization.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from report import AuthorizationDecision
from request import Request
from result import Result
from toolkit import RequestToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")


class RequestAuthorizer(ABC, Generic[T]):
    _toolkit: RequestToolkit[T]
    
    def __init__(self, toolkit: RequestToolkit[T]):
        """
        Args:
            toolkit: RequestToolkit[T]
        """
        self._toolkit = toolkit
        
    @property
    def toolkit(self) -> RequestToolkit[T]:
        return self._toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Request[T]) -> AuthorizationDecision:
        pass