# src/operation/registry/worker/search/domain.operation.py

"""
Module: operation.registry.worker.search.domain.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Dict, List

from result import SearchResult
from model import WorkerRegistry
from util import LoggingLevelRouter
from operation import Operation, WorkerRegistryOperation


class WorkerRegistryDomainSearch(WorkerRegistryOperation):
    NAME = "worker_registry_domain_search"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            domain: str,
            registry: WorkerRegistry,
    ) -> SearchResult[Dict[str, Operation]]:
        method = f"{cls.__name__}.execute"
        
        if domain.upper() not in registry.domains:
            return SearchResult.empty()
        workers = registry.entries[domain.upper()]
        return SearchResult.success(workers)