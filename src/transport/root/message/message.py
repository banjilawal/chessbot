# src/transport/root/message/message.py

"""
Module: transport.root.message.message
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.0
"""

from __future__ import annotations

from transport import Label


class Message:
    _label: Label
    
    def __init__(self, label: Label):
        self._label = label
        
    @property
    def label(self) -> Label:
        return self._label
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Message):
            return other.label == self._label
        return False