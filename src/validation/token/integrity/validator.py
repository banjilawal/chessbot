# src/validation/token/integrity/validator.py

"""
Module: validation.token.integrity.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from controller import WorkerRegistryController
from factory import ToolkitFactory
from model import CombatantToken, KingToken, Token
from operation import Validator
from toolkit import TokenToolkit
from database import CoordDatabase
from result import BuildResult, ValidationResult
from util import LoggingLevelRouter
from err import CoordDatabaseNullException, TokenNullException, TokenValidationException


class TokenIntegrityValidator(Validator[Token]):
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
    OPERATION_NAME = "token_validator"
    
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
        
        toolkit_build_result = cls._get_toolkit(toolkit=toolkit)
        if toolkit_build_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=toolkit_build_result.exception,
                )
            )
        tools = toolkit_build_result.payload
        
        # Handle the case that, the candidate does not exist.
        validation_priming_result = tools["validation_primer"].build(
            candidate=candidate,
            target_model=Token,
            context_null_exception=TokenNullException(),
        )
        if validation_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=validation_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Token for additional tests ---#
        token = cast(Token, candidate)
        
        # Handle the case that, id or designation are not certified safe.
        identity_validation_result = tools["identity_service"].validate_identity(
            id_candidate=token.id,
            name_candidate=token.designation
        )
        if identity_validation_result.is_failure:
            # Send the exception chain on failure.
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
        team_validation_result = tools["team_validator"].build(token.team)
        if team_validation_result.is_failure:
            # Send the exception chain on failure.
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
        opening_square_validation_result = toolkit["square_validator"].build(token.opening_square)
        if opening_square_validation_result.is_failure:
            # Send the exception chain on failure.
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
        rank_validation_result = tools["rank_service.validator"].build(rank=token.rank)
        if rank_validation_result.is_failure:
            # Send the exception chain on failure.
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
        coord_database_validation_result = tools["validation_primer"].build(
            candidate=token.positions,
            target_model=CoordDatabase,
            context_null_exception=CoordDatabaseNullException()
        )
        if coord_database_validation_result.is_failure:
            # Send the exception chain on failure.
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
    def _get_toolkit(cls, toolkit: TokenToolkit) -> BuildResult[TokenToolkit]:
        method = f"{cls.__name__}._get_toolkit"
        
        build_result = ToolkitFactory.build_toolkit(toolkit_class=TokenToolkit,)
        if build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidationException.MSG,
                    err_code=TokenValidationException.ERR_CODE,
                    ex=build_result.exception,
                )
            )
        return BuildResult.success(build_result.payload)

    


# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=TokenIntegrityValidator)