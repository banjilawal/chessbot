# src/operation/registry/worker/validation/search/domain/operation.py

"""
Module: operation.registry.worker.validation.search.domain.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from err import NullException
from operation import NameValidator, Operation, ValidationBootstrapper, WorkerRegistryOperation
from result import ValidationResult
from util import LoggingLevelRouter


class RegistryNameValidator(WorkerRegistryOperation):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            names: List[str],
            name_validator: NameValidator |  None = None,
    ) -> ValidationResult[int]:
        method = f"{cls.__name__}.execute"
        
        if name_validator is None:
            name_validator = NameValidator()
            
        for name in names:
            validation_result = name_validator.validate(name)
            if validation_result.is_failure:
                return ValidationResult.failure(validation_result.exception)
            
        return ValidationResult.success(0)