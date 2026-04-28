# src/operation/registration/invoke.operation.py

"""
Module: operation.registration.invoke.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from err import ChessException, WorkerOpNameCollisionException, WorkerRegistrationException
from result import InsertionResult, ValidationResult
from model import WorkerRegistry
from system import LoggingLevelRouter
from operation import Operation, RegistryWorkerSearch, WorkerRegistryOperation



class RegisterWorker(WorkerRegistryOperation):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Registers a worker to the registry while maintaining consistency and integrity.

    Attributes:
        DOMAIN = "registration"
        OPERATION_NAME = "register_worker"

    Provides:
        -   def execute(
                    worker: Operation,
                    registry: WorkerRegistry,
                    worker_search: RegistryWorkerSearch | None = None,
            ) -> InsertionResult:

    Super Class:
        WorkerRegistryOperation
    """
    OPERATION_NAME = "register_worker"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            worker: Operation,
            registry: WorkerRegistry,
            worker_search: RegistryWorkerSearch | None = None,
    ) -> InsertionResult:
        """
        Register a new worker to the registry.
        
        Action:
            1.  Send an exception chain in the InsertionResult if either condition occurs.
                    -   A different worker exists in the same domain with the same operation name.
                    -   Registering the worker's entry in the registry dictionary fails.
            2.  Otherwise, send the success result.
        Args:
            worker: Operation
            registry: WorkerRegistry
            worker_search: RegistryWorkerSearch
        Returns:
            InsertionResult
        Raises:
            CoordBuildException
        """
        method = f"{cls.__name__}.execute"
        
        if worker_search is None:
            worker_search = RegistryWorkerSearch()
        
        worker_search_result = worker_search.execute(
            domain=worker.DOMAIN,
            operation_name=worker.OPERATION_NAME,
            registry=registry
        )
        # Handle the case that, the search is not completed.
        if worker_search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                WorkerRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=WorkerRegistrationException.MSG,
                    err_code=WorkerRegistrationException.ERR_CODE,
                    ex=worker_search_result.exception,
                )
            )
        # --- Handoff processing to _collision_helper if the key has already been used. ---#
        if worker_search_result.is_success:
            collision_processing_result = cls._collision_helper(registry)
            # handle the case that, there is a hash key collision.
            if collision_processing_result.is_failure:
                # Send the exception chain on failure.
                return InsertionResult.failure(
                    WorkerRegistrationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=WorkerRegistrationException.MSG,
                        err_code=WorkerRegistrationException.ERR_CODE,
                        ex=collision_processing_result.exception,
                    )
                )
            # Send the success result if there is no hash collision.
            return InsertionResult.success()
        # --- Add a new entry to the registry if the key is new. ---#
        registry.entries[worker.DOMAIN][worker.OPERATION_NAME] = worker
        registry.registration_counters[worker.DOMAIN][worker.OPERATION_NAME] += 1
        
        # --- Send the success result . ---#
        return InsertionResult.success()
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _collision_helper(
            cls,
            colliding_key: str,
            new_worker: Operation,
            registry: WorkerRegistry,
    ) -> InsertionResult:
        """
        Process the cases where the worker's operation_name has already been a key.

        Action:
            1.  Send an exception chain in the InsertionResult if the current entry's value
                is different from the worker to register.
            2.  Otherwise, increment the registration counter, then send the success result.
        Args:
            colliding_key: str
            new_worker: Operation
            registry: WorkerRegistry
        Returns:
            InsertionResult
        Raises:
            WorkerRegistrationException
            WorkerOpNameCollisionException
        """
        method = f"{cls.__name__}._collision_helper"
        
        # --- Get the operation which is already using the key. ---#
        old_worker = registry.entries[new_worker.DOMAIN][colliding_key]
        
        # Handle the case that the, old and new workers are different.
        if old_worker.OPERATION_NAME.upper() != new_worker.OPERATION_NAME.upper():
            # Send the exception chain on failure.
            return InsertionResult.failure(
                WorkerRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=WorkerRegistrationException.MSG,
                    err_code=WorkerRegistrationException.ERR_CODE,
                    ex=WorkerOpNameCollisionException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=WorkerOpNameCollisionException.MSG,
                        err_code=WorkerOpNameCollisionException.ERR_CODE,
                        var="var_registered_worker",
                        val=old_worker,
                    ),
                )
            )
        # --- If the operations are the same, increment the registration counter ---#
        registry.registration_counters[new_worker.DOMAIN][new_worker.OPERATION_NAME] += 1
        
        return InsertionResult.success()
        