# src/operation/registry.py

"""
Module: operation.registry
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from operation import Operation


class WorkerRegistry:
    _invocation_counters: dict[str, int]
    _registration_counters: dict[str, int]
    _workers: Dict[str, Dict[str, Operation]]
    
    def __init__(self):
        self._workers = {str: {}}
        self._invocation_counters = {}
        self._registration_counters = {}
        
    @property
    def workers(self) -> Dict[str, Dict[str, Operation]]:
        return self._workers
    
    @property
    def invocation_counters(self) -> dict[str, int]:
        return self._invocation_counters
    
    @property
    def registration_counters(self) -> dict[str, int]:
        return self._registration_counters