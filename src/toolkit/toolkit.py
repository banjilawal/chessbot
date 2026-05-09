# src/toolkit/toolkit.py

"""
Module: toolkit.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, List, TypeVar

from controller import WorkerRegistryController
from err import ToolkitException
from err.search.empty.operation import OperationNotFoundException
from microservice import Microservice
from operation import Operation
from result import SearchResult

T = TypeVar("T")



class Toolkit(ABC, Generic[T]):
    """
    Role:
        -   Utility Container
        
    Responsibilities:
        1.  Collection of workers and services that are required for a task.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:

    Provides:

    Super Class:
    """
    REQUIRED_OPERATIONS: List[Operation] = []
    REQUIRED_SERVICES: List[Microservice] = []
    
    def __init__(self, worker_controller: WorkerRegistryController):
        self._worker_controller = worker_controller
    
    def _resolve_operations(self) -> SearchResult[List[Dict[str, Operation]]]:
        """
        Dynamically resolve required operations based on REQUIRED_OPERATIONS.
        """
        method = f"{self.__class__.__name__}._resolve_operations"
        resolved = {}
        for operation in self.REQUIRED_OPERATIONS:
            domain = operation.DOMAIN
            operation_name = operation.OPERATION_NAME
            
            search_result = self._worker_controller.find_worker(
                domain=domain,
                operation_name=operation_name,
            )
            # Handle the case that, the search failed.
            if search_result.is_failure:
                # Send the exception chain on failure.
                ToolkitException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ToolkitException.MSG,
                    err_code=ToolkitException.ERR_CODE,
                    ex=search_result.exception,
                )
            # Handle the case that, a dependency was not found.
            if search_result.is_empty:
                # Send the exception chain on failure.
                ToolkitException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ToolkitException.MSG,
                    err_code=ToolkitException.ERR_CODE,
                    ex=OperationNotFoundException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=OperationNotFoundException.MSG,
                        err_code=OperationNotFoundException.ERR_CODE,
                        var=operation_name,
                        val=operation
                    )
                )
            # Store resolved operation instance
            if search_result.is_success:
                resolved[operation.__name__] = search_result.payload[0]
        
        return SearchResult.success([resolved])
