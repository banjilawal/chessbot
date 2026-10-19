# src/authorization/permitter/permitter.py

"""
Module: authorization.permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from authorization import AuthorizationLoader
from util import LoggingLevelRouter


T = TypeVar("T", bound="AuthorizationRequest")


class OperationPermitter(ABC, Generic[T]):
    """
    Role:
        - Permission Authorization
        - Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Handoff service requests to the adjudicator to run through its authorization checklist.
        2.  Supply adjudicator dependencies.
        3.  Wrap any exceptions adjudicator exceptions for debuggung the exception chain.
        4.  Cast to the approrpate Request type before forwarding Adjudicator approvals to the client

    Attributes:
        loader: AuthorizationLoader[T]
        
    Provides:
        -  def execute(self, request: Request) -> RequestDecision

    Super Class:
    """
    _loader: AuthorizationLoader[T]
    
    def __init__(self, loader: AuthorizationLoader[T]):
        """
        Args:
            loader: AuthorizationLoader[T]
        """
        self._loader = loader
        
    @property
    def loader(self) -> AuthorizationLoader[T]:
        return self._loader
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision[T]:
        pass