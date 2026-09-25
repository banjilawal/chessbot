# src/searcher/registry/worker/name/searcher.py

"""
Module: searcher.registry.worker.name.search
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List

from err import WorkerRegistryNameSearchException
from artifcat import SearchResult
from client.exchange.model import WorkerRegistry
from util import LoggingLevelRouter
from transit.controller import WorkerRegistryController
from operation import Operator, RegistryEntryNameValidator




class WorkerRegistryNameSearch(Operator):
    """
    Role
        - Search Worker

    Responsibilities:
        1.  Search the WorkerRegistry for an operation.

    Attributes:

    Provides:
        -   def execute(
                    client: str,
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
            client: str,
            operation_name: str,
            registry: WorkerRegistry,
            key_name_validator: RegistryEntryNameValidator | None = None,
    ) -> SearchResult[List[Operator]]:
        """
        Search the WorkerRegistry for an operation.
        
        Action:
            1.  Send an exception chain in the SearchResult if either the client
                or the name is not a valid String.
            2.  Otherwise, search the WorkerRegistry for the operation. If either of the following occurs,
                send an empty SearchResult:
                    - The client does not exist.
                    - The operation does not exist in the client.exchange.
                Else, send the operation in a SearchResult.
        Args:
            client: str
            operation_name: str
            registry: WorkerRegistry
            key_name_validator: RegistryEntryNameValidator
        Returns:
            SearchResult[List[Operation]]
        Raises:
            WorkerRegistryNameSearchException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if key_name_validator is None:
            key_name_validator = RegistryEntryNameValidator()
        
        # Handle the case that one of keys is not a valid String.
        search_key_validation_result = key_name_validator.execute(
            candidates=[client, operation_name],
        )
        if search_key_validation_result.is_failure:
            # Send the exception chain on failure.
            SearchResult.failure(
                WorkerRegistryNameSearchException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=WorkerRegistryNameSearchException.MSG,
                    err_code=WorkerRegistryNameSearchException.ERR_CODE,
                    ex=search_key_validation_result.exception,
                )
            )
        # Send and empty result if the client does not exist.
        if client.exchange.upper() not in registry.clients:
            return SearchResult.empty()
        # Send and empty result if the operation does not exist in the client.exchange.
        if operation_name.upper() not in registry.entries[client].keys():
            return SearchResult.empty()
        
        # --- Otherwise, return the hits in the work product. ---#
        operation = registry.entries[client][operation_name]
        return SearchResult.success([operation])

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=WorkerRegistryNameSearch)