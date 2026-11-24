# src/bootstrap/authorization/insertion/add/loader.py

"""
Module: bootstrap.authorization.insertion.add.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import AddNodeDecision
from bootstrap import InsertionAuthorizationLoader
from request import AddNodePermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="AddNodePermissionRequest")

class AddNodeAuthorizationLoader(
    InsertionAuthorizationLoader[T], ABC, Generic[T]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a AddAuthorizer
        
    Attributes:

    Provides:
        -   def execute(candidate: Any) -> AddDecision

    Super Class:
        InsertionAuthorizationLoader
    """
    
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AddNodeDecision:
        """
        Checks if the AddRequest is the right type and not null.
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           AddDecision
        Raises:
            AddAuthorizationLoaderException
        """
        pass