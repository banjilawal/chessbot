# src/chess/system/service/request/request.py

"""
Module: chess.system.service.request.request
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, Dict


class ServiceRequest:
    """
    A class representing a service request.
    """
    _command: str
    _arguments: Dict[str: Any]
    
    def __init__(self, command: str, arguments: Dict[str, Any]):
        self._command = command
        self._arguments = arguments
    
    @property
    def command(self):
        return self._command
    
    @property
    def arguments(self):
        return self._arguments
