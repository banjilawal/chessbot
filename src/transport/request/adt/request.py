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
    
    def __init__(self, id: int, sender_address: AddressTag, command: Command):
        """
        Args:
            id: int
            command: Command
            sender_address: AddressTag
        """
        super().__init__(id=id, sender_address=sender_address)
        self._command = command
    
    @property
    def command(self) -> Command:
        return self._command
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, ServiceRequest):
            return super().__eq__(other)
        return False
        