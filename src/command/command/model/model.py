# src/command/command/model/command.py

"""
Module: command.command.model/.command
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, TypeVar

from logic.system import Service

T = TypeVar("T")

class Command(ABC, Generic[T]):
    """
    Role
        -   Data-Holder
        -   Messaging

    Naming Conventions:
        -   <Operation>Command.

    Responsibilities:
        1.  Issue its server instructions on how the client wants the operation to be executed.

    Attributes:
        id: int
        name: str - Name of the server's operation.
        server: Service - Operation provider
        parameters: Dict[str, Any] - Parameters for the operation's methods.

    Provides:
        -   execute(candidate: Any, *args, **kwargs) -> ValidationResult[T]

    super Class:
    """
    _id: int
    _name: str
    _server: Service
    _parameters: Dict[str: Any]
    
    def __init__(
            self,
            id: int,
            name: str,
            server: Service,
            parameters: Dict[str, Any],
    ):
        """
        Args:
            id: int
            name: str
            service: Service
            parameters: Dict[str, Any]
        """
        self._id = id
        self._name = name
        self._server = server
        self._parameters = parameters
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def server(self) -> Service:
        return self._server
    
    @property
    def parameters(self) -> Dict[str, Any]:
        return self._parameters
    
    def __eq__(self, other: Any) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Command):
            return other.id == self._id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    @classmethod
    @abstractmethod
    def cipher(cls,) -> T:
        pass