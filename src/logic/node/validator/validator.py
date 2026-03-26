# src/logic/node/validation/validation.py

"""
Module: logic.node.validation.validation
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, List, cast

from logic.square import SquareValidationProcess
from logic.system import LoggingLevelRouter, NumberValidationProcess, ValidationResult, ValidationProcess
from logic.node import (
    DiscoveryStatus, DiscoveryStatusNullException, NullNodeException, Node, NodeValidationException
)


class NodeValidationProcess(ValidationProcess[Node]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a Node instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   ValidationProcess

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            number_validator: NumberValidationProcess = NumberValidationProcess(),
            square_validator: SquareValidationProcess = SquareValidationProcess(),
    ) -> ValidationResult[Node]:
        """
        # ACTION:
            1.  If the candidate fails existence or type tests send the exception in the ValidationResult.
                Else, cast to Node instance, node.
            2.  If either the head, tail, dist, heuristic or weight fail verification send an exception chain
                in the ValidationResult. Else, send the node in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   node_validator (NodeValidationProcess)
            *   identity_service (IdentityService)
            *   number_validation (NumberValidationProcess)
        # RETURNS:
            *   ValidationResult[] containing either:
                    - On failure: Exception.
                    - On success: Node in the payload.
        Raises:
            *   TypeError
            *   NullNodeException
            *   NodeValidationException
        """
        method = "NodeValidationProcess.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeValidationException(
                    msg=f"{method}: {NodeValidationException.MSG}",
                    ex=NullNodeException(f"{method}: {NullNodeException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Node):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeValidationException(
                    msg=f"{method}: {NodeValidationException.MSG}",
                    ex=TypeError(f"{method}: Expected an Node, got {type(candidate).__name__}. instead")
                )
            )
        # --- Cast the candidate to an Node for additional tests ---#
        node = cast(Node, candidate)
        
        # Handle the case that, the square is not valid.
        square_validation_result = square_validator.execute(node.square)
        if square_validation_result.is_failure:
            # Return the exception chain on failure.
            ValidationResult.failure(
                NodeValidationException(
                    msg=f"{method}: {NodeValidationException.MSG}",
                    ex=square_validation_result.exception
                )
            )
        # Handle the case that, the incoming_nodes is not a list of nodes.
        if not isinstance(node.incoming_nodes, List):
            # Return the exception chain on failure.
            ValidationResult.failure(
                NodeValidationException(
                    msg=f"{method}: {NodeValidationException.MSG}",
                    ex=TypeError(
                        f"{method}: Node expected a List of Nodes, for its incoming got "
                        f"{type(node.incoming_nodes).__name__}. instead."
                    )
                )
            )
        # Handle the case that, the outgoing_nodes is not a list of nodes.
        if not isinstance(node.outgoing_nodes, List):
            # Return the exception chain on failure.
            ValidationResult.failure(
                NodeValidationException(
                    msg=f"{method}: {NodeValidationException.MSG}",
                    ex=TypeError(
                        f"{method}: Node expected a List of Nodes, for its outgoing got "
                        f"{type(node.outgoing_nodes).__name__}. instead."
                    )
                )
            )
        # If the predecessor is not null handle the case that its not a Node.
        if node.predecessor is not None and not isinstance(node.predecessor, Node):
            # Return the exception chain on failure.
            ValidationResult.failure(
                NodeValidationException(
                    msg=f"{method}: {NodeValidationException.MSG}",
                    ex=TypeError(
                        f"{method}: Node expected a Node for its predecessor, got "
                        f"{type(node.predecessor).__name__}. instead."
                    )
                )
            )
        # Handle the case that, the priority is not a number
        priority_validation_result = number_validator.execute(node.priority)
        if priority_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeValidationException(
                    msg=f"{method}: {NodeValidationException.MSG}",
                    ex=priority_validation_result.exception
                )
            )
        # Handle the case that, the DiscoveryStatus does not exist
        if node.discovery_status is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeValidationException(
                    msg=f"{method}: {NodeValidationException.MSG}",
                    ex=DiscoveryStatusNullException(
                        f"{method}: {DiscoveryStatusNullException.MSG}"
                    )
                )
            )
        # Handle the case that, the DiscoveryStatus is the wrong type
        if not isinstance(node.discovery_status, DiscoveryStatus):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                NodeValidationException(
                    msg=f"{method}: {NodeValidationException.MSG}",
                    ex=TypeError(
                        f"{method}: Expected DiscoveryStatus, got {type(node.discovery_status).__name__} instead."
                    )
                )
            )
        # Tests have been passed return the node in the ValidationResult.
        return ValidationResult.success(payload=node)
    
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
        Raises:
            *   TypeError
            *   DiscoveryStatusNullException
        """
        method = "NodeContextValidationProcess.validate_discovery_status"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                DiscoveryStatusNullException(f"{method}: {DiscoveryStatusNullException.MSG}")
            )
        # Handle the wrong class case.
        if not isinstance(candidate, DiscoveryStatus):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TypeError(
                    f"{method}: Was expecting a DiscoveryStatus, got {type(candidate).__predecessor__} instead."
                )
            )
        return ValidationResult.success(cast(DiscoveryStatus, candidate))