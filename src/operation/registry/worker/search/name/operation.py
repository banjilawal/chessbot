# src/operation/registry/worker/search/name.operation.py

"""
Module: operation.registry.worker.search.name.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from result import SearchResult
from model import WorkerRegistry
from util import LoggingLevelRouter
from operation import Operation, WorkerRegistryOperation



class WorkerRegistryNameSearch(WorkerRegistryOperation):
    NAME = "registry_worker_search"
    
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
        return SearchResult.success(List[operation])