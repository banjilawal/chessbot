# src/validator/context/node/validator.py

"""
Module: validator.context.node.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class NodeContextValidator(ContextValidator[Node]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a NodeContext instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Super Class:
        *   Validator

    Provides:


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
            number_validator: NumberValidator = NumberValidator(),
    ) -> ValidationResult[Node]:
        """
        # ACTION:
            1.  If Candidate fails existence or type checks return the exception chain in the ValidationResult. Else,
                test how many optional attributes are not null.
            2.  If only one attribute is one and only one attribute is not null return the exception chain in the
                ValidationResult.
            3.  If no route is found for the enabled attribute send an exception chain in the ValidationResult.
            4.  If a validation route exists return the outcome of the validation to the caller.
        # PARAMETERS:
            *   rank (Any)
            *   discovery_status_service (Discovery_StatusService)
            *   square_validator (SquareService)
            *   node_validator (NodeValidator)
            *   number_validation (NumberValidator):
        # RETURNS:
            *   ValidationResult[Node] containing either:
                    - On failure: Exception.
                    - On success: NodeContext in the payload.
        Raises:
            *   TypeError
            *   NullNodeContextException
            *   ZeroNodeContextFlagsException
            *   ArenaNodeContextFlagsException
            *   NodeContextValidationRouteException
            *   NodeContextValidatorException
        """
        method = "NodeContextValidator.execute"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidatorException(
                    msg=f"{method}: {NodeContextValidatorException.MSG}",
                    ex=NullNodeContextException(f"{method}: {NullNodeContextException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, NodeContext):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidatorException(
                    msg=f"{method}: {NodeContextValidatorException.MSG}",
                    ex=TypeError(
                        f"{method}: Was expecting a NodeContext, got {type(candidate).__predecessor__} instead."
                    )
                )
            )
        # --- Cast the candidate into NodeContext for additional tests. ---#
        context = cast(NodeContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidatorException(
                    msg=f"{method}: {NodeContextValidatorException.MSG}",
                    ex=ZeroNodeContextFlagsException(f"{method}: {ZeroNodeContextFlagsException.MSG}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeContextValidatorException(
                    msg=f"{method}: {NodeContextValidatorException.MSG}",
                    ex=ArenaNodeContextFlagsException(
                        f"{method}: {ArenaNodeContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-priority target.
        if context.priority is not None:
            validation = number_validator.execute(
                candidate=context.priority,
                floor=-(sys.maxsize -1),
                ceiling=sys.maxsize
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidatorException(
                        msg=f"{method}: {NodeContextValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the priority_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-predecessor target.
        if context.predecessor is not None:
            validation = node_validator.execute(candidate=context.predecessor)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidatorException(
                        msg=f"{method}: {NodeContextValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the predecessor_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-square target.
        if context.home_square is not None:
            validation = square_service.run.execute(context.home_square)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidatorException(
                        msg=f"{method}: {NodeContextValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the square_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-discovery_status target.
        if context.discovery_status is not None:
            validation = node_validator.execute_discovery_status(context.discovery_status)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NodeContextValidatorException(
                        msg=f"{method}: {NodeContextValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the discovery_status_NodeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            NodeContextValidatorException(
                msg=f"{method}: {NodeContextValidatorException.MSG}",
                ex=NodeContextValidationRouteException(
                    f"{method}: {NodeContextValidationRouteException.MSG}"
                )
            )
        )
    


