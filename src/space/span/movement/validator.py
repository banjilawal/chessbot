# src/span/movement/validator.py

"""
Module: span.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import Any, Type, cast

from bootstrapper import PrimingValidator
from container import VectorSet
from err import NullException
from result import ValidationResult
from space.span import VectorMovement
from validator import Validator


class MovementValidator(Validator[VectorMovement]):

    _vector_validator: VectorValidator = VectorValidator()
    _priming_validator: PrimingValidator = PrimingValidator()
    
    
    def execute(self, candidate: Any) -> ValidationResult[VectorMovement]:
        priming = self._priming_validator.execute(
            candidate=candidate,
            target_model=Type[VectorMovement],
            null_exception=NullException()
        )
        if priming.is_failure:
            return ValidationResult.failure(
                priming.exception
            )
        movement = cast(VectorMovement, priming.payload)
        vector_set_validation = self._priming_validator.execute(
            candidate=movement_vectors,
            target_model=Type[VectorSet],
            null_exception=NullException()
        )
        if vector_set_validation.is_failure:
            return ValidationResult.failure(
                priming.exception
            )
        return ValidationResult.success(movement)
        