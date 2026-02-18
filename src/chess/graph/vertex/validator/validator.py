# src/chess/graph/vertex/validator/validator.py

"""
Module: chess.graph.vertex.validator.validator
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, List, cast

from chess.graph import DiscoveryStatus, NullVertexException, Vertex, VertexValidationFailedException
from chess.square import SquareValidator
from chess.system import LoggingLevelRouter, NumberValidator, ValidationResult, Validator


class VertexValidator(Validator[Vertex]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Vertex instance is certified safe, reliable and consistent before use.
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
            square_validator: SquareValidator = SquareValidator(),
    ) -> ValidationResult[Vertex]:
        """
        # ACTION:
            1.  If the candidate fails existence or type tests send the exception in the ValidationResult.
                Else, cast to Vertex instance, vertex.
            2.  If either the head, tail, distance, heuristic or weight fail verification send an exception chain
                in the ValidationResult. Else, send the vertex in the ValidationResult..
        # PARAMETERS:
            *   candidate (Any)
            *   vertex_validator (VertexValidator)
            *   identity_service (IdentityService)
            *   number_validator (NumberValidator)
        # RETURNS:
            *   ValidationResult[] containing either:
                    - On failure: Exception.
                    - On success: Vertex in the payload.
        # RAISES:
            *   TypeError
            *   NullVertexException
            *   VertexValidationFailedException
        """
        method = "VertexValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VertexValidationFailedException(
                    message=f"{method}: {VertexValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullVertexException(f"{method}: {NullVertexException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(Vertex, candidate):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VertexValidationFailedException(
                    message=f"{method}: {VertexValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected an Vertex, got {type(candidate).__name__}. instead")
                )
            )
        # --- Cast the candidate to an Vertex for additional tests ---#
        vertex = cast(candidate, Vertex)
        
        # Handle the case that the square is not valid.
        square_validation_result = square_validator.validate(vertex.square)
        if square_validation_result.is_failure:
            # Return the exception chain on failure.
            ValidationResult.failure(
                VertexValidationFailedException(
                    message=f"{method}: {VertexValidationFailedException.DEFAULT_MESSAGE}",
                    ex=square_validation_result.exception
                )
            )
        # Handle the case that the incoming_vertexs is not a list of vertexs.
        if not isinstance(vertex.incoming_vertexs, List):
            # Return the exception chain on failure.
            ValidationResult.failure(
                VertexValidationFailedException(
                    message=f"{method}: {VertexValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(
                        f"{method}: Vertex expected a List of Vertexs, for its incoming got "
                        f"{type(vertex.incoming_vertexs).__name__}. instead."
                    )
                )
            )
        # Handle the case that the outgoing_vertexs is not a list of vertexs.
        if not isinstance(vertex.outgoing_vertexs, List):
            # Return the exception chain on failure.
            ValidationResult.failure(
                VertexValidationFailedException(
                    message=f"{method}: {VertexValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(
                        f"{method}: Vertex expected a List of Vertexs, for its outgoing got "
                        f"{type(vertex.outgoing_vertexs).__name__}. instead."
                    )
                )
            )
        # If the predecessor is not null handle the case that its not a Vertex.
        if vertex.predecessor is not None and not isinstance(vertex.predecessor, Vertex):
            # Return the exception chain on failure.
            ValidationResult.failure(
                VertexValidationFailedException(
                    message=f"{method}: {VertexValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(
                        f"{method}: Vertex expected a Vertex for its predecessor, got "
                        f"{type(vertex.predecessor).__name__}. instead."
                    )
                )
            )
        # Handle the case that the priority is not a number
        priority_validation_result = number_validator.validate(vertex.priority)
        if priority_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VertexValidationFailedException(
                    message=f"{method}: {VertexValidationFailedException.DEFAULT_MESSAGE}",
                    ex=priority_validation_result.exception
                )
            )
        # Handle the case that the DiscoveryStatus does not exist
        if vertex.discovery_status is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VertexValidationFailedException(
                    message=f"{method}: {VertexValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullDiscoveryStatusException(
                        f"{method}: {NullDiscoveryStatusException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the DiscoveryStatus is the wrong type
        if not isinstance(vertex.discovery_status, DiscoveryStatus):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VertexValidationFailedException(
                    message=f"{method}: {VertexValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(
                        f"{method}: Expected DiscoveryStatus, got {type(vertex.discovery_status).__name__} instead."
                    )
                )
            )
        # Tests have been passed return the vertex in the ValidationResult.
        return ValidationResult.success(payload=vertex)