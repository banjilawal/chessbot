# src/model/state/registry/worker.model.py

"""
Module: model.state.registry.worker.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Dict, List

from operation import Operation


class WorkerRegistry:
    """
    Role
        -   Controller
        -   Publisher
    
    Responsibilities:
        1.  Dynamic, entry and removal of public operations available for building toolkits.
        2.  Uses namespaces to improve search and minimize hash collisions.
    
    Attributes:
        invocation_counters: dict[str, int]
        registration_counters: dict[str, int]
        items: Dict[str, Dict[str, Operation]]
    
    Provides:
        -   def domains(self) -> List[str]:
    
    Super Class:
        Model
    """
    _invocation_counters: dict[str, int]
    _registration_counters: dict[str, int]
    _entries: Dict[str, Dict[str, Operation]]
    
    def __init__(self):
        self._entries = {str: {}}
        self._invocation_counters = {}
        self._registration_counters = {}
    
    @property
    def domains(self) -> List[str]:
        return list(self._entries.keys())
        
    @property
    def entries(self) -> Dict[str, Dict[str, Operation]]:
        return self._entries
    
    @property
    def invocation_counters(self) -> dict[str, int]:
        return self._invocation_counters
    
    @property
    def registration_counters(self) -> dict[str, int]:
        return self._registration_counters
    
