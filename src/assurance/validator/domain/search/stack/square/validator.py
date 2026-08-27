# src/assurance/validator/domain/search/stack/square/checker.py

"""
Module: assurance.validator.domain.search.stack.square.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import SquareValidationBundle, StackContextValidator
from domain import SquareSearchSearchContext
from err import (
    ExcessSquareContextFlagsException, SquareContextCheckerException, SquareContextValidationRouteException,
    ZeroSquareContextFlagsException
)
from util import LoggingLevelRouter


class SquareContextValidator(StackContextValidator[SquareSearchSearchContext]):
    """
    Role
        -  Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null SquareSearchContext.
        2.  Run safety checks on any SquareSearchContext attributes that are enabled.

    Attributes:
        bundle: SquareValidationBundle

    Provides:
        - def execute(candidate: Any) -> ValidationResult[SquareSearchContext]:

    Super Class:
        StackSearchContextChecker
    """
    
    def __init__(self, bundle: Optional[SquareValidationBundle] | None = None, ):
        super().__init__(bundle=bundle or SquareValidationBundle())
    
    
    @property
    def bundle(self) -> SquareValidationBundle:
        return cast(SquareValidationBundle, super().bundle)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SquareSearchSearchContext]:
        """
        Certify a candidate is a SquareSearchContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -  The candidate is not a SquareSearchContext.
                    -  The wrong number of search attributes is enabled.
                    -  An enabled search attribute fails a safety check.
            2.  Otherwise, send a TokeSearchContext in the success result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[SquareSearchContext]
        Raises:
            SquareContextCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the validator is not primed.
        priming = self.bundle.priming_validator.execute(
            candidate=candidate,
            target_model=self.bundle.types.search_context,
            null_exception=self.bundle.nulls.search_context,
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextCheckerException.MSG,
                    err_code=SquareContextCheckerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate into SquareContext for routing attribute testing ---#
        context = cast(SquareSearchSearchContext, priming.payload)
        
        # Handle the case that, no flags are enabled.
        if context.has_no_active_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextCheckerException.MSG,
                    err_code=SquareContextCheckerException.ERR_CODE,
                    ex=ZeroSquareContextFlagsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ZeroSquareContextFlagsException.MSG,
                        err_code=ZeroSquareContextFlagsException.ERR_CODE
                    )
                )
            )
        # Handle the case that too many context flags are enabled.
        if context.has_excessive_active_contexts:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextCheckerException.MSG,
                    err_code=SquareContextCheckerException.ERR_CODE,
                    ex=ExcessSquareContextFlagsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ExcessSquareContextFlagsException.MSG,
                        err_code=ExcessSquareContextFlagsException.ERR_CODE
                    )
                )
            )
        # --- Route to the appropriate validation path. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation_result = self.bundle.identity_service.validate_id(
                candidate=context.id
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareContextCheckerException.MSG,
                        err_code=SquareContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-schema target.
        if context.name is not None:
            validation_result = self.bundle.identity_service.validate_name(
                candidate=context.name
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareContextCheckerException.MSG,
                        err_code=SquareContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-coord target.
        if context.coord is not None:
            validation_result = self.bundle.coord_validator.execute(
                candidate=context.coord
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareContextCheckerException.MSG,
                        err_code=SquareContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-board target.
        if context.board is not None:
            validation_result = self.bundle.board_validator.execute(
                candidate=context.board
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareContextCheckerException.MSG,
                        err_code=SquareContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-occupant target.
        if context.occupant is not None:
            validation_result = self.bundle.token_validator.execute(
                candidate=context.occupant
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareContextCheckerException.MSG,
                        err_code=SquareContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-state.
        if context.state is not None:
            validation_result = self.bundle.priming_validator.execute(
                candidate=context.state,
                model_type=SquareState,
                null_exception=SquareStateNullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareContextCheckerException.MSG,
                        err_code=SquareContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-formation.
        if context.home_square_type is not None:
            validation_result = self.bundle.priming_validator.execute(
                candidate=context.home_square_type,
                model_type=bool,
                null_exception=NullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareContextCheckerException.MSG,
                        err_code=SquareContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            SquareContextCheckerException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=SquareContextCheckerException.MSG,
                err_code=SquareContextCheckerException.ERR_CODE,
                ex=SquareContextValidationRouteException(
                    msg=SquareContextValidationRouteException.MSG,
                    err_code=SquareContextValidationRouteException.ERR_CODE,
                )
            )
        )

