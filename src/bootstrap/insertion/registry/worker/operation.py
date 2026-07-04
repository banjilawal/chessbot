# src/bootstrap/insertion/registry/worker/operation.py

"""
Module: bootstrap.insertion.registry.worker.operation
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
from operation import Primer, Operation, RegistryEntryNameValidator, ValidationPrimer


class PrimingWorkerRegistration(Primer[Operation]):
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
                validation_primer: ValidationPrimer,
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
            validation_primer: ValidationPrimer | None = None,
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
            validation_primer: ValidationPrimer
            registry_entry_name_validator: RegistryEntryNameValidator
        Returns:
            ValidationResult[Operation]
        Raises:
            NewWorkerRegistrationException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if null_exception is None:
            null_exception = OperationNullException()
        if validation_primer is None:
            validation_primer = ValidationPrimer()
        if registry_entry_name_validator is None:
            registry_entry_name_validator = RegistryEntryNameValidator()
        
        # Handle the case that, the worker is not a valid operation.
        worker_validation_result = validation_primer.validate(
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
            validation_primer=validation_primer,
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
            name_collision_result = cls._name_collision_helper(
                target=worker,
                registry=registry,
            )
            if name_collision_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NewWorkerRegistrationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=NewWorkerRegistrationException.MSG,
                        err_code=worker_validation_result.ERR_CODE,
                        ex=name_collision_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(worker)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _name_collision_helper(
            cls,
            target: Operation,
            registry: WorkerRegistry,
    ) -> ValidationResult[Operation]:
        """
        Process the cases where the worker's operation_name has already been a key.

        Action:
            1.  If the worker's name is being used by a different worker in the domain send an
                exception chain in the ValidationResult.
            2.  Otherwise, send the success result.
        Args:
            target: Operation
            registry: WorkerRegistry
        Returns:
            ValidationResult[Operation]
        Raises:
            RegistryKeyCollisionException
        """
        method = f"{cls.__name__}._name_collision_helper"
        
        # Search for the registry using the worker's domain and name.
        registered_worker = None
        if target.NAME in registry.entries[target.DOMAIN].keys():
            registered_worker = registry.entries[target.DOMAIN][target.NAME]
        
        # --- If the worker's name is not in the domain send the success result. ---#
        if registered_worker is None:
            return ValidationResult.success(target)
        
        # Handle the case that, the registered_worker's type differs from the target's
        if not isinstance(type(registered_worker), type(target)):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RegistryKeyCollisionException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=RegistryKeyCollisionException.MSG,
                        err_code=RegistryKeyCollisionException.ERR_CODE,
                        var=f"shared_key={target.NAME}",
                        val=f"registered_worker_type=f{type(registered_worker).__name__}",
                    )
                )
        # --- Otherwise, the target and the registered_worker are the same. Return success. ---#
        return ValidationResult.success(target)

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=PrimingWorkerRegistration)
        