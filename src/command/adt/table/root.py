# src/command/adt/table/root.py

"""
Module: command.adt.table.root
Author: Banji Lawal
Created: 2026-02-24
Version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from command.adt import Command, CommandArgs


class CommandTable:
    _table: Dict[Command: CommandArgs]
    
    def __init__(self):
        self._table = {}
    
    @property
    def table(self) -> Dict[Command: CommandArgs]:
        return self._table
    
    @table.setter
    def table(self, value: Dict[Command: CommandArgs]):
        self._table = value
