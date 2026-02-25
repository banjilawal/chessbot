# src/chess/system/service/menu/execution/execution.py

"""
Module: chess.system.service.menu.execution.execution
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Dict


class ServiceExecution:
    """
    A class representing a service execution.
    """
    _name: str
    _params: Dict[str: Any]
    
    def __init__(self, name: str, params: Dict[str, Any]):
        self._name = name
        self._params = params
    
    @property
    def name(self):
        return self._name
    
    @property
    def params(self):
        return self._params