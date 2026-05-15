# src/operation/registry/worker/validation/registration/operation.py

"""
Module: operation.registry.worker.validation.registration.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import NewWorkerRegistrationException, NullException
from model import WorkerRegistry
from operation import NameValidator, Operation, ValidationBootstrapper, WorkerRegistryOperation
from operation.registry.worker.insert.bootstrap.operation import BootstrapWorkerRegistration
from result import InsertionResult, ValidationResult
from util import LoggingLevelRouter


class AddWorkerBootstrapper(WorkerRegistryOperation):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            worker: Operation,
            registry: WorkerRegistry,
            bootstrap_worker_registration: BootstrapWorkerRegistration | None = None,
    ) -> ValidationResult[Operation]:
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies ---#
        if bootstrap_worker_registration is None:
            bootstrap_worker_registration = BootstrapWorkerRegistration()
            
        worker_bootstrap_result = bootstrap_worker_registration.execute(
            worker=worker,
            registry=registry,
        )
        # Handle the case that, the worker is flagged during bootstrapping.
        if worker_bootstrap_result.is_failure:
            return InsertionResult.failure(
                NewWorkerRegistrationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NewWorkerRegistrationException.MSG,
                    err_code=NewWorkerRegistrationException.ERR_CODE,
                    ex=worker_bootstrap_result.exception
                )
            )

        
        worker_validation = validation_bootstrapper.validate(
            candidate=worker,
            target_type=worker.__class__,
            null_exception=null_exception,
        )
        if not worker_validation.is_false:
            return ValidationResult.failure(worker_validation.exception)
        
        domain_validation_result = name_validator.validate(worker.DOMAIN)
        if not domain_validation_result.is_false:
            return ValidationResult.failure(domain_validation_result.exception)
        operation_name_validation_result = name_validator.validate(worker.NAME)
        if not operation_name_validation_result.is_false:
            return ValidationResult.failure(operation_name_validation_result.exception)
        
        return ValidationResult.success(0)