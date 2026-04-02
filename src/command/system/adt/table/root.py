# src/command/service/adt/table/root.py

"""
Module: command.service.adt.table.root
Author: Banji Lawal
Created: 2026-02-24
Version: 1.0.0
"""

from __future__ import annotations
from typing import Dict, List, Union, cast

from command.system.adt import Command, CommandArgs


class CommandTable:
    _entries: Dict[Command: CommandArgs]
    
    def __init__(self):
        self._entries = {}
    
    @property
    def size(self) -> int:
        return len(self._entries)
    
    @property
    def is_empty(self) -> bool:
        return len(self._entries) == 0
    
    @property
    def entries(self) -> Dict[Command: CommandArgs]:
        return self._entries
    
    @property
    def command_types(self) -> Union:
        return cast(Union, self._entries.keys())
    
    @property
    def command_names(self) -> List[str]:
        names = []
        for key in self._entries:
            names.append(key.designation)
        return names
