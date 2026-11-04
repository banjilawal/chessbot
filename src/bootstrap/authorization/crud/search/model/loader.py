# src/bootstrap/authorization/search/model/loader.py

"""
Module: bootstrap.authorization.search.model.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import SearchDecision
from bootstrap import SearchAuthorizationLoader
from exchange import SearchPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchPermissionRequest")

class ModelSearchAuthorizationLoader(
    SearchAuthorizationLoader[T], ABC, Generic[T]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ModelAuthorizer
        
    Attributes:

    Provides:
        -   def execute(candidate: Any) -> SearchDecision

    Super Class:
        SearchAuthorizationLoader
    """
    
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> SearchDecision:
        """
        Checks if the SearchRequest is the right type and not null.
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           SearchDecision
        Raises:
            ModelSearchAuthorizationLoaderException
        """
        pass