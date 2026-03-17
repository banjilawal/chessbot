# src/command/request/request.py

"""
Module: command.request.request
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Dict


class Request:
    """
    Role:Messaging. Service Request, Command Build Params.

    Responsibilities:
    1.  Client send a request for one of a service's operations. supported by
        a Command.
    2.  Parameter for CommandBuilders.

    Super Class:
    None

    Provides:

    # LOCAL ATTRIBUTES:
        *   command_name (str)
        *   arguments (Dict[str, Any])

    # INHERITED ATTRIBUTES:
    None

    Attributes:
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
    def command_name(self) -> str:
        return self._command_name
    
    @property
    def arguments(self) -> Dict[str, Any]:
        return self._arguments
