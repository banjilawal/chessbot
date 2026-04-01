# src/command/service/adt/args/root.py

"""
Module: command.service.adt.args.root
Author: Banji Lawal
Created: 2026-02-24
Version: 1.0.0
"""

from __future__ import annotations

from typing import Any, Dict, List, Union, cast


class CommandArgs:
    _args: Dict[str, Any]
    
    def __init__(self):
        self._args = {}
    
    @property
    def entries(self) -> Dict[str, Any]:
        return self._args
        
    @property
    def identifiers(self) -> List[str]:
        return cast(List, self._args.keys())
    
    @property
    def types(self) -> Union:
        return cast(Union, self._args.values())
        
    @property
    def count(self) -> int:
        return len(self._args)
    
    @property
    def has_no_params(self) -> bool:
        return len(self._args) == 0
