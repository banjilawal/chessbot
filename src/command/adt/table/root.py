# src/command/adt/table/root.py

"""
Module: command.adt.table.root
Author: Banji Lawal
Created: 2026-02-24
Version: 1.0.0
"""

from __future__ import annotations
from typing import Dict, List, cast

from command.adt import Command, CommandArgs


class CommandTable:
    _hash: Dict[Command: CommandArgs]
    
    def __init__(self):
        self._hash = {}
    
    @property
    def size(self) -> int:
        return len(self._hash)
    
    @property
    def is_empty(self) -> bool:
        return len(self._hash) == 0
    
    @property
    def hash(self) -> Dict[Command: CommandArgs]:
        return self._hash
    
    @property
    def command_types(self) -> List[Command]:
        return cast(List[Command], self._hash.keys())
