# src/command/adt/args/root.py

"""
Module: command.adt.args.root
Author: Banji Lawal
Created: 2026-02-24
Version: 1.0.0
"""

from __future__ import annotations

from collections.abc import dict_keys
from typing import Any, Dict, List, cast


class CommandArgs:
    _args: Dict[str, Any]
    
    def __init__(self):
        self._args = {}
    
    @property
    def args(self) -> Dict[str, Any]:
        return self._args
    
    @args.setter
    def args(self, value: Dict[str, Any]):
        self._args = value
        
    @property
    def variables(self) -> List[str]:
        return cast(List, self._args.keys())
    
    @property
    def types(self) -> List[str]:
        return cast(List, self._args.values())
        
    @property
    def count(self) -> int:
        return len(self._args)
    
    @property
    def has_no_params(self) -> bool:
        return len(self._args) == 0
