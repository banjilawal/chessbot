# src/transport/request/model/request.py

"""
Module: transport.request.model.request
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.0
"""

from __future__ import annotations

from command import Command
from transport import AddressTag, Message


class ServiceRequest(Message):
    _command: Command
    
    def __init__(self, id: int, source_: AddressTag, command: Command):
        """
        Args:
            id: int
            label: AddressTag
            command: Command
        """
        super().__init__(id=id, label=label)
        self._command = command
        
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def label(self) -> AddressTag:
        return self._label
    
    @property
    def command(self) -> Command:
        return self._command
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, ServiceRequest):
            return self._id == other._id
        return False
        