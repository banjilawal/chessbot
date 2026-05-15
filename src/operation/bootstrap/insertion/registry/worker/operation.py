# src/operation/bootstrap/insertion/registry/worker/operation.py

"""
Module: operation.boostrap.insertion.registry.worker.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import WorkerRegistry
from result import ValidationResult
from util import LoggingLevelRouter
from controller import WorkerRegistryController
from err import NewWorkerRegistrationException, OperationNullException, RegistryKeyCollisionException
from operation import Operation, RegistryEntryNameValidator, ValidationBootstrapper, WorkerRegistryOperation



class BootstrapWorkerRegistration(WorkerRegistryOperation):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Validate a worker is a safe Operation before adding to the WorkerRegistry.
        2.  Detect key collisions in the before attempting to add a new entry in a Worker Domain.

    Attributes:

    Provides:
        -   def execute(
                worker: Operation,
                registry: WorkerRegistry,
                null_exception: OperationNullException,
                validation_bootstrapper: ValidationBootstrapper,
                registry_entry_name_validator: RegistryEntryNameValidator\,
            ) -> ValidationResult[Operation]:

    Super Class:
        WorkerRegistryOperation
    """
    NAME = "insert_worker"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            worker: Operation,
            registry: WorkerRegistry,
            null_exception: OperationNullException | None = None,
            validation_bootstrapper: ValidationBootstrapper | None = None,
            registry_entry_name_validator: RegistryEntryNameValidator| None = None,
    ) -> ValidationResult[Operation]:
        """
        validate a worker before adding it to WorkerRegistry.
        
        Action:
            1.  Send an exception chain in the ValidationResult if either condition occurs.
                    -   The worker is not an Operation.
                    -   Either, worker.DOMAIN or worker.NAME are not safe Strings.
                    -   The worker's name has already been used in the domain.
            2.  Otherwise, send the success result.
        Args:
            worker: Operation
            registry: WorkerRegistry
            null_exception: OperationNullException
            validation_bootstrapper: ValidationBootstrapper
            registry_entry_name_validator: RegistryEntryNameValidator
        Returns:
            ValidationResult[Operation
        Raises:
            NewWorkerRegistrationException
            RegistryKeyCollisionException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies ---#
        if null_exception is None:
            null_exception = OperationNullException()
        if validation_bootstrapper is None:
            validation_bootstrapper = ValidationBootstrapper()
        if registry_entry_name_validator is None:
            registry_entry_name_validator = RegistryEntryNameValidator()
        
        # Handle the case that, the worker is not a valid operation.
        worker_validation_result = validation_bootstrapper.validate(
            candidate=worker,
            target_model=Operation,
            null_exception=null_exception,
        )
        if worker_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NewWorkerRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NewWorkerRegistrationException.MSG,
                    err_code=worker_validation_result.ERR_CODE,
                    ex=worker_validation_result.exception,
                )
            )
        # Handle the case that, either the worker's domain or name are not good strings.
        keys_validation_result = registry_entry_name_validator.validate(
            candidates=[worker.DOMAIN, worker.NAME],
            validation_bootstrapper=validation_bootstrapper,
        )
        if keys_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NewWorkerRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NewWorkerRegistrationException.MSG,
                    err_code=worker_validation_result.ERR_CODE,
                    ex=keys_validation_result.exception,
                )
            )
        # Handle the case that, the worker's name has already been used in the domain.
        if worker.DOMAIN in registry.entries.keys():
            if worker.NAME in registry.entries[worker.DOMAIN].keys():
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NewWorkerRegistrationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=NewWorkerRegistrationException.MSG,
                        err_code=worker_validation_result.ERR_CODE,
                        ex=RegistryKeyCollisionException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=RegistryKeyCollisionException.MSG,
                            err_code=RegistryKeyCollisionException.ERR_CODE,
                            var="operation_name",
                            val=worker.NAME,
                        ),
                    )
                )        
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(worker)

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register(worker=BootstrapWorkerRegistration)
        