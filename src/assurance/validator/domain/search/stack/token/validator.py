# src/assurance/validator/domain/search/stack/token/checker.py

"""
Module: assurance.validator.domain.search.stack.token.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from assurance import ContextValidator, TokenValidationBundle
from config import GameColor
from domain import Persona, TokenSearchContext
from artifcat import ValidationResult
from err import (
    ExcessTokenContextFlagsException, GameColorNullException, TokenContextCheckerException,
    TokenContextValidationRouteException,
    ZeroTokenContextFlagsException
)
from util import LoggingLevelRouter


class TokenContextValidator(ContextValidator[TokenSearchContext]):
    """
    Role
        -  Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null TokenContext.
        2.  Run safety checks on any TokenContext attributes that are enabled.

    Attributes:
        bundle: TokenValidationBundle

    Provides:
        - def execute(candidate: Any) -> ValidationResult[TokenContext]:

    Super Class:
        StackContextChecker
    """
    
    def __init__(self, bundle: Optional[TokenValidationBundle] | None = None, ):
        super().__init__(bundle=bundle or TokenValidationBundle())
    
    
    @property
    def bundle(self) -> TokenValidationBundle:
        return cast(TokenValidationBundle, super().bundle)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TokenSearchContext]:
        """
        Certify a candidate is a TokenContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -  The candidate is not a TokenContext.
                    -  The wrong number of search attributes is enabled.
                    -  An enabled search attribute fails a safety check.
            2.  Otherwise, send a TokeContext in the success result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[TokenContext]
        Raises:
            TokenContextCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is null or the wrong type.
        priming = self.bundle.priming_validator.execute(
            candidate=candidate,
            target_model=self.bundle.types.search_context,
            null_exception=self.bundle.nulls.search_context
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextCheckerException.MSG,
                    err_code=TokenContextCheckerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate into TokenContext for routing attribute testing ---#
        context = cast(TokenSearchContext, priming.payload)
        
        # Handle the case that, no flags are enabled.
        if context.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextCheckerException.MSG,
                    err_code=TokenContextCheckerException.ERR_CODE,
                    ex=ZeroTokenContextFlagsException(
                        cls_mthd = method,
                        cls_name = self.__class__.__name__,
                        msg=ZeroTokenContextFlagsException.MSG,
                        err_code=ZeroTokenContextFlagsException.ERR_CODE
                    )
                )
            )
        # Handle the case that too many context flags are enabled.
        if context.is_above_max_size:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextCheckerException.MSG,
                    err_code=TokenContextCheckerException.ERR_CODE,
                    ex=ExcessTokenContextFlagsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ExcessTokenContextFlagsException.MSG,
                        err_code=ExcessTokenContextFlagsException.ERR_CODE
                    )
                )
            )
            
        # Certification for the search-by-id target.
        if context.id is not None:
            validation = self.bundle.identity_service.validate_id(
                candidate=context.id
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenContextCheckerException.MSG,
                        err_code=TokenContextCheckerException.ERR_CODE,
                        ex=validation.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-designation target.
        if context.name is not None:
            validation = self.bundle.identity_service.validate_name(
                candidate=context.name
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenContextCheckerException.MSG,
                        err_code=TokenContextCheckerException.ERR_CODE,
                        ex=validation.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-home_square target.
        if context.home_square is not None:
            validation = self.bundle.square_validator.execute(
                candidate=context.home_square
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenContextCheckerException.MSG,
                        err_code=TokenContextCheckerException.ERR_CODE,
                        ex=validation.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-coord target.
        if context.current_position is not None:
            validation = self.bundle.coord_validator.execute(
                candidate=context.current_position
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenContextCheckerException.MSG,
                        err_code=TokenContextCheckerException.ERR_CODE,
                        ex=validation.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-team target.
        if context.team is not None:
            validation = self.bundle.team_validator.execute(
                candidate=context.current_position
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenContextCheckerException.MSG,
                        err_code=TokenContextCheckerException.ERR_CODE,
                        ex=validation.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-rank target.
        if context.rank is not None:
            validation = self.bundle.rank_service.validator.execute(
                candidate=context.rank
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenContextCheckerException.MSG,
                        err_code=TokenContextCheckerException.ERR_CODE,
                        ex=validation.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-color target.
        if context.team_color is not None:
            validation = self.priming_validator.execute(
                candidate=context.team_color,
                model_type=GameColor,
                null_exception=GameColorNullException()
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenContextCheckerException.MSG,
                        err_code=TokenContextCheckerException.ERR_CODE,
                        ex=validation.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-ransom target.
        if context.ransom is not None:
            validation = self.bundle.number_validator.execute(
                candidate=context.ransom,
                floor=Persona.KING.ransom,
                ceiling=Persona.QUEEN.ransom,
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenContextCheckerException.MSG,
                        err_code=TokenContextCheckerException.ERR_CODE,
                        ex=validation.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Handle the case that, there is no validation logic for the attribute.
        return ValidationResult.failure(
            TokenContextCheckerException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=TokenContextCheckerException.MSG,
                err_code=TokenContextCheckerException.ERR_CODE,
                ex=TokenContextValidationRouteException(
                    msg=TokenContextValidationRouteException.MSG,
                    err_code=TokenContextValidationRouteException.ERR_CODE,
                )
            )
        )