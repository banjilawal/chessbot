# src/validator/blueprint/node/validator.py

"""
Module: validator.blueprint.node.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class NodeBlueprintValidator(BlueprintValidator[Node]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a NodeBlueprint instance is certified safe, reliable and consistent before use.
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
                    - On success: NodeBlueprint in the payload.
        Raises:
            *   TypeError
            *   NullNodeBlueprintException
            *   ZeroNodeBlueprintFlagsException
            *   ArenaNodeBlueprintFlagsException
            *   NodeBlueprintValidationRouteException
            *   NodeBlueprintValidatorException
        """
        method = "NodeBlueprintValidator.execute"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeBlueprintValidatorException(
                    msg=f"{method}: {NodeBlueprintValidatorException.MSG}",
                    ex=NullNodeBlueprintException(f"{method}: {NullNodeBlueprintException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, NodeBlueprint):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeBlueprintValidatorException(
                    msg=f"{method}: {NodeBlueprintValidatorException.MSG}",
                    ex=TypeError(
                        f"{method}: Was expecting a NodeBlueprint, got {type(candidate).__predecessor__} instead."
                    )
                )
            )
        # --- Cast the candidate into NodeBlueprint for additional tests. ---#
        blueprint = cast(NodeBlueprint, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(blueprint.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeBlueprintValidatorException(
                    msg=f"{method}: {NodeBlueprintValidatorException.MSG}",
                    ex=ZeroNodeBlueprintFlagsException(f"{method}: {ZeroNodeBlueprintFlagsException.MSG}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NodeBlueprintValidatorException(
                    msg=f"{method}: {NodeBlueprintValidatorException.MSG}",
                    ex=ArenaNodeBlueprintFlagsException(
                        f"{method}: {ArenaNodeBlueprintFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-priority target.
        if blueprint.priority is not None:
            validation = number_validator.execute(
                candidate=blueprint.priority,
                floor=-(sys.maxsize -1),
                ceiling=sys.maxsize
            )
            if validator.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NodeBlueprintValidatorException(
                        msg=f"{method}: {NodeBlueprintValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the priority_NodeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-predecessor target.
        if blueprint.predecessor is not None:
            validation = node_validator.execute(candidate=blueprint.predecessor)
            if validator.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NodeBlueprintValidatorException(
                        msg=f"{method}: {NodeBlueprintValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the predecessor_NodeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-square target.
        if blueprint.home_square is not None:
            validation = square_service.run.build(blueprint.home_square)
            if validator.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NodeBlueprintValidatorException(
                        msg=f"{method}: {NodeBlueprintValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the square_NodeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-discovery_status target.
        if blueprint.discovery_status is not None:
            validation = node_validator.execute_discovery_status(blueprint.discovery_status)
            if validator.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    NodeBlueprintValidatorException(
                        msg=f"{method}: {NodeBlueprintValidatorException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the discovery_status_NodeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Return the exception chain if there is no validation route for the blueprint.
        return ValidationResult.failure(
            NodeBlueprintValidatorException(
                msg=f"{method}: {NodeBlueprintValidatorException.MSG}",
                ex=NodeBlueprintValidationRouteException(
                    f"{method}: {NodeBlueprintValidationRouteException.MSG}"
                )
            )
        )
    


