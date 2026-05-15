# src/validation/context/edge/operation.py

"""
Module: validation.context.edge.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class EdgeContextValidator(Validator[EdgeContext]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a EdgeContext instance is certified safe, reliable and consistent before use.
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
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            edge_service: EdgeService = EdgeService(),
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[EdgeContext]:
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
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   edge_service (EdgeService)
            *   identity_service (IdentityService):
        # RETURNS:
            *   ValidationResult[EdgeContext] containing either:
                    - On failure:   Exception.
                    - On success:   EdgeContext in the payload.
        Raises:
            *   TypeError
            *   NullEdgeContextException
            *   ZeroEdgeContextFlagsException
            *   ArenaEdgeContextFlagsException
            *   EdgeContextValidationRouteException
            *   EdgeContextValidationException
        """
        method = "EdgeContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EdgeContextValidationException(
                    msg=f"{method}: {EdgeContextValidationException.MSG}",
                    ex=NullEdgeContextException(f"{method}: {NullEdgeContextException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, EdgeContext):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EdgeContextValidationException(
                    msg=f"{method}: {EdgeContextValidationException.MSG}",
                    ex=TypeError(
                        f"{method}: Was expecting a EdgeContext, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate into EdgeContext for additional tests. ---#
        context = cast(EdgeContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EdgeContextValidationException(
                    msg=f"{method}: {EdgeContextValidationException.MSG}",
                    ex=ZeroEdgeContextFlagsException(f"{method}: {ZeroEdgeContextFlagsException.MSG}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EdgeContextValidationException(
                    msg=f"{method}: {EdgeContextValidationException.MSG}",
                    ex=ArenaEdgeContextFlagsException(
                        f"{method}: {ArenaEdgeContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation = identity_service.validate_id(candidate=context.id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeContextValidationException(
                        msg=f"{method}: {EdgeContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_EdgeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-schema target.
        if context.designation is not None:
            validation = identity_service.validate_name(context.designation)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeContextValidationException(
                        msg=f"{method}: {EdgeContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the name_EdgeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-coord target.
        if context.coord is not None:
            validation = coord_service.validator.validate(context.coord)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeContextValidationException(
                        msg=f"{method}: {EdgeContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the coord_EdgeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-board target.
        if context.board is not None:
            validation = board_service.validator.validate(context.board)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeContextValidationException(
                        msg=f"{method}: {EdgeContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_EdgeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-occupant target.
        if context.occupant is not None:
            validation = edge_service.validator.validate(context.occupant)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeContextValidationException(
                        msg=f"{method}: {EdgeContextValidationException.MSG}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_EdgeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-state.
        if context.state is not None:
            if not isinstance(context.state, EdgeState):
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeContextValidationException(
                        msg=f"{method}: {EdgeContextValidationException.MSG}",
                        ex=TypeError(
                            f"{method}: Was expecting a EdgeState, got {type(candidate).__name__} instead."
                        )
                    )
                )
            # On certification success return the board_EdgeContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            EdgeContextValidationException(
                msg=f"{method}: {EdgeContextValidationException.MSG}",
                ex=EdgeContextValidationRouteException(
                    f"{method}: {EdgeContextValidationRouteException.MSG}"
                )
            )
        )

