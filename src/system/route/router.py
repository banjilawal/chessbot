# src/logic/system/route/router.py

"""
Module: logic.system.route.router
Author: Banji Lawal
Created: 2026-03-30
Version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from system import LoggingLevelRouter

T = TypeVar("T")

class Router(ABC, Generic[T]):
    """
    Role
        -   Transaction Worker
        -   Routing

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.

    Attributes:

    Provides:
        -   route(*args, **kwargs) -> Any

    super Class:
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def route(self, *args, **kwargs) -> Any:
        pass