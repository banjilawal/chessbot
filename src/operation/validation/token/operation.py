# src/operation/validation/token/operation.py

"""
Module: operation.validation.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from database import CoordDatabase
from err import CoordDatabaseNullException, TokenNullException, TokenValidationException
from model import Token
from operation import Validator
from result import ValidationResult
from system import LoggingLevelRouter
from toolkit import TokenToolkit


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
        -   def validate(candidate: Any, toolkit: TokenToolkit) -> ValidationResult[Token]:

    Super Class:
        Validator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: TokenToolkit | None = None,
    ) -> ValidationResult[Token]:
        """
        Verify the object is a Token that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null
                    -   It's not a number.
                    _   A Team check fails
                    -   A Rank check fails
                    -   Identity check fails
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: TokenToolkit
        Returns:
            ValidationResult[Token]
        Raises:
             TokenValidationException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = TokenToolkit()
        
        # Handle the case that, the candidate does not exist.
        validation_bootstrap_result = toolkit.validation_bootstrapper.validate(
            candidate=candidate,
            target_model=Token,
            null_exception=TokenNullException(),
        )
        if validation_bootstrap_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=validation_bootstrap_result.exception,
                )
            )
        # --- Cast the rank to a Token for additional tests ---#
        token = cast(Token, candidate)
        
        # Handle the case that, id or designation are not certified safe.
        identity_validation_result = toolkit.identity_service.validate_identity(
            id_candidate=token.id,
            name_candidate=token.designation
        )
        if identity_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=identity_validation_result.exception,
                )
            )
        # Handle the case that, the occupant's team fails validation.
        team_validation_result = toolkit.team_validator.validate(token.team)
        if team_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=team_validation_result.exception,
                )
            )
        # Handle the case that, the roster or opening_square_name are not acceptable.
        opening_square_validation_result = toolkit.square_validator.validate(token.opening_square)
        if opening_square_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=opening_square_validation_result.exception,
                )
            )
        # Handle the case that, the rank is not safe.
        rank_validation_result = toolkit.rank_service.validator.validate(rank=token.rank)
        if rank_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=rank_validation_result.exception,
                )
            )
        # Handle the case that the token's CoordDatabase fails it safety checks.
        coord_database_validation_result = toolkit.validation_bootstrapper.validate(
            candidate=token.positions,
            target_model=CoordDatabase,
            null_exception=CoordDatabaseNullException()
        )
        if coord_database_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=coord_database_validation_result,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(token)

    
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
                    cls_mthd=method,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, the rank is not a CombatantToken.
        if not isinstance(candidate, CombatantToken):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
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