# src/controller/registry/worker/controller.py

"""
Module: controller.registry.worker/controller
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Dict, List

from controller import Controller
from model import WorkerRegistry
from toolkit import WorkerRegistryToolkit
from util import LoggingLevelRouter, singleton
from result import InsertionResult, SearchResult
from operation import Operation
from err import OperationNullException, WorkerRegistryControllerException


@singleton
class WorkerRegistryController(Controller[WorkerRegistry]):
    """
    Role
        -   Controller
        -   Integrity Maintenance
        -   Consistency Assurance
    
    Responsibilities:
        1.  Ensure WorkerRegistry stays consistent during and after operations.
    
    Attributes:
        registry: WorkerRegistry
        toolkit: WorkerRegistryToolkit
    
    Provides:
        -   def find_worker(domain: str, operation_name: str) -> SearchResult[List[Operation]]:
        -   def domain_workers(domain: str) -> SearchResult[List[dict[str, Operation]]]:
        
        -   def register_worker(
                    worker: Operation,
                    null_exception: OperationNullException,
            ) -> InsertionResult:
    
    Super Class:
        Controller
    """
    _registry: WorkerRegistry
    _toolkit: WorkerRegistryToolkit
    
    def __init__(
            self,
            registry: WorkerRegistry | None = None,
            toolkit: WorkerRegistryToolkit | None = None,
    ):
        self._registry = registry or WorkerRegistry()
        self._toolkit = toolkit or WorkerRegistryToolkit()
    
    @property
    def is_empty(self) -> bool:
        return self.number_of_workers == 0
    
    @property
    def number_of_workers(self) -> int:
        count = 0
        for domain in self._registry.entries.keys():
            count += len(self._registry.entries[domain])
        return count
    
    @property
    def domains(self) -> List[str]:
        return self._registry.domains
    
    @LoggingLevelRouter.monitor
    def register_worker(
            self,
            worker: Operation,
            null_exception: OperationNullException | None = None,
    ) -> InsertionResult:
        """
        Add a new worker to the registry.
        
        Action:
            1.  Send an exception chain in the InsertionResult if any of the following occur.
                    -   worker is flagged unsafe.
                    -   Writing the worker into the registry raises an error.
            2.  Otherwise, add the entry to the registry and return a success result.
        Args:
            worker: Operation
            null_exception: OperationNullException
        Returns:
            InsertionResult
        Raises:
            WorkerRegistryControllerException
        """
        method = f"{self.__class__.__name__}.register_worker"
        
        # --- Supply any missing dependencies. ---#
        if null_exception is None:
            null_exception = OperationNullException()
            
        # Handoff the insertion request to the worker.
        insertion_result = self._toolkit.register_new_worker.execute(
            worker=worker,
            registry=self._registry,
            null_exception=null_exception,
        )
        # Handle the case that, the request is not satisfied.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=insertion_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def find_worker(self, domain: str, operation_name: str,) -> SearchResult[List[Operation]]:
        """
        Find a worker in the registry.

        Action:
            1.  Send an exception chain in the SearchResult if the search is not completed.
            2.  Otherwise, send the success result.
        Args:
            domain: str
            operation_name: str
        Returns:
            SearchResult[List[Operation]]
        Raises:
            WorkerRegistryControllerException
        """
        method = f"{self.__class__.__name__}.find_worker"
        
        # Handoff the search request to the worker.
        search_result = self._toolkit.worker_registry_name_search.execute(
            domain=domain,
            operation_name=operation_name,
            registry=self._registry,
        )
        # Handle the case that, the request is not satisfied.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=search_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return search_result
    
    @LoggingLevelRouter.monitor
    def domain_workers(self, domain: str,) -> SearchResult[List[Dict[str, Operation]]]:
        """
        Find the workers in a domain.

        Action:
            1.  Send an exception chain in the SearchResult if the search is not completed.
            2.  Otherwise, send the success result
        Args:
            domain: str
        Returns:
            SearchResult[List[dict[str, Operation]]]
        Raises:
            WorkerRegistryControllerException
        """
        method = f"{self.__class__.__name__}.find_domain_workers"
        
        # Handoff the search request to the worker.
        search_result = self._toolkit.worker_registry_domain_search.execute(
            domain=domain,
            registry=self._registry,
        )
        # Handle the case that, the request is not satisfied.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=search_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return search_result
        