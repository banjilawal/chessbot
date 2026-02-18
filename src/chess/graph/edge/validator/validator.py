# src/chess/graph/edge/validator/validator.py

"""
Module: chess.graph.edge.validator.validator
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""
from ctypes import cast
from typing import Any

from chess.graph import (
    Edge, EdgeDistanceException, EdgeHeuristicException, EdgeValidationFailedException,
    EdgeWeightException, NullEgeException, VertexValidator
)
from chess.system import IdentityService, LoggingLevelRouter, NumberValidator, ValidationResult, Validator


class EdgeValidator(Validator[Edge]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator(),
            identity_service: IdentityService = IdentityService(),
            vertex_validator: VertexValidator = VertexValidator()
    ) -> ValidationResult[Edge]:
        method = "EdgeValidator.validate"
        
        # Handle the case that the candidate does not exist
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullEgeException(f"{method}: {NullEgeException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the candidate is the wrong type.
        if not isinstance(Edge, candidate):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected an Edge, got {type(candidate).__name__}. instead")
                )
            )
        
        edge = cast(candidate, Edge)
        
        # Handle the case that the id is not certified as safe
        id_validation_result = identity_service.validate_id(edge.id)
        # Return the exception chain on failure.
        if id_validation_result.is_failure:
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=id_validation_result.exception
                )
            )
        # Handle the case that the distance is not a number.
        distance_validation_result = number_validator.validate(edge.distance)
        if distance_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=EdgeDistanceException(
                        f"{method}: {EdgeDistanceException.DEFAULT_MESSAGE}",
                        ex=distance_validation_result.exception
                    )
                )
            )
        # Handle the case that the heuristic is not a number.
        heuristic_validation_result = number_validator.validate(edge.heuristic)
        if heuristic_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=EdgeHeuristicException(
                        f"{method}: {EdgeHeuristicException.DEFAULT_MESSAGE}",
                        ex=heuristic_validation_result.exception
                    )
                )
            )
        # Handle the case that the weight is not a number.
        weight_validation_result = number_validator.validate(edge.weight)
        if weight_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=EdgeWeightException(
                        f"{method}: {EdgeWeightException.DEFAULT_MESSAGE}",
                        ex=weight_validation_result.exception
                    )
                )
            )
        # Handle the case that the head is not certified as a safe vertex.
        head_validation_result = vertex_validator.validate(edge.head)
        if head_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=head_validation_result.exception
                )
            )
        # Handle the case that the tail is not certified as a safe vertex.
        tail_validation_result = vertex_validator.validate(edge.head)
        if tail_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=tail_validation_result.exception
                )
            )
        return ValidationResult.success(payload=edge)
        