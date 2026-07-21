# src/certifier/edge/validator.py

"""
Module: certifier.edge.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class EdgeRootCertifier(ModelRootCertifier[Edge]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a EdgeBlueprint instance is certified safe, reliable and consistent before use.
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
    ) -> ValidationResult[Edge]:
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
            *   ValidationResult[Edge] containing either:
                    - On failure:   Exception.
                    - On success:   EdgeBlueprint in the payload.
        Raises:
            *   TypeError
            *   NullEdgeBlueprintException
            *   ZeroEdgeBlueprintFlagsException
            *   ArenaEdgeBlueprintFlagsException
            *   EdgeBlueprintValidationRouteException
            *   EdgeCertifierException
        """
        method = "EdgeCertifier.execute"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EdgeCertifierException(
                    msg=f"{method}: {EdgeCertifierException.MSG}",
                    ex=NullEdgeBlueprintException(f"{method}: {NullEdgeBlueprintException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, EdgeBlueprint):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EdgeCertifierException(
                    msg=f"{method}: {EdgeCertifierException.MSG}",
                    ex=TypeError(
                        f"{method}: Was expecting a EdgeBlueprint, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate into EdgeBlueprint for additional tests. ---#
        blueprint = cast(EdgeBlueprint, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(blueprint.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EdgeCertifierException(
                    msg=f"{method}: {EdgeCertifierException.MSG}",
                    ex=ZeroEdgeBlueprintFlagsException(f"{method}: {ZeroEdgeBlueprintFlagsException.MSG}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EdgeCertifierException(
                    msg=f"{method}: {EdgeCertifierException.MSG}",
                    ex=ArenaEdgeBlueprintFlagsException(
                        f"{method}: {ArenaEdgeBlueprintFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if blueprint.id is not None:
            validation = identity_service.validate_id(candidate=blueprint.id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeCertifierException(
                        msg=f"{method}: {EdgeCertifierException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the id_EdgeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-schema target.
        if blueprint.name is not None:
            validation = identity_service.validate_name(blueprint.name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeCertifierException(
                        msg=f"{method}: {EdgeCertifierException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the name_EdgeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-coord target.
        if blueprint.coord is not None:
            validation = coord_service.run.execute(blueprint.coord)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeCertifierException(
                        msg=f"{method}: {EdgeCertifierException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the coord_EdgeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-board target.
        if blueprint.board is not None:
            validation = board_service.run.execute(blueprint.board)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeCertifierException(
                        msg=f"{method}: {EdgeCertifierException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the board_EdgeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-occupant target.
        if blueprint.occupant is not None:
            validation = edge_service.run.execute(blueprint.occupant)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeCertifierException(
                        msg=f"{method}: {EdgeCertifierException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the board_EdgeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-state.
        if blueprint.state is not None:
            if not isinstance(blueprint.state, EdgeState):
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EdgeCertifierException(
                        msg=f"{method}: {EdgeCertifierException.MSG}",
                        ex=TypeError(
                            f"{method}: Was expecting a EdgeState, got {type(candidate).__name__} instead."
                        )
                    )
                )
            # On certification success return the board_EdgeBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Return the exception chain if there is no validation route for the blueprint.
        return ValidationResult.failure(
            EdgeCertifierException(
                msg=f"{method}: {EdgeCertifierException.MSG}",
                ex=EdgeBlueprintValidationRouteException(
                    f"{method}: {EdgeBlueprintValidationRouteException.MSG}"
                )
            )
        )

