# src/toolkit/toolkit.py

"""
Module: toolkit.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Dict, Generic, List, TypeVar

from controller import ServiceRegistryController, WorkerRegistryController
from err import ToolkitException
from microservice import IdentityService, Microservice
from operation import Operation
from result import SearchResult
from util import LoggingLevelRouter
from validation import PrimingValidator

T = TypeVar("T")



class Toolkit(ABC, Generic[T]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider
        
    Responsibilities:
        1.  Aggregates workers and services an entity requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []
        
        identity_service: IdentityService
        priming_validator: PrimingValidator
        
        _entries: Dict[str, Any]
    
    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:
        -   def _resolve_service_dependencies() -> SearchResult[List[Dict[str, Microservice]]]:
        -   def _resolve_dependencies(self) -> SearchResult[List[Dict[str, Operation]]]
        
    Super Class:
    """
    DEPENDENCIES: List[Operation] = []
    SERVICE_DEPENDENCIES: List[Microservice] = []
    
    identity_service: IdentityService = IdentityService()
    priming_validator: PrimingValidator = PrimingValidator()
    
    _entries: Dict[str, Any] = {}
    
    def __init__(
            self,
            worker_controller: WorkerRegistryController | None = None,
            service_controller: ServiceRegistryController | None = None,
    ):
        self._worker_controller = worker_controller
        self._service_controller = service_controller
        
    @LoggingLevelRouter.monitor
    def resolve_dependencies(self) -> SearchResult[List[Dict[str, Any]]]:
        method = f"{self.__class__.__name__}._resolve_dependencies"
        
        services_resolution_result = self._resolve_service_dependencies()
        # Handle the case that, the service dependencies are not resolved.
        if services_resolution_result.is_failure:
            # Send the exception chain on failure.
            ToolkitException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=ToolkitException.MSG,
                err_code=ToolkitException.ERR_CODE,
                ex=services_resolution_result.exception,
            )
        operations_resolution_result = self._resolve_dependencies()
        # Handle the case that, the operation dependencies are not resolved.
        if operations_resolution_result.is_failure:
            # Send the exception chain on failure.
            ToolkitException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=ToolkitException.MSG,
                err_code=ToolkitException.ERR_CODE,
                ex=operations_resolution_result.exception,
            )
        
        for key in services_resolution_result.payload[0].keys():
            self._entries[key] = services_resolution_result.payload[0][key]
            
        for key in operations_resolution_result.payload[0].keys():
            self._entries[key] = operations_resolution_result.payload[0][key]
            
        return SearchResult.success([self._entries])
    
    def _resolve_service_dependencies(self) -> SearchResult[List[Dict[str, Microservice]]]:
        """
        Dynamically resolve required operations based on REQUIRED_OPERATIONS.
        """
        method = f"{self.__class__.__name__}._resolve_service_dependencies"
        resolved = {}
        for dependency in self.SERVICE_DEPENDENCIES:
            search_result = self._service_controller.find_service(service_name=dependency.NAME)
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
                        var=dependency.NAME,
                        val=dependency
                    )
                )
            # Store resolved operation instance
            if search_result.is_success:
                resolved[dependency.__name__] = search_result.payload[0]
        
        return SearchResult.success([resolved])
    
    def _resolve_dependencies(self) -> SearchResult[List[Dict[str, Operation]]]:
        """
        Dynamically resolve required operations based on REQUIRED_OPERATIONS.
        """
        method = f"{self.__class__.__name__}._resolve_operations"
        resolved = {}
        for dependency in self.DEPENDENCIES:
            search_result = self._worker_controller.find_worker(
                domain=dependency.DOMAIN,
                operation_name=dependency.NAME,
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
                        var=dependency.NAME,
                        val=dependency
                    )
                )
            # Store resolved operation instance
            if search_result.is_success:
                resolved[dependency.__name__] = search_result.payload[0]
        
        return SearchResult.success([resolved])
