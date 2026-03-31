# src/logic/system/route/router.py

"""
Module: logic.system.route.router
Author: Banji Lawal
Created: 2026-03-30
Version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, TypeVar

from logic.system import LoggingLevelRouter, Router

T = TypeVar("T")

class TokenOpsRouter(Router[str]):
    """
    Role
        -   Transaction Worker
        -   Routing

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.

    Attributes:

    Provides:
        -   route(op_name: str) -> Result

    super Class:
    """
    MENU = {
        "build": TokenBuilder,
        
    }
    _menu: Dict[str, Any]
    
    def __init__(self,):
        self._menu = {}
        
    @property
    def menu(self) -> Dict[str, Any]:
        return self._menu
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def route(self, op_name: str) -> Result:
        pass