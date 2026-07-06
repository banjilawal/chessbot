# src/validator/blueprint/board/validator.py

"""
Module: validator.blueprint.board.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class BoardBlueprintValidator(BlueprintValidator[Board]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a BoardBlueprint instance is certified safe, reliable and consistent before use.
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
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[Board]:
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
            *   arena_service (ArenaService)
            *   identity_service (IdentityService):
        # RETURNS:
            *   ValidationResult[Board] containing either:
                    - On failure:   Exception.
                    - On success:   BoardBlueprint in the payload.
        Raises:
            *   TypeError
            *   NullBoardBlueprintException
            *   ZeroBoardBlueprintFlagsException
            *   ArenaBoardBlueprintFlagsException
            *   BoardBlueprintValidationRouteException
            *   BoardBlueprintValidationException
        """
        method = "BoardBlueprintValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardBlueprintValidationException(
                    msg=f"{method}: {BoardBlueprintValidationException.MSG}",
                    ex=NullBoardBlueprintException(f"{method}: {NullBoardBlueprintException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, BoardBlueprint):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardBlueprintValidationException(
                    msg=f"{method}: {BoardBlueprintValidationException.MSG}",
                    ex=TypeError(f"{method}: Was expecting a BoardBlueprint, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate into BoardBlueprint for additional tests. ---#
        blueprint = cast(BoardBlueprint, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(blueprint.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardBlueprintValidationException(
                    msg=f"{method}: {BoardBlueprintValidationException.MSG}",
                    ex=ZeroBoardBlueprintFlagsException(f"{method}: {ZeroBoardBlueprintFlagsException.MSG}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardBlueprintValidationException(
                    msg=f"{method}: {BoardBlueprintValidationException.MSG}",
                    ex=ArenaBoardBlueprintFlagsException(
                        f"{method}: {ArenaBoardBlueprintFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if blueprint.id is not None:
            validation = identity_service.validate_id(candidate=blueprint.id)
            if validator.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    BoardBlueprintValidationException(
                        msg=f"{method}: {BoardBlueprintValidationException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the id_BoardBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Certification for the search-by-arena target.
        if blueprint.arena is not None:
            validation = arena_service.execute.search_service(blueprint.arena)
            if validator.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    BoardBlueprintValidationException(
                        msg=f"{method}: {BoardBlueprintValidationException.MSG}",
                        ex=validator.exception
                    )
                )
            # On certification success return the arena_BoardBlueprint in the ValidationResult.
            return ValidationResult.success(payload=blueprint)
        
        # Return the exception chain if there is no validation route for the blueprint.
        return ValidationResult.failure(
            BoardBlueprintValidationException(
                msg=f"{method}: {BoardBlueprintValidationException.MSG}",
                ex=BoardBlueprintValidationRouteException(
                    f"{method}: {BoardBlueprintValidationRouteException.MSG}"
                )
            )
        )