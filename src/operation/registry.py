# src/worker/registry.py

"""
Module: worker.registry
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from operation import Operation


class WorkerRegistry:
    _workers: dict[str, [str, Operation]]
    
    def __init__(self):
        self._workers = {}
        
    @property
    def workers(self) -> dict[str, Operation]:
        return self._workers