# src/searcher/registry/worker/exchange/searcher.py

"""
Module: searcher.registry.worker.exchange.search
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List

from transit.controller import WorkerRegistryController
from err import WorkerRegistryExchangeSearchException
from artifcat import SearchResult
from exchange.model import WorkerRegistry
from util import LoggingLevelRouter
from operation import Operator, RegistryEntryNameValidator


class WorkerRegistryExchangeSearch(Dict[str, Operator]):
    """
    Role
        - Search Worker

    Responsibilities:
        1.   Search the WorkerRegistry for items in a exchange.

    Attributes:

    Provides:
        -   def execute(
                    exchange: str,
                    registry: WorkerRegistry,
                    key_name_validator: RegistryEntryNameValidator,
            ) -> SearchResult[List[Dict[str, Operation]]]:

    Super Class:
        WorkerRegistryOperation
    """
    NAME = "worker_registry_exchange_search"
    
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
            2.  Otherwise, search the WorkerRegistry for the exchange.
                    - If the exchange does not exist, send an empty SearchResult.
                    - Else, send the exchange's items in a SearchResult.
        Args:
            name: str
            registry: WorkerRegistry   
            key_name_validator: RegistryEntryNameValidator         
        Returns:
            SearchResult[List[Operation]]
        Raises:
            WorkerRegistryExchangeSearchException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if key_name_validator is None:
            key_name_validator = RegistryEntryNameValidator()
        
        # Handle the case that exchange is not a valid String.
        search_key_validation_result = key_name_validator.execute(candidates=[name], )
        if search_key_validation_result.is_failure:
            # Send the exception chain on failure.
            SearchResult.failure(
                WorkerRegistryExchangeSearchException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=WorkerRegistryExchangeSearchException.MSG,
                    err_code=WorkerRegistryExchangeSearchException.ERR_CODE,
                    ex=search_key_validation_result.exception,
                )
            )
        # Send and empty result if the exchange does not exist.
        if name.upper() not in registry.exchanges:
            return SearchResult.empty()
        
        # --- Otherwise, return the exchange's items in the work product. ---#
        workers = registry.entries[name.upper()]
        return SearchResult.success([workers])

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=WorkerRegistryExchangeSearch)