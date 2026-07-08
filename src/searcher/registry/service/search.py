# src/searcher/registry/service/name/searcher.py

"""
Module: searcher.registry.service.name.search
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from err import ServiceRegistrySearchException
from result import SearchResult
from model import ServiceRegistry
from util import LoggingLevelRouter
from controller import ServiceRegistryController
from operation import Operation, RegistryEntryNameValidator




class ServiceRegistrySearch(Operation):
    """
    Role
        -   Search Service

    Responsibilities:
        1.  Search the ServiceRegistry for an operation.

    Attributes:

    Provides:
        -   def execute(
                    domain: str,
                    operation_name: str,
                    registry: ServiceRegistry,
            ) -> SearchResult[List[Operation]]:

    Super Class:
        ServiceRegistryOperation
    """
    NAME = "service_registry_name_search"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            service_name: str,
            registry: ServiceRegistry,
            key_name_validator: RegistryEntryNameValidator | None = None,
    ) -> SearchResult[List[Microservice]]:
        """
        Search the ServiceRegistry for an operation.
        
        Action:
            1.  Send an exception chain in the SearchResult if the name is not a valid String.
            2.  Otherwise, search the ServiceRegistry and send any hits in the success  result.
        Args:
            service_name: str
            registry: ServiceRegistry
            key_name_validator: RegistryEntryNameValidator
        Returns:
            SearchResult[List[Microservice]]
        Raises:
            ServiceRegistrySearchException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if key_name_validator is None:
            key_name_validator = RegistryEntryNameValidator()
        
        # Handle the case that, one of keys is not a valid String.
        search_key_validation_result = key_name_validator.validate(candidates=[service_name],)
        if search_key_validation_result.is_failure:
            # Send the exception chain on failure.
            SearchResult.failure(
                ServiceRegistrySearchException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ServiceRegistrySearchException.MSG,
                    err_code=ServiceRegistrySearchException.ERR_CODE,
                    ex=search_key_validation_result.exception,
                )
            )
        # Send and empty result if the operation does not exist in the domain.
        if service_name.upper() not in registry.entries.keys():
            return SearchResult.empty()
        
        # --- Otherwise, return the hits in the work product. ---#
        microservice = registry.entries[service_name]
        return SearchResult.success([microservice])

# --- FINALLY: REGISTER THE OPERATION ---#
ServiceRegistryController.register_service(service=ServiceRegistrySearch)