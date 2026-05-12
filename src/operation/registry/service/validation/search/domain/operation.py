# src/operation/registry/service/validation/search/domain/operation.py

"""
Module: operation.registry.service.validation.search.domain.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from err import NullException
from operation import NameValidator, Operation, ValidationBootstrapper, ServiceRegistryOperation
from result import ValidationResult
from util import LoggingLevelRouter


class DomainSearchBootstrapper(ServiceRegistryOperation):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            name: str,
            name_validator: NameValidator |  None = None,
    ) -> ValidationResult[int]:
        method = f"{cls.__name__}.execute"
        if name_validator is None:
            name_validator = NameValidator()
        
        validation_result = name_validator.validate(name)
        if validation_result.is_failure:
            return ValidationResult.failure(validation_result.exception)
            
        return ValidationResult.success(0)