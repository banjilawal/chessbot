# src/chess/edge/validator/validator.py

"""
Module: chess.edge.validator.validator
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from __future__ import annotations

import sys
from math import sqrt
from typing import Any, cast

from chess.node import NodeValidator
from chess.system import (
    BOARD_DIMENSION, IdentityService, LoggingLevelRouter, NumberValidator, ValidationResult, Validator
)
from chess.edge import (
    CircularEdgeException, Edge, EdgeDistanceException, EdgeHeuristicException, NullEdgeException,
    ValidatingEdgeException,
    EdgeWeightException,
)

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
            node_validator: NodeValidator = NodeValidator(),
            number_validator: NumberValidator = NumberValidator(),
            identity_service: IdentityService = IdentityService(),
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
            *   ValidationResult[Edge] containing either:
                    - On failure: Exception.
                    - On success: Edge in the payload.
        # RAISES:
            *   TypeError
            *   NullEdgeException
            *   ValidatingEdgeException
        """
        method = "EdgeValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ValidatingEdgeException(
                    message=f"{method}: {ValidatingEdgeException.DEFAULT_MESSAGE}",
                    ex=NullEdgeException(f"{method}: {NullEdgeException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(Edge, candidate):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ValidatingEdgeException(
                    message=f"{method}: {ValidatingEdgeException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected an Edge, got {type(candidate).__name__}. instead")
                )
            )
        # --- Cast the candidate to an Edge for additional tests. ---#
        edge = cast(candidate, Edge)
        
        # Handle the case that the label is not certified as safe
        label_validation_result = identity_service.validate_id(edge.id)
        # Return the exception chain on failure.
        if label_validation_result.is_failure:
            return ValidationResult.failure(
                ValidatingEdgeException(
                    message=f"{method}: {ValidatingEdgeException.DEFAULT_MESSAGE}",
                    ex=label_validation_result.exception
                )
            )
        # Handle the case that the distance is not at between 0 and the board's diagonal.
        distance_validation_result = number_validator.validate(
            candidate=edge.distance,
            floor=0,
            # Ceiling is the diagonal to an int and increment by 1 to handle truncation.
            ceiling=cast(int, sqrt(2) *BOARD_DIMENSION) + 1,
        )
        if distance_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ValidatingEdgeException(
                    message=f"{method}: {ValidatingEdgeException.DEFAULT_MESSAGE}",
                    ex=EdgeDistanceException(
                        message="{method}: {EdgeDistanceException.DEFAULT_MESSAGE}",
                        ex=distance_validation_result.exception
                    )
                )
            )
        # Handle the case that the heuristic is not a number.
        heuristic_validation_result = number_validator.validate(
            candidate=edge.heuristic,
            # Heuristic is probably going to be distance and the max ransom (the king's).
            ceiling=sys.maxsize,
            floor=0,
        )
        if heuristic_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ValidatingEdgeException(
                    message=f"{method}: {ValidatingEdgeException.DEFAULT_MESSAGE}",
                    ex=EdgeHeuristicException(
                        message=f"{method}: {EdgeHeuristicException.DEFAULT_MESSAGE}",
                        ex=heuristic_validation_result.exception
                    )
                )
            )
        # Handle the case that the weight is not a number.
        weight_validation_result = number_validator.validate(
            candidate=edge.weight,
            ceiling=sys.maxsize,
            floor=(-sys.maxsize + 1),
        )
        if weight_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ValidatingEdgeException(
                    message=f"{method}: {ValidatingEdgeException.DEFAULT_MESSAGE}",
                    ex=EdgeWeightException(
                        message=f"{method}: {EdgeWeightException.DEFAULT_MESSAGE}",
                        ex=weight_validation_result.exception
                    )
                )
            )
        # Handle the case that the head is not certified as a safe node.
        head_validation_result = node_validator.validate(edge.head)
        if head_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ValidatingEdgeException(
                    message=f"{method}: {ValidatingEdgeException.DEFAULT_MESSAGE}",
                    ex=head_validation_result.exception
                )
            )
        # Handle the case that the tail is not certified as a safe node.
        tail_validation_result = node_validator.validate(edge.head)
        if tail_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ValidatingEdgeException(
                    message=f"{method}: {ValidatingEdgeException.DEFAULT_MESSAGE}",
                    ex=tail_validation_result.exception
                )
            )
        # Handle the case that head and tail are the same.
        if edge.head == edge.tail:
            # Return the exception chain on failure
            return ValidationResult.failure(
                ValidatingEdgeException(
                    message=f"{method} {ValidatingEdgeException.DEFAULT_MESSAGE}",
                    ex=CircularEdgeException(f"{method}: {CircularEdgeException.DEFAULT_MESSAGE}")
                )
            )
        # --- Send validated edge to the caller. ---#
        return ValidationResult.success(payload=edge)

