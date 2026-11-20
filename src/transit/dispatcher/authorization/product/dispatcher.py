# src/transit/dispatcher/authorization/computation/dispatcher.py

"""
Module: transit.dispatcher.authorization.computation.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, TypeVar, cast

from artifcat import ComputationDecision
from authorization import ComputationPermitter
from exchange import ComputationPermissionRequest
from transit import PermissionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="ComputationPermissionRequest")

class ComputationPermissionDispatcher(PermissionDispatcher[T]):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a ComputationPermitter then send the results back
            to clients.

    Attributes:
        permitter: ComputationPermitter[T]

    Provides:
        -   def  execute(candidate: Any) -> ComputationDecision

    Super Class:
        PermissionDispatcher
    """
    
    def __init__(self, permitter: ComputationPermitter[T]):
        """
        Args:
             permitter: ComputationPermitter[T]
        """
        super().__init__(permitter=permitter)
        
    @property
    def permitter(self) -> ComputationPermitter:
        return cast(ComputationPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ComputationDecision:
        """
        Make a decision about a ComputationRequest.

        Args:
            candidate: Any
        Returns:
            ComputationDecision
        Raises:
            ComputationPermissionDispatcherException
        """
        pass