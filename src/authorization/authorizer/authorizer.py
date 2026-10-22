# src/authorization/authorizer/authorizer.py

"""
Module: authorization.authorizer.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from authorization import RoleReviewer, ApplicantReviewer, AuthorizationLoader
from exchange import AuthorizationRequest
from util import LoggingLevelRouter


T = TypeVar("T", bound="AuthorizationRequest")


class Authorizer(ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization
        -   Consistency and Integrity Management

    Responsibilities:
        1.  Check if a candidate satisfies the criteria to perform an operation.

    Attributes:
        loader: AuthorizationLoader[T]
        role_reviewer: RoleReviewer[T]
        applicant_reviewer: ApplicantReviewer[T]
        
    Provides:
        -  def process(self, form: T) -> Decision[T]:
        
    Super Class:
    """
    _loader: AuthorizationLoader[T]
    _role_reviewer: RoleReviewer[T]
    _applicant_reviewer: ApplicantReviewer[T]

    
    def __init__(
            self,
            loader: AuthorizationLoader[T],
            role_reviewer: RoleReviewer[T],
            applicant_reviewer: ApplicantReviewer[T],
    ):
        """
        Args:
            loader: AuthorizationLoader[T]
            role_reviewer: RoleReviewer[T]
            applicant_reviewer: ApplicantReviewer[T]
        """
        self._loader = loader
        self._role_reviewer = role_reviewer
        self._applicant_reviewer = applicant_reviewer
        
    @property
    def loader(self) -> AuthorizationLoader[T]:
        return self._loader
    
    @property
    def role_reviewer(self) -> RoleReviewer[T]:
        return self._role_reviewer
    
    @property
    def applicant_reviewer(self) -> ApplicantReviewer[T]:
        return self._applicant_reviewer
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest[T]) -> Decision[T]:
        """
        Checks if an AuthorizationRequest can be granted.
        
        Args:
            request: AuthorizationRequest[T]
        Returns:
           Decision[T]
        Raises:
            AuthorizerException
        """
        pass