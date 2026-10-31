# src/bootstrap/authorization/insertion/push/loader.py

"""
Module: bootstrap.authorization.insertion.push.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat.decision import Decision
from bootstrap import InsertionAuthorizationLoader
from exchange import PushPermissionRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="PushPermissionRequest")

class PushAuthorizationLoader(
    InsertionAuthorizationLoader[T], ABC, Generic[T]
):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a PushAuthorizer
        
    Attributes:

    Provides:
        -   def execute(candidate: Any) -> PushDecision[T]

    Super Class:
        InsertionAuthorizationLoader
    """
    
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> PushDecision[T]:
        """
        Checks if the PushRequest is the right type and not null.
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           PushDecision[T]
        Raises:
            PushAuthorizationLoaderException
        """
        pass