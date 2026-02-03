# src/chess/token/validator/validator.py

"""
Module: chess.token.validator
Author: Banji Lawal
Created: 2025-10-22
Version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast


from chess.rank import RankService
from chess.team import Team, TeamService
from chess.coord import CoordStackService, CoordService
from chess.token import CombatantToken, KingToken, NullTokenException, Token, TokenValidationFailedException
from chess.system import (
    NumberValidator, IdentityService, LoggingLevelRouter, ServiceValidator, ValidationResult, Validator
)

class TokenValidator(Validator[Token]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Token instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
        * TokenValidator

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
            team_service: TeamService = TeamService(),
            rank_service: RankService = RankService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            service_validator: ServiceValidator = ServiceValidator(),
            number_validation: NumberValidator = NumberValidator(),
    ) -> ValidationResult[Token]:
        """
        # ACTION:
            1.  If the candidate fails existence or type tests send the exception in the ValidationResult.
                Else, cast to Token instance occupant.
            2.  If any of the attributes; id, designation, roster_number, rank or positions fail their validation
                tests send the exception in the ValidationResult.
            3.  The occupant has passed all verification tests. Send the occupant in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   rank_service (RankService)
            *   team_service (TeamService)
            *   coord_service (CoordService)
            *   identity_service (IdentityService)
            *   number_validator (NumberValidator)
        # RETURNS:
            *   ValidationResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        # RAISES:
            *   TypeError
            *   NullTeamException
            *   TeamValidationFailedException
        """
        method = "Token.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullTokenException(f"{method}: {NullTokenException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Token):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}:Expected Token, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate to a Token for additional tests ---#
        token = cast(Token, candidate)
        
        # Handle the case that id or designation are not certified safe.
        identity_validation = identity_service.validate_identity(
            id_candidate=token.id,
            name_candidate=token.designation
        )
        if identity_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=identity_validation.exception
                )
            )
        # Handle the case that the occupant's team fails validation.
        team_validation = team_service.item_validator.validate(token.team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=team_validation.exception
                )
            )
        # Handle the case that the Token's roster or opening_square  fail validation and in the allowed range.
        roster_and_square_validation = identity_service.validate_identity(
            id_candidate=token.roster_number,
            name_candidate=token.opening_square
        )
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=roster_and_square_validation.exception
                )
            )
        # Handle the case that the rank is not certified safe.
        rank_validation = rank_service.validator.validate(candidate=token.rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=rank_validation.exception
                )
            )
        # Handle the case that occupant.positions fails its validation.
        service_validation = service_validator.validate(candidate=token.positions, expected_type=CoordStackService)
        if service_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=service_validation.exception
                )
            )
        # Tests have been passed return the occupant in the ValidationResult.
        return ValidationResult.success(payload=token)
    
    @classmethod
    def verify_token_is_combatant(cls, candidate: Any) -> ValidationResult[CombatantToken]:
        method = "TokenValidator.validate_token_is_combatant"
        # Handle the case that the candidate is not certified as a safe occupant.
        validation = cls.validate(candidate)
        if validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=validation.exception
                )
            )
        # Handle the case that the candidate is not a CombatantToken.
        if not isinstance(candidate, CombatantToken):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}:Expected CombatantToken, got {type(candidate).__name__} instead.")
                )
            )
        # Tests have been passed return cast the candidate to CombatantToken and return to the caller.
        return ValidationResult.success(payload=cast(CombatantToken, candidate))
        
    @classmethod
    def verify_token_is_king(cls, candidate: Any) -> ValidationResult[KingToken]:
        method = "TokenValidator.validate_token_is_king"
        # Handle the case that the candidate is not certified as a safe occupant.
        validation = cls.validate(candidate)
        if validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=validation.exception
                )
            )
        # Handle the case that the candidate is not a KingToken.
        if not isinstance(candidate, KingToken):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}:Expected KingToken, got {type(candidate).__name__} instead.")
                )
            )
        # Tests have been passed return cast the candidate to CombatantToken and return to the caller.
        return ValidationResult.success(payload=cast(CombatantToken, candidate))