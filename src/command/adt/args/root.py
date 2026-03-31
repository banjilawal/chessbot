# src/command/adt/args/root.py

"""
Module: command.adt.args.root
Author: Banji Lawal
Created: 2026-02-24
Version: 1.0.0
"""

from __future__ import annotations


from typing import Any, Dict


class CommandArgs:
    _args: Dict[str, Any]
    
    def __init__(self, args: Dict[str, Any]):
        self._args = args
    
    @property
    def args(self) -> Dict[str, Any]:
        return self._args
