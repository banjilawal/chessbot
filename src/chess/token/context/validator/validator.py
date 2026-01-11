# src/chess/token/validator/validator.py

"""
Module: chess.token.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.team import TeamService
from chess.rank import RankService
from chess.coord import CoordService
from chess.system import (
    GameColorValidator, IdentityService, LoggingLevelRouter, NotNegativeNumberValidator, Validator, ValidationResult
)
from chess.token import (
    ExcessiveTokenContextFlagsException, NullTokenContextException, TokenContext, TokenContextValidationFailedException,
    TokenContextValidationRouteException, ZeroTokenContextFlagsException
)

class TokenContextValidator(Validator[TokenContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a TokenContext instance is certified safe, reliable and consistent before use.
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
            rank_service: RankService = RankService(),
            team_service: TeamService = TeamService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
            number_validator: NotNegativeNumberValidator = NotNegativeNumberValidator(),
    ) -> ValidationResult[TokenContext]:
        """
        # ACTION:
            1.  If the candidate fails existence or type tests send the exception in the ValidationResult.
                Else, cast to TeamContext instance context.
            2.  If one-and-only-one context attribute is not null return an exception in the ValidationResult.
            3.  If there is no certification route for the attribute return an exception in the ValidationResult.
            4.  If the certification route exists use the appropriate service or validator to send either an exception
                chain the ValidationResult or the context.
        # PARAMETERS:
            *   candidate (Any)
            *   rank_service (RankService)
            *   team_service (TeamService)
            *   coord_service (CoordService)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)
            *   number_validator (NotNegativeNumberValidator)
        # RETURNS:
            *   ValidationResult[TeamContext] containing either:
                    - On failure: Exception.
                    - On success: TeamContext in the payload.
        # RAISES:
            *   TypeError
            *   NullTeamContextException
            *   ZeroTeamContextFlagsException
            *   ExcessiveTeamContextFlagsException
            *   TeamContextValidationFailedException
            *   TeamContextValidationRouteException
        """
        method = "TokenContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationFailedException(
                    message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                    ex=NullTokenContextException(f"{method}: {NullTokenContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, TokenContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationFailedException(
                    message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected TokenContext, got {type(candidate).__designation__} instead.")
                )
            )
        # After existence and type checks cast the candidate to a TeamContext for additional tests.
        context = cast(TokenContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        if len(context.to_dict()) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationFailedException(
                    message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                    ex=ZeroTokenContextFlagsException(f"{method}: {ZeroTokenContextFlagsException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if len(context.to_dict()) > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationFailedException(
                    message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                    ex=ExcessiveTokenContextFlagsException(
                        f"{method}: {ExcessiveTokenContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation = identity_service.validate_id(candidate=context.id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationFailedException(
                        message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_TokenContext in the ValidationResult.
            return ValidationResult.success(context)
        
        # Certification for the search-by-designation target.
        if context.designation is not None:
            validation = identity_service.validate_name(candidate=context.designation)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationFailedException(
                        message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the designation_TokenContext in the ValidationResult.
            return ValidationResult.success(context)
        
        # Certification for the search-by-coord target.
        if context.coord is not None:
            validation = coord_service.validator.validate(candidate=candidate)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationFailedException(
                        message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the coord_TokenContext in the ValidationResult.
            return ValidationResult.success(context)
        
        # Certification for the search-by-team target.
        if context.team is not None:
            validation = team_service.validator.validate(candidate=candidate)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationFailedException(
                        message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the team_TokenContext in the ValidationResult.
            return ValidationResult.success(context)
        
        # Certification for the search-by-rank target.
        if context.rank is not None:
            validation = rank_service.validator.validate(candidate=candidate)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationFailedException(
                        message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the rank_TokenContext in the ValidationResult.
            return ValidationResult.success(context)
        
        # Certification for the search-by-color target.
        if context.color is not None:
            validation = color_validator.validate(candidate=candidate)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidationFailedException(
                        message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the color_TokenContext in the ValidationResult.
            return ValidationResult.success(context)
        
        # Certification for the search-by-ransom target.
        if context.ransom is not None:
            validation = number_validator.validate(candidate=candidate)
            # Return the exception chain on failure.
            if validation.is_failure:
                return ValidationResult.failure(
                    TokenContextValidationFailedException(
                        message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the ransom_TokenContext in the ValidationResult.
            return ValidationResult.success(context)
        
        # Return the exception chain if there was no validation route for the context.
        return ValidationResult.failure(
            TokenContextValidationFailedException(
                message=f"{method}: {TokenContextValidationFailedException.ERROR_CODE}",
                ex=TokenContextValidationRouteException(
                    f"{method}: {TokenContextValidationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )
        
    
