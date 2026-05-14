# src/operation/registry/worker/search/name.operation.py

"""
Module: operation.registry.worker.search.name.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from err import OperationNotFoundSearchException, WorkerRegistryDomainSearchException, WorkerRegistryNameSearchException
from result import SearchResult
from model import WorkerRegistry
from util import LoggingLevelRouter
from operation import Operation, WorkerRegistryOperation



class WorkerRegistryNameSearch(WorkerRegistryOperation):
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
            1.  Send an exception in the SearchResult if any of the following occur:
                    -   The domain does not exist in the registry.
                    -   The operation_name is not found in the domain.
            2.  Otherwise, send the success result.
        Returns:
            SearchResult[List[Operation]]
        Raises:
            WorkerRegistryDomainSearchException
            WorkerRegistryNameSearchException
            OperationNotFoundSearchException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the domain does not exist in the registry.
        if domain.upper() not in registry.domains:
            # Send the exception chain on failure.
            return SearchResult.failure(
                WorkerRegistryDomainSearchException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=WorkerRegistryDomainSearchException.MSG,
                    err_code=WorkerRegistryDomainSearchException.ERR_CODE,
                    var="operation_domain",
                    val=domain,
                )
            )
        # Handle the case that, none of the operations in the domain has the name.
        if operation_name.upper() not in registry.entries[domain].keys():
            # Send the exception chain on failure.
            return SearchResult.failure(
                WorkerRegistryNameSearchException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=WorkerRegistryNameSearchException.MSG,
                    err_code=WorkerRegistryNameSearchException.ERR_CODE,
                    ex=OperationNotFoundSearchException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=OperationNotFoundSearchException.MSG,
                        err_code=OperationNotFoundSearchException.ERR_CODE,
                        var="operation_name",
                        val=operation_name,
                    )
                )
            )
        # --- Return the work product. ---#
        operation = registry.entries[domain][operation_name]
        return SearchResult.success(List[operation])