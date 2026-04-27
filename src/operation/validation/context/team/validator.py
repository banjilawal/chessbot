# src/operation/validation/context/team/operation.py

"""
Module: operation.validation.context.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class TeamContextValidator(Validator[TeamContext]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a TeamContext instance is certified safe, reliable and consistent before use.
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
            player_service: PlayerService = PlayerService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> ValidationResult[TeamContext]:
        """
        # ACTION:
            1.  If the rank fails existence or type tests send the exception in the ValidationResult.
                Else, cast to TeamContext instance context.
            2.  If one-and-only-one context attribute is not null return an exception in the ValidationResult.
            3.  If there is no certification route for the attribute return an exception in the ValidationResult.
            4.  If the certification route exists use the appropriate service or validation to send either an exception
                chain the ValidationResult or the context.
        # PARAMETERS:
            *   rank (Any)
            *   color_validator (ColorValidator)
            *   player_service (PlayerService)
            *   arena_service (ArenaService)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[TeamContext] containing either:
                    - On failure: Exception.
                    - On success: TeamContext in the payload.
        Raises:
            *   TypeError
            *   NullTeamContextException
            *   ZeroTeamContextFlagsException
            *   ArenaTeamContextFlagsException
            *   TeamContextValidationException
            *   TeamContextValidationRouteException
        """
        method = "TeamContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidationException(
                    msg=f"{method}: {TeamContextValidationException.ERR_CODE}",
                    ex=NullTeamContextException(f"{method}: {NullTeamContextException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, TeamContext):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidationException(
                    msg=f"{method}: {TeamContextValidationException.ERR_CODE}",
                    ex=TypeError(f"{method}: Expected TeamContext, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate into TeamContext for additional tests. ---#
        context = cast(TeamContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidationException(
                    msg=f"{method}: {TeamContextValidationException.ERR_CODE}",
                    ex=ZeroTeamContextFlagsException(f"{method}: {ZeroTeamContextFlagsException.MSG}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidationException(
                    msg=f"{method}: {TeamContextValidationException.ERR_CODE}",
                    ex=ArenaTeamContextFlagsException(
                        f"{method}: {ArenaTeamContextFlagsException.MSG}"
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
                    TeamContextValidationException(
                        msg=f"{method}: {TeamContextValidationException.ERR_CODE}", ex=validation.exception
                    )
                )
            # On certification success return the TeamContext_id in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-owner target.
        if context.owner is not None:
            validation = player_service.validator.validate(candidate=context.owner)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextValidationException(
                        msg=f"{method}: {TeamContextValidationException.ERR_CODE}", ex=validation.exception
                    )
                )
            # On certification success return the TeamContext_owner in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-arena target.
        if context.arena is not None:
            validation = arena_service.validator.search_service(candidate=context.arena)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextValidationException(
                        msg=f"{method}: {TeamContextValidationException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the TeamContext_arena in a ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-color target.
        if context.color is not None:
            validation = color_validator.validate(candidate=context.color)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextValidationException(
                        msg=f"{method}: {TeamContextValidationException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the team_color_context in a ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            TeamContextValidationException(
                msg=f"{method}: {TeamContextValidationException.ERR_CODE}",
                ex=TeamContextValidationRouteException(
                    f"{method}: {TeamContextValidationRouteException.MSG}"
                )
            )
        )