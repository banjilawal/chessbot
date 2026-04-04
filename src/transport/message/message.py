# src/transport/system/adt/message/message.py

"""
Module: transport.system.adt.message.message
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.0
"""

from __future__ import annotations

from transport import AddressTag


class Message:
    _id: int
    _sender_address: AddressTag
    
    def __init__(self, id: int, sender_address: AddressTag):
        self._id = id
        self._sender_address = sender_address
        
    @property
    def id(self) -> int:
        return self._id
        
    @property
    def sender_address(self) -> AddressTag:
        return self._sender_address
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Message):
            return (
                    other.id == self._id and
                    other.sender_address == self._sender_address
            )
        return False