# src/bootstrap/authorization/crud/search/loader.py

"""
Module: bootstrap.authorization.crud.search.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import SearchDecision
from bootstrap import CrudAuthorizationLoader
from exchange import SearchPermissionRequest

from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchPermissionRequest")

class SearchAuthorizationLoader(
    CrudAuthorizationLoader[T], ABC, Generic[T]
):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a CrudAuthorization module.
        
    Attributes:

    Provides:
        -   def execute(candidate: Any) -> SearchDecision

    Super Class:
        CrudAuthorizationLoader
    """
    
    def __init__(self):
        super().__init__()

    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> SearchDecision:
        """
        Checks if the Request is the right type.
        
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
            SearchAuthorizationLoaderException
        """
        pass