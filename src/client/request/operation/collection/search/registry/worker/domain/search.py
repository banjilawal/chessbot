# src/searcher/registry/worker/client/searcher.py

"""
Module: searcher.registry.worker.client.search
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List

from transit.controller import WorkerRegistryController
from err import WorkerRegistryClientSearchException
from artifcat import SearchResult
from client.model import WorkerRegistry
from util import LoggingLevelRouter
from operation import Operator, RegistryEntryNameValidator


class WorkerRegistryClientSearch(Dict[str, Operator]):
    """
    Role
        - Search Worker

    Responsibilities:
        1.   Search the WorkerRegistry for items in a client.

    Attributes:

    Provides:
        -   def execute(
                    client: str,
                    registry: WorkerRegistry,
                    key_name_validator: RegistryEntryNameValidator,
            ) -> SearchResult[List[Dict[str, Operation]]]:

    Super Class:
        WorkerRegistryOperation
    """
    NAME = "worker_registry_client_search"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            name: str,
            registry: WorkerRegistry,
            key_name_validator: RegistryEntryNameValidator | None = None,
    ) -> SearchResult[List[Dict[str, Operator]]]:
        """
        Search the WorkerRegistry for an operation.

        Action:
            1.   Send an exception chain in the SearchResult if the name is not a valid String.
            2.  Otherwise, search the WorkerRegistry for the client.
                    - If the client does not exist, send an empty SearchResult.
                    - Else, send the client's items in a SearchResult.
        Args:
            name: str
            registry: WorkerRegistry   
            key_name_validator: RegistryEntryNameValidator         
        Returns:
            SearchResult[List[Operation]]
        Raises:
            WorkerRegistryClientSearchException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if key_name_validator is None:
            key_name_validator = RegistryEntryNameValidator()
        
        # Handle the case that client is not a valid String.
        search_key_validation_result = key_name_validator.execute(candidates=[name], )
        if search_key_validation_result.is_failure:
            # Send the exception chain on failure.
            SearchResult.failure(
                WorkerRegistryClientSearchException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=WorkerRegistryClientSearchException.MSG,
                    err_code=WorkerRegistryClientSearchException.ERR_CODE,
                    ex=search_key_validation_result.exception,
                )
            )
        # Send and empty result if the client does not exist.
        if name.upper() not in registry.clients:
            return SearchResult.empty()
        
        # --- Otherwise, return the client's items in the work product. ---#
        workers = registry.entries[name.upper()]
        return SearchResult.success([workers])

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=WorkerRegistryClientSearch)