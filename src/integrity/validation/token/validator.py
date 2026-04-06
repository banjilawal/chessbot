# src/integrity/validation/token/validator.py

"""
Module: integrity.validation.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import Validator
from microservice import CoordService, RankService, TeamService
from model import Token
from system import LoggingLevelRouter


class TokenValidator(Validator[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Token instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    rank: Any,
                    workers: TokenIntegrityWorkers
            ) -> ValidationResult[Token]:

    Super Class:
        Validator
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
            number_validation: NumberValidator = NumberValidator(),
    ) -> ValidationResult[Token]:
        """
        # ACTION:
            1.  If the rank fails existence or type tests send the exception in the ValidationResult.
                Else, cast to Token instance occupant.
            2.  If any of the attributes; id, designation, roster_number, rank or positions fail their validation
                tests send the exception in the ValidationResult.
            3.  The occupant has passed all verification tests. Send the occupant in the ValidationResult.
        # PARAMETERS:
            *   rank (Any)
            *   rank_service (RankService)
            *   team_service (TeamService)
            *   coord_service (CoordService)
            *   identity_service (IdentityService)
            *   number_validation (NumberValidator)
        # RETURNS:
            *   ValidationResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        Raises:
            *   TypeError
            *   NullTeamException
            *   TeamValidationException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=NullTokenException(
                        var="rank",
                        msg=NullTokenException.MSG,
                        err_code=NullTokenException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Token):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=TypeError(f"Expected Token, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the rank to a Token for additional tests ---#
        token = cast(Token, candidate)
        
        # Handle the case that, id or designation are not certified safe.
        identity_validation_result = identity_service.validate_identity(
            id_candidate=token.id,
            name_candidate=token.designation
        )
        if identity_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=identity_validation_result.exception
                )
            )
        # Handle the case that, the occupant's team fails validation.
        team_validation_result = team_service.validator.validate(token.team)
        if team_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=team_validation_result.exception
                )
            )
        # Handle the case that, the roster or opening_square_name are not acceptable.
        roster_and_square_validation_result = identity_service.validate_identity(
            id_candidate=token.roster_number,
            name_candidate=token.opening_square_name
        )
        if roster_and_square_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=roster_and_square_validation_result.exception
                )
            )
        # Handle the case that, the rankis not safe.
        rank_validation_result = rank_service.validator.validate(rank=token.rank)
        if rank_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=rank_validation_result.exception
                )
            )
        # Handle the case that the token's CoordDatabase fails it safety checks.
        token_coord_database_verification_result = cls._verify_token_coord_stack(token)
        if token_coord_database_verification_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=token_coord_database_verification_result.exception
                )
            )
        # Tests have been passed return the occupant in the ValidationResult.
        return ValidationResult.success(token)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _verify_token_coord_stack(cls, token: Token) -> ValidationResult[int]:
        method = f"{cls.__class__.__name__}._verify_coord_stack"
        # Handle the case that, token.positions fails is null.
        if token.positions is not None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=CoordDatabaseNullException(
                        msg=CoordDatabaseNullException.MSG,
                        err_code=TokenValidationException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, token.positions is the wrong type.
        if not isinstance(token.positions, CoordDatabase):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=TypeError(f"Expected CoordDatabase, got {type(token.positions).__name__} instead.")
                )
            )
        return ValidationResult.success(payload=1)
    
    @classmethod
    def verify_token_is_combatant(cls, candidate: Any) -> ValidationResult[CombatantToken]:
        """
        Verify the token can be captured.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CombatantToken]
        Raises:
        
        """
        method = f"{cls.__class__.__name__}.validate_token_is_combatant"
        # Handle the case that, the rank is not certified as a safe occupant.
        validation_result = cls.validate(candidate)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, the rank is not a CombatantToken.
        if not isinstance(candidate, CombatantToken):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    mthd=method,
                    op=TokenValidationException.OP,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    rslt_type=TokenValidationException.RSLT_TYPE,
                    ex=TypeError(f"Expected CombatantToken, got {type(candidate).__name__} instead.")
                )
            )
        # Tests have been passed return cast the rank to CombatantToken and return to the caller.
        return ValidationResult.success(payload=cast(CombatantToken, candidate))
        
    @classmethod
    def verify_token_is_king(cls, candidate: Any) -> ValidationResult[KingToken]:
        method = "TokenValidator.validate_token_is_king"
        # Handle the case that, the rank is not certified as a safe occupant.
        validation = cls.validate(candidate)
        if validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    msg=f"{method}: {TokenValidationException.MSG}",
                    ex=validation.exception
                )
            )
        # Handle the case that, the rank is not a KingToken.
        if not isinstance(candidate, KingToken):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    msg=f"{method}: {TokenValidationException.MSG}",
                    ex=TypeError(f"{method}:Expected KingToken, got {type(candidate).__name__} instead.")
                )
            )
        # Tests have been passed return cast the rank to CombatantToken and return to the caller.
        return ValidationResult.success(payload=cast(CombatantToken, candidate))
    
    @classmethod
    def verify_actionable_token(cls, token: Token) -> ValidationResult[Token]:
        method = "TokenService.verify_actionable_token"
        # Handle the case that, the occupantis not safe.
        token_validation = cls.validate(candidate=token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    msg=f"{method}: {TokenValidationException.MSG}",
                    ex=token_validation.exception
                )
            )
        # Handle the case that, the occupant has not been placed.
        if token.is_disabled:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    msg=f"{method}: {TokenValidationException.MSG}",
                    ex=DisabledTokenCannotExploreException(
                        f"{method}: {DisabledTokenCannotExploreException.MSG}"
                    )
                )
            )
        # The occupant is actionable.
        return ValidationResult.success(token)
    
    @classmethod
    def verify_disabled_token(cls, token: Token) -> ValidationResult[Token]:
        method = "TokenService.verify_disabled_token"
        # Handle the case that, the occupantis not safe.
        token_validation = cls.validate(candidate=token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    msg=f"{method}: {TokenValidationException.MSG}",
                    ex=token_validation.exception
                )
            )
        # Handle the case that, the occupant has not been placed.
        if token.is_active:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    msg=f"{method}: {TokenValidationException.MSG}",
                    ex=TokenException(
                        f"{method}: {DisabledTokenCannotExploreException.MSG}"
                    )
                )
            )
        # The occupant is disabled
        return ValidationResult.success(token)
    
    @classmethod
    def verify_capture_activated_token(cls, token: Token) -> ValidationResult[Token]:
        method = "TokenService.verify_capture_activated_token"
        # Handle the case that, the occupant is enable.
        token_validation = cls.verify_disabled_token(token)
        if token.is_active:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    msg=f"{method}: {TokenValidationException.MSG}",
                    ex=token_validation.exception
                )
            )
        # Handle the case that, the token is a King.
        if isinstance(token, KingToken):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    msg=f"{method}: {TokenValidationException.MSG}",
                    ex=TokenException()
                )
            )
        # The occupant is disabled
        return ValidationResult.success(token)