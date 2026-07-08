# src/validator/context/token/validator.py

"""
Module: validator.context.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from model import Persona, TokenContext
from result import ValidationResult
from setting import GameColor
from toolkit import TokenToolkit
from util import LoggingLevelRouter
from validator import ContextValidator, PrimingValidator
from err import (
    GameColorNullException, TokenContextNullException, TokenContextValidatorException,
    TokenContextValidationRouteException
)


class TokenContextValidator(ContextValidator):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a TokenContext instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    toolkit: TokenToolkit,
            ) -> ValidationResult[Token]:

    Super Class:
        ContextValidator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            toolkit: TokenToolkit | None = None,
    ) -> ValidationResult[TokenContext]:
        """
        Certify a candidate is a TokenContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Validation is not primed.
                    -   The enabled attribute fails a safety check.
                    -   There is no validation path for the attribute.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            toolkit: TokenToolkit,
        Returns:
            ValidationResult[Token]
        Raises:
            TokenContextValidatorException
            TokenContextValidationRouteException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenToolkit()
        
        # Handle the case that, the validator is not primed.
        priming_result = toolkit.priming_validator.execute(
            candidate=candidate,
            context_model=candidate,
            context_null_exception=TokenContext,
            priming_validator=TokenContextNullException()
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenContextValidatorException.MSG,
                    err_code=TokenContextValidatorException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into TokenContext for routing attribute testing ---#
        context = cast(TokenContext, candidate)
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation_result = toolkit.identity_service.validate_id(
                candidate=context.id
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenContextValidatorException.MSG,
                        err_code=TokenContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-designation target.
        if context.designation is not None:
            validation_result = toolkit.identity_service.validate_name(
                candidate=context.designation
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenContextValidatorException.MSG,
                        err_code=TokenContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-home_square target.
        if context.home_square is not None:
            validation_result = toolkit.square_validator.execute(
                candidate=context.home_square
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenContextValidatorException.MSG,
                        err_code=TokenContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-coord target.
        if context.current_position is not None:
            validation_result = toolkit.coord_validator.execute(
                candidate=context.current_position
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenContextValidatorException.MSG,
                        err_code=TokenContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
    
        # Certification for the search-by-team target.
        if context.team is not None:
            validation_result = toolkit.team_validator.execute(
                candidate=context.current_position
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenContextValidatorException.MSG,
                        err_code=TokenContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-rank target.
        if context.rank_level is not None:
            validation_result = toolkit.rank_service.validator.execute(
                candidate=context.rank_level
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenContextValidatorException.MSG,
                        err_code=TokenContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-color target.
        if context.color is not None:
            validation_result = toolkit.priming_validator.execute(
                candidate=context.color,
                model_type=GameColor,
                null_exception=GameColorNullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenContextValidatorException.MSG,
                        err_code=TokenContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-ransom target.
        if context.ransom is not None:
            validation_result = toolkit.number_validator.execute(
                candidate=context.ransom,
                floor=Persona.KING.ransom,
                ceiling=Persona.QUEEN.ransom,
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenContextValidatorException.MSG,
                        err_code=TokenContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Handle the case that, there is no validation logic for the attribute.
        return ValidationResult.failure(
            TokenContextValidatorException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=TokenContextValidatorException.MSG,
                err_code=TokenContextValidatorException.ERR_CODE,
                ex=TokenContextValidationRouteException(
                    msg=TokenContextValidationRouteException.MSG,
                    err_code=TokenContextValidationRouteException.ERR_CODE,
                )
            )
        )
        
    
