# src/bootstrap/authorization/vectorloader.py

"""
Module: bootstrap.authorization.vector.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ComputationDecision
from bootstrap import ComputationAuthorizationLoader
from request import VectorComputationPermissionRequest

from util import LoggingLevelRouter

T = TypeVar("T", bound="VectorComputationPermissionRequest")

class VectorComputationAuthorizationLoader(
    ComputationAuthorizationLoader[T], ABC, Generic[T]
):
    """
    Role:
        -   Process Bootstrapper

    Responsibilities:
        1.  Ensure the correct Request type is loaded into a ComputationAuthorization module.

    Attributes:

    Provides:
        -   def execute(candidate: Any) -> ComputationDecision

    Super Class:
        ComputationAuthorizationLoader
    """
    
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ComputationDecision:
        """
        Validates and type checks the candidate and its contents for the ComputationPermitter.
        
        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   the wrong type.
            2.  Otherwise, send an approval.
        Args:
            candidate: Any
        Returns:
           ComputationDecision
        Raises:
            ComputationAuthorizationLoader
        """
        pass