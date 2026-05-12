# src/operation/registry/worker/validation/registration/operation.py

"""
Module: operation.registry.worker.validation.registration.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import NullException
from operation import NameValidator, Operation, ValidationBootstrapper, WorkerRegistryOperation
from result import ValidationResult
from util import LoggingLevelRouter


class AddWorkerBootstrapper(WorkerRegistryOperation):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            worker: Operation,
            null_exception: NullException,
            name_validator: NameValidator |  None = None,
            validation_bootstrapper: ValidationBootstrapper | None = None,
    ) -> ValidationResult[Operation]:
        method = f"{cls.__name__}.execute"
        if name_validator is None:
            name_validator = NameValidator()
        if validation_bootstrapper is None:
            validation_bootstrapper = ValidationBootstrapper()
        
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
        operation_name_validation_result = name_validator.validate(worker.OPERATION_NAME)
        if not operation_name_validation_result.is_false:
            return ValidationResult.failure(operation_name_validation_result.exception)
        
        return ValidationResult.success(0)