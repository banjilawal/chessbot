# src/operation/registry/search/worker/operation.py

"""
Module: operation.registry.search.worker.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from result import SearchResult
from model import WorkerRegistry
from system import LoggingLevelRouter
from operation import Operation, WorkerRegistryOperation



class RegistryWorkerSearch(WorkerRegistryOperation):
    OPERATION_NAME = "registry_worker_search"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            domain: str,
            operation_name: str,
            registry: WorkerRegistry,
    ) -> SearchResult[List[Operation]]:
        method = f"{cls.__name__}.execute"
        
        if domain.upper() not in registry.domains:
            return SearchResult.empty()
        if operation_name.upper() not in registry.entries[domain].keys():
            return SearchResult.empty()
        operation = registry.entries[domain][operation_name]
        return SearchResult.success(list[operation]([]))