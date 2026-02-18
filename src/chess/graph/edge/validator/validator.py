# src/chess/graph/edge/validator/validator.py

"""
Module: chess.graph.edge.validator.validator
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast


from chess.graph import (
    Edge, EdgeDistanceException, EdgeHeuristicException, EdgeValidationFailedException, EdgeWeightException,
    HeadCannotBeTailException, NullEgeException, NodeValidator
)
from chess.system import IdentityService, LoggingLevelRouter, NumberValidator, ValidationResult, Validator


class EdgeValidator(Validator[Edge]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Edge instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            number_validator: NumberValidator = NumberValidator(),
            identity_service: IdentityService = IdentityService(),
            node_validator: NodeValidator = NodeValidator()
    ) -> ValidationResult[Edge]:
        """
        # ACTION:
            1.  If the candidate fails existence or type tests send the exception in the ValidationResult.
                Else, cast to Edge instance, edge.
            2.  If either the head, tail, distance, heuristic or weight fail verification send an exception chain 
                in the ValidationResult. Else, send the edge in the ValidationResult..
        # PARAMETERS:
            *   candidate (Any)
            *   node_validator (NodeValidator)
            *   identity_service (IdentityService)
            *   number_validator (NumberValidator)
        # RETURNS:
            *   ValidationResult[] containing either:
                    - On failure: Exception.
                    - On success: Edge in the payload.
        # RAISES:
            *   TypeError
            *   NullEdgeException
            *   EdgeValidationFailedException
        """
        method = "EdgeValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullEgeException(f"{method}: {NullEgeException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(Edge, candidate):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected an Edge, got {type(candidate).__name__}. instead")
                )
            )
        # --- Cast the candidate to an Edge for additional tests ---#
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
        # Handle the case that the head is not certified as a safe node.
        head_validation_result = node_validator.validate(edge.head)
        if head_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=head_validation_result.exception
                )
            )
        # Handle the case that the tail is not certified as a safe node.
        tail_validation_result = node_validator.validate(edge.head)
        if tail_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method}: {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=tail_validation_result.exception
                )
            )
        # Handle the case that head and tail are the same.
        if edge.head == edge.tail:
            # Return the exception chain on failure
            return ValidationResult.failure(
                EdgeValidationFailedException(
                    message=f"{method} {EdgeValidationFailedException.DEFAULT_MESSAGE}",
                    ex=HeadCannotBeTailException(f"{method}: {HeadCannotBeTailException.DEFAULT_MESSAGE}")
                )
            )
        # Tests have been passed return the edge in the ValidationResult.
        return ValidationResult.success(payload=edge)

