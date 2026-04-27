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
from system import LoggingLevelRouter
from result import InsertionResult, SearchResult, ValidationResult
from operation import NameValidator, Operation, ValidationBootstrapper, WorkerRegistry
from err import ChessException, OperationNullException, WorkerRegistryControllerException

class WorkerRegistryController(Controller[WorkerRegistry]):
    _validation_bootstrapper: ValidationBootstrapper
    _name_validator: NameValidator
    _registry: WorkerRegistry
    _invocation_count_table: dict[str, int]
    _registration_count_table: dict[str, int]
    
    def __init__(
            self,
            registry: WorkerRegistry | None = None,
            name_validator: NameValidator | NameValidator = None,
            validation_bootstrapper: ValidationBootstrapper | ValidationBootstrapper = None
    ):
        self._registry = registry or WorkerRegistry()
        self._name_validator = name_validator or NameValidator()
        self._validation_bootstrapper = validation_bootstrapper or ValidationBootstrapper()
        self._invocation_count_table = {}
        self._registration_count_table = {}
    
    @property
    def is_empty(self) -> bool:
        return self.number_of_workers == 0
    
    @property
    def number_of_workers(self) -> int:
        return len(self._registry.workers)
    
    @property
    def domains(self) -> List[str]:
        domains = []
        for domain in self._registry.workers.keys():
            domains.append(domain)
        return domains
    
    @LoggingLevelRouter.monitor
    def domain_workers(self, domain: str) -> dict[str, Operation]:
        return self._registry.workers[domain]
    
    @LoggingLevelRouter.monitor
    def domain_worker_names(self, domain: str) -> List[str]:
        names = []
        for name in self._registry.workers[domain].keys():
            names.append(name)
        return names
    
    @LoggingLevelRouter.monitor
    def register_worker(self, worker: Operation) -> InsertionResult:
        """
        Add a new worker to the registry.
        
        Action:
            1.  Send an exception chain in the InsertionResult if any of the following occur.
                    -   The name is not a valid string.
                    -   The worker is null or thr wrong type.
                    -   The name is already in the registry with a different worker.
            2.  If the entry already exists, return a success result.
            3.  Otherwise, add the entry to the registry and return a success result.
        Args:
            name: str
            worker: Operation
        Returns:
            InsertionResult
        Raises:
            WorkerRegistryControllerException
        """
        method = f"{self.__class__.__name__}.register_worker"
        

        # Handle the case that, the name is already in the registry
        if worker.OPERATION_NAME in self._registry.workers.keys():
            # Send the exception chain on failure.
            if worker.__class__.__name__.upper() != self._registry.workers[worker.].__class__.__name__.upper():
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
            else:
                self._registry.workers[worker.DOMAIN] = [worker.OPERATION_NAME, worker]
                return InsertionResult.success()
        self._registry.workers[name.upper()] = worker
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def call_worker(self, name: str) -> SearchResult[List[Operation]]:
        """
        Find a worker in the registry.

        Action:
            1.  Send an exception chain in the SearchResult if:
                    -   The name is not a valid string.
            2.  If key does not exist, return an empty result.
            3.  Otherwise, send the success result.
        Args:
            name: str
        Returns:
            SearchResult
        Raises:
            WorkerRegistryControllerException
        """
        method = f"{self.__class__.__name__}.call_worker"
        
        # Handle the case that, the name is not a safe string.
        name_validation_result = self._name_validator.validate(name)
        if not name_validation_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=name_validation_result.exception
                )
            )
        # Handle the case that, the operation is not registered.
        if name.upper() not in self._registry.workers.keys():
            return SearchResult.empty()
        # --- Forward the work product to the caller. ---#
        current_invocation_count = self._invocation_count_table[name]
        self._invocation_count_table[name] = current_invocation_count + 1
        return SearchResult.success([self._registry.workers[name.upper()]])
    
    @LoggingLevelRouter.monitor
    def run_validations(self, worker: Operation) -> ValidationResult[int]:
        method = f"{self.__class__.__name__}.run_validations"
        
        # Handle the case that, the domain is not a safe string.
        domain_validation_result = self._name_validator.validate(worker.DOMAIN)
        if not domain_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=domain_validation_result.exception
                )
            )
        # Handle the case that, the name is not a safe string.
        name_validation_result = self._name_validator.validate(worker.OPERATION_NAME)
        if not name_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=name_validation_result.exception
                )
            )
        # Handle the case that, the worker is null or not an Operation.
        worker_validation_result = self._validation_bootstrapper.validate(
            candidate=worker,
            target_type=Operation,
            null_exception=OperationNullException(),
        )
        if worker_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=worker_validation_result.exception
                )
            )
        
    @LoggingLevelRouter.monitor
    def _name_collision_checker(self, name: str, worker: Operation):
        method = f"{self.__class__.__name__}._name_collision_handler"
        
        
        
        
    
    @LoggingLevelRouter.monitor
    def _registration_helper(self, name: str, worker: Operation):
        method = f"{self.__class__.__name__}._registration_helper"
        
        # Send the exception chain on failure.
        if worker.__class__.__name__.upper() != self._registry.workers[name].__class__.__name__.upper():
            # Send the exception chain on failure.
            return InsertionResult.failure(
                WorkerRegistryControllerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WorkerRegistryControllerException.MSG,
                    err_code=WorkerRegistryControllerException.ERR_CODE,
                    ex=ChessException()
                )
            )
        self._registration_count_table[name] = self._registration_count_table[name] + 1
        return InsertionResult.success()
        