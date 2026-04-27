# src/controller/registry/controller.py

"""
Module: controller.registry.controller
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List


from controller import Controller
from model import WorkerRegistry
from system import LoggingLevelRouter
from result import InsertionResult, SearchResult
from operation import Operation, WorkerRegistryToolkit
from err import OperationNullException, WorkerRegistryControllerException

class WorkerRegistryController(Controller[WorkerRegistry]):
    """
    Role
        -   Controller
        -   Publisher

    Responsibilities:
        1.  Dynamic registry of operations available for toolkits.

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
    def  domains(self) -> List[str]:
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
        
        if null_exception is None:
            null_exception = OperationNullException()
            
        # Handle the case that, the worker fails a safety check.
        worker_validation_result = self._toolkit.add_worker_bootstrapper.execute(
            worker=worker,
            null_exception=null_exception,
            name_validator=self._toolkit.name_validator,
            validation_bootstrapper=self._toolkit.validation_bootstrapper,
        )
        if worker_validation_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=worker_validation_result.exception
                )
            )
        # --- After The worker is validated, run the registration steps. ---#
        insertion_result = self._toolkit.register_worker.execute(
            worker=worker,
            registry=self._registry,
        )
        # Handle the case that, the worker does not get registered.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=worker_validation_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def find_worker(self, domain: str, operation_name: str,) -> SearchResult[List[Operation]]:
        """
        Find a worker in the registry.

        Action:
            1.  Send an exception chain in the SearchResult if either of the following occur:
                    -   A param is flagged unsafe.
                    -   The search is not completed.
            2.  Otherwise, send the success result.
        Args:
            domain: str
            operation_name: str
        Returns:
            SearchResult[List[Operation]]
        Raises:
            WorkerRegistryControllerException
        """
        method = f"{self.__class__.__name__}.call_worker"
        
        # Handle the case that, the domain or operation+name are flagged unsafe.
        param_validation_result = self._toolkit.worker_search_bootstrapper.execute(
            domain=domain,
            name=operation_name,
            name_validator=self._toolkit.name_validator,
            validation_bootstrapper=self._toolkit.validation_bootstrapper,
        )
        if param_validation_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=param_validation_result.exception
                )
            )
        # --- When the params are validated, search with them. ---#
        search_result = self._toolkit.worker_search.execute(
            domain=domain,
            operation_name=operation_name,
            registry=self._registry,
        )
        # handle the case that, the search was not completed.
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
    def domain_workers(self, domain: str,) -> SearchResult[List[dict[str, Operation]]]:
        """
        Find the workers in a domain.

        Action:
            1.  Send an exception chain in the SearchResult if any of the following occur.
                    -   domain is flagged unsafe.
            2.  Otherwise, send the success result
        Args:
            domain: str
        Returns:
            SearchResult[List[dict[str, Operation]]]
        Raises:
            WorkerRegistryControllerException
        """
        method = f"{self.__class__.__name__}.find_domain_workers"
        
        # Handle the case that, the domain is flagged unsafe.
        param_validation_result = self._toolkit.domain_search_bootstrapper.execute(
            domain=domain,
            name_validator=self._toolkit.name_validator,
            validation_bootstrapper=self._toolkit.validation_bootstrapper,
        )
        if param_validation_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=param_validation_result.exception
                )
            )
        # --- When the param is validated, search with it. ---#
        search_result = self._toolkit.domain_search.execute(
            domain=domain,
            registry=self._registry,
        )
        # handle the case that, the search was not completed.
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
        