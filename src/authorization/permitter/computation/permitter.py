# src/authorization/permitter/computation/permitter.py

"""
Module: authorization.permitter.computation.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ComputationDecision
from authorization import Permitter
from bootstrap import ComputationAuthorizationLoader
from exchange import ComputationPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="ComputationPermissionRequest")

class ComputationPermitter(Permitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a ComputationPermissionRequest.

    Attributes:
        loader: ComputationAuthorizationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> ComputationDecision

    Super Class:
        Permitter
    """

    def __init__(self, loader: ComputationAuthorizationLoader[T]):
        """
        Args:
            loader: ComputationAuthorizationLoader[T]
        """
        super().__init__(loader=loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ComputationDecision:
        """
        Grant permission for a COMPUTATION activity.
        Args:
            candidate: Any
        Returns:
           ComputationDecision
        Raises:
            ComputationPermitterException
        """
        