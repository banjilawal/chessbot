# src/authorization/chain/request/checker.py

"""
Module: authorization.chain.request.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from authorization import Chainable
from exchange import PermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class Checker(Chainable, ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        pass