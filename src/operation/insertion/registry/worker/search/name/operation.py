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
from controller import WorkerRegistryController
from operation import Operation, WorkerRegistryOperation
from err import OperationNotFoundSearchException, WorkerRegistryDomainSearchException, WorkerRegistryNameSearchException




class WorkerRegistryNameSearch(WorkerRegistryOperation):
    """
    Role
        -   Search Worker

    Responsibilities:
        1.  Search the WorkerRegistry for an operation.

    Attributes:

    Provides:
        -   def execute(
                    domain: str,
                    operation_name: str,
                    registry: WorkerRegistry,
            ) -> SearchResult[List[Operation]]:

    Super Class:
        WorkerRegistryOperation
    """
    NAME = "worker_registry_name_search"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            domain: str,
            operation_name: str,
            registry: WorkerRegistry,
    ) -> SearchResult[List[Operation]]:
        """
        Search the WorkerRegistry for an operation.
        
        Action:
            1.  Return an empty SearchResult if either:
                    -   The domain does not exist.
                    -   The name does not exist in the domain.
            2.  Otherwise, send the hits in the payload.
        Returns:
            SearchResult[List[Operation]]
        Raises:
        """
        
        # Handle the case that, the domain does not exist in the registry.
        if domain.upper() not in registry.domains:
            # Send the exception chain on failure.
            return SearchResult.empty()
        # Handle the case that, none of the operations in the domain has the name.
        if operation_name.upper() not in registry.entries[domain].keys():
            return SearchResult.empty()
        
        # --- Return the work product. ---#
        operation = registry.entries[domain][operation_name]
        return SearchResult.success(List[operation])


# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register(worker=WorkerRegistryNameSearch)