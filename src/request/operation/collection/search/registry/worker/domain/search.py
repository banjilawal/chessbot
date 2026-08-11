# src/searcher/registry/worker/domain/searcher.py

"""
Module: searcher.registry.worker.domain.search
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Dict, List

from controller import WorkerRegistryController
from err import WorkerRegistryDomainSearchException
from result import SearchResult
from model import WorkerRegistry
from util import LoggingLevelRouter
from operation import Operation, RegistryEntryNameValidator


class WorkerRegistryDomainSearch(Dict[str, Operation]):
    """
    Role
        -   Search Worker

    Responsibilities:
        1.  Search the WorkerRegistry for items in a domain.

    Attributes:

    Provides:
        -   def execute(
                    domain: str,
                    registry: WorkerRegistry,
                    key_name_validator: RegistryEntryNameValidator,
            ) -> SearchResult[List[Dict[str, Operation]]]:

    Super Class:
        WorkerRegistryOperation
    """
    NAME = "worker_registry_domain_search"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            name: str,
            registry: WorkerRegistry,
            key_name_validator: RegistryEntryNameValidator | None = None,
    ) -> SearchResult[List[Dict[str, Operation]]]:
        """
        Search the WorkerRegistry for an operation.

        Action:
            1.  Send an exception chain in the SearchResult if the name is not a valid String.
            2.  Otherwise, search the WorkerRegistry for the domain.
                    -   If the domain does not exist, send an empty SearchResult.
                    -   Else, send the domain's items in a SearchResult.
        Args:
            name: str
            registry: WorkerRegistry   
            key_name_validator: RegistryEntryNameValidator         
        Returns:
            SearchResult[List[Operation]]
        Raises:
            WorkerRegistryDomainSearchException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if key_name_validator is None:
            key_name_validator = RegistryEntryNameValidator()
        
        # Handle the case that, domain is not a valid String.
        search_key_validation_result = key_name_validator.execute(candidates=[name], )
        if search_key_validation_result.is_failure:
            # Send the exception chain on failure.
            SearchResult.failure(
                WorkerRegistryDomainSearchException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=WorkerRegistryDomainSearchException.MSG,
                    err_code=WorkerRegistryDomainSearchException.ERR_CODE,
                    ex=search_key_validation_result.exception,
                )
            )
        # Send and empty result if the domain does not exist.
        if name.upper() not in registry.domains:
            return SearchResult.empty()
        
        # --- Otherwise, return the domain's items in the work product. ---#
        workers = registry.entries[name.upper()]
        return SearchResult.success([workers])

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=WorkerRegistryDomainSearch)