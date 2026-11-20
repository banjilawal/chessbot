# src/bootstrap/authorization/computation/distance/loader.py

"""
Module: bootstrap.authorization.computation.distance.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import DistanceDecision
from bootstrap import ComputationAuthorizationLoader
from exchange import DistancePermissionRequest

from util import LoggingLevelRouter

T = TypeVar("T", bound="DistancePermissionRequest")

class DistanceAuthorizationLoader(
    ComputationAuthorizationLoader[T], ABC, Generic[T]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ComputationAuthorization module.
        
    Attributes:

    Provides:
        -   def execute(candidate: Any) -> DistanceDecision

    Super Class:
        ComputationAuthorizationLoader
    """
    
    def __init__(self):
        super().__init__()

    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> DistanceDecision:
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
           DistanceDecision
        Raises:
            DistanceAuthorizationLoaderException
        """
        pass