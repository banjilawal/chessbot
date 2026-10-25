# src/authorization/authorizer/authorizer.py

"""
Module: authorization.authorizer.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import Decision
from authorization import ApplicantReviewer, AuthorizationLoader, RolePermitter
from exchange import PermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class Authorizer(ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Grant permission to perform an activity.

    Attributes:
        loader: AuthorizationLoader[T]
        role_permitter: RolePermitter[T]
        applicant_reviewer: ApplicantReviewer[T]

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
    """
    
    _loader: AuthorizationLoader[T]
    _role_permitter: RolePermitter[T]
    _applicant_reviewer: ApplicantReviewer[T]

    def __init__(
            self,
            loader: AuthorizationLoader[T],
            role_permitter: RolePermitter[T],
            applicant_reviewer: ApplicantReviewer[T],
    ):
        """
        Args:
            loader: AuthorizationLoader[T]
            role_permitter: RolePermitter[T]
            applicant_reviewer: ApplicantReviewer[T]
        """
        self._loader = loader
        self._role_permitter = role_permitter
        self._applicant_reviewer = applicant_reviewer
    
    @property
    def loader(self) -> AuthorizationLoader[T]:
        return self._loader
    
    @property
    def role_permitter(self) -> RolePermitter[T]:
        return self._role_permitter
    
    @property
    def applicant_reviewer(self) -> ApplicantReviewer[T]:
        return self._applicant_reviewer
    
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Grant permission for an activity.
        
        Args:
            request: T
        Returns:
           Decision[T]
        Raises:
            AuthorizerException
        """
        