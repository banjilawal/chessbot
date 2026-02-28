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
    # ROLE: Messaging. Service Request, Command Build Params.

    # RESPONSIBILITIES:
    1.  Client send a request for one of a service's operations. supported by
        a Command.
    2.  Parameter for CommandBuilders.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   command_name (str)
        *   arguments (Dict[str, Any])

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        *   command_name (str)
        *   arguments (Dict[str, Any])
    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _command_name: str
    _arguments: Dict[str: Any]
    
    def __init__(self, command_name: str, arguments: Dict[str, Any] = Dict[str, Any]):
        self._command_name = command_name
        self._arguments = arguments
    
    @property
    def command_name(self):
        return self._command_name
    
    @property
    def arguments(self):
        return self._arguments
