# src/validator/space/span/basis/validator.py

"""
Module: validator.space.span.basis.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic
from typing_extensions import TypeVar

from result import ValidationResult
from validator import SpanValidator



# from carrier_validator import PrimingValidator
# from container import VectorSet
# from err import NullException
# from result import ValidationResult
# from space.span import VectorBasis
# from validator import Validator

T = TypeVar("T", bound="VectorBasis")


class BasisValidator(SpanValidator, Generic[T]):
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
# _vector_validator: VectorValidator = VectorValidator()
    # _priming_validator: PrimingValidator = PrimingValidator()
    #
    #
    # def execute(self, candidate: Any) -> ValidationResult[VectorBasis]:
    #     priming = self._priming_validator.execute(
    #         candidate=candidate,
    #         target_model=Type[VectorBasis],
    #         null_exception=NullException()
    #     )
    #     if priming.is_failure:
    #         return ValidationResult.failure(
    #             priming.exception
    #         )
    #     basis = cast(VectorBasis, priming.payload)
    #     vector_set_validation = self._priming_validator.execute(
    #         candidate=basis.movement_vectors,
    #         target_model=Type[VectorSet],
    #         null_exception=NullException()
    #     )
    #     if vector_set_validation.is_failure:
    #         return ValidationResult.failure(
    #             priming.exception
    #         )
    #     return ValidationResult.success(basis)
        