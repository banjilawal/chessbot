# src/bootstrap/authorization/loader.py

"""
Module: bootstrap.authorization.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import CrudDecision
from bootstrap import AuthorizationLoader
from exchange import CrudPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="CrudPermissionRequest")

class CrudAuthorizationLoader(AuthorizationLoader[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a CrudAuthorization module.

    Attributes:

    Provides:
        -   def execute(candidate: Any) -> CrudDecision[T]

    Super Class:
        AuthorizationLoader
    """
    
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> CrudDecision[T]:
        """
        Validates and type checks the candidate and its contents for the CrudPermitter.
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           CrudDecision[T]
        Raises:
            CrudAuthorizationLoader
        """
        pass