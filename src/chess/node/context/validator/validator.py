# src/chess/node/context/validator/validator.py

"""
Module: chess.node.context.validator.validator
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations

import sys
from typing import Any, cast

from chess.node import (
    DiscoveryStatus, DiscoveryStatusNullException, ExcessiveNodeContextFlagsException, NodeContext,
    NodeContextValidationFailedException,
    NodeContextValidationRouteException, NodeValidator,
    NullNodeContextException,
    ZeroNodeContextFlagsException
)
from chess.square import SquareService
from chess.system import LoggingLevelRouter, NumberValidator, ValidationResult, Validator


class NodeContextValidator(Validator[NodeContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a NodeContext instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception returned to the caller.

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
            square_service: SquareService = SquareService(),
            node_validator: NodeValidator = NodeValidator(),
            number_validator: NumberValidator = NumberValidator()
    ) -> ValidationResult[NodeContext]:
        """
        # ACTION:
            1.  If Candidate fails existence or type checks return the exception chain in the ValidationResult. Else,
                test how many optional attributes are not null.
            2.  If only one attribute is one and only one attribute is not null return the exception chain in the
                ValidationResult.
            3.  If no route is found for the enabled attribute send an exception chain in the ValidationResult.
            4.  If a validation route exists return the outcome of the validation to the caller.
        # PARAMETERS:
            *   candidate (Any)
            *   discovery_status_service (Discovery_StatusService)
            *   square_service (SquareService)
            *   node_validator (NodeValidator)
            *   number_validator (NumberValidator):
        # RETURNS:
            *   ValidationResult[NodeContext] containing either:
                    - On failure: Exception.
                    - On success: NodeContext in the payload.
        # RAISES:
            *   TypeError
            *   NullNodeContextException
            *   ZeroNodeContextFlagsException
            *   ExcessiveNodeContextFlagsException
            *   NodeContextValidationRouteException
            *   NodeContextValidationFailedException
        """
        method = "NodeContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidationFailedException(
                    message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullNodeContextException(f"{method}: {NullNodeContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, NodeContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidationFailedException(
                    message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(
                        f"{method}: Was expecting a NodeContext, got {type(candidate).__predecessor__} instead."
                    )
                )
            )
        # --- Cast the candidate to NodeContext for additional tests. ---#
        context = cast(NodeContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidationFailedException(
                    message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ZeroNodeContextFlagsException(f"{method}: {ZeroNodeContextFlagsException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidationFailedException(
                    message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ExcessiveNodeContextFlagsException(
                        f"{method}: {ExcessiveNodeContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.priority is not None:
            validation = number_validator.validate(
                candidate=context.priority,
                floor=-(sys.maxsize -1),
                ceiling=sys.maxsize
            )
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the priority_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-predecessor target.
        if context.predecessor is not None:
            validation = node_validator.validate(candidate=context.predecessor)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the predecessor_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-square target.
        if context.square is not None:
            validation = square_service.validator.validate(context.square)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the square_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-discovery_status target.
        if context.discovery_status is not None:
            validation = cls.validate_discovery_status(context.discovery_status)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidationFailedException(
                        message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the discovery_status_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            NodeContextValidationFailedException(
                message=f"{method}: {NodeContextValidationFailedException.DEFAULT_MESSAGE}",
                ex=NodeContextValidationRouteException(
                    f"{method}: {NodeContextValidationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )
    
    @classmethod
    def validate_discovery_status(cls, candidate: Any) -> ValidationResult[DiscoveryStatus]:
        """
        # ACTION:
            1.  If Candidate fails existence or type checks return the exception chain in the ValidationResult.
                Else, cast to DiscoveryState and send in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
        # RETURNS:
            *   ValidationResult[DiscoveryStatus] containing either:
                    - On failure: Exception.
                    - On success: DiscoveryStatus in the payload.
        # RAISES:
            *   TypeError
            *   DiscoveryStatusNullException
        """
        method = "NodeContextValidator.validate_discovery_status"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                    DiscoveryStatusNullException(f"{method}: {DiscoveryStatusNullException.DEFAULT_MESSAGE}")
                )
        # Handle the wrong class case.
        if not isinstance(candidate, NodeContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidationFailedException(
                    ex=TypeError(
                        f"{method}: Was expecting a DiscoveryStatus, got {type(candidate).__predecessor__} instead."
                    )
                )
            )
        return ValidationResult.success(cast(DiscoveryStatus, candidate))

