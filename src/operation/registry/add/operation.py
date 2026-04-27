# src/operation/registry/invoke.operation.py

"""
Module: operation.registry.invoke.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from err import ChessException
from result import InsertionResult, ValidationResult
from model import WorkerRegistry
from system import LoggingLevelRouter
from operation import Operation, RegistryWorkerSearch, WorkerRegistryOperation



class RegisterWorker(WorkerRegistryOperation):
    OPERATION_NAME = "registry_add"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            worker: Operation,
            registry: WorkerRegistry,
            worker_search: RegistryWorkerSearch | None = None,
    ) -> InsertionResult:
        method = f"{cls.__name__}.execute"
        
        if worker_search is None:
            worker_search = RegistryWorkerSearch()
        
        worker_search_result = worker_search.execute(
            domain=worker.DOMAIN,
            operation_name=worker.OPERATION_NAME,
            registry=registry
        )
        # Handle the case that, the search is not completed.
        if worker_search_result.is_failure:
            return InsertionResult.failure(worker_search_result.exception)
        if worker_search_result.is_success:
            result = cls._collision_helper(registry)
            if result.is_failure:
                return InsertionResult.failure(result.exception)
            return result
            
        registry.entries[worker.DOMAIN][worker.OPERATION_NAME] = worker
        registry.registration_counters[worker.DOMAIN][worker.OPERATION_NAME] += 1
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _collision_helper(
            cls,
            colliding_key: str,
            registry: WorkerRegistry,
            worker: Operation,
    ) -> InsertionResult:
        method = f"{cls.__name__}._collision_helper"
        
        candidate = registry.entries[worker.DOMAIN][colliding_key]
        
        if candidate.OPERATION_NAME.upper() != worker.OPERATION_NAME.upper():
            return InsertionResult.failure(
                ChessException()
            )
        registry.registration_counters[worker.DOMAIN][worker.OPERATION_NAME] += 1
        return InsertionResult.success()
        