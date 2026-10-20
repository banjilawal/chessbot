# src/authorization/permitter/permitter.py

"""
Module: authorization.permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import Decision
from authorization import ApplicantReviewer, AuthorizationLoader
from exchange import PermissionRequest
from util import LoggingLevelRouter


T = TypeVar("T", bound="PermissionRequest")


class Authorizer(ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization
        -   Consistency and Integrity Management

    Responsibilities:
        1.  Check if a candidate satisfies the criteria to perform an operation.

    Attributes:
        loader: AuthorizationLoader[T]
        
    Provides:
        -  def process(self, form: T) -> Decision[T]:
        
    Super Class:
    """
    _loader: AuthorizationLoader[T]
    _applicant_reviewer: ApplicantReviewer[T]
    _permit_reviewer: PermitRevier[T]
    
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
    def execute(self, request: PermissionRequest[T]) -> Decision[T]:
        pass