# src/validation/context/square/validator.py

"""
Module: validation.context.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from model import Formation, SquareContext, SquareState
from result import ValidationResult
from toolkit import SquareContextToolkit
from util import LoggingLevelRouter
from validation import ContextValidator
from err import (
    FormationNullException, SquareContextValidationException, SquareContextValidationRouteException,
    SquareStateNullException
)



class SquareContextValidator(ContextValidator[Square]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a SquareContext instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    toolkit: SquareContextToolkit,
            ) -> ValidationResult[Square]:

    Super Class:
        ContextValidator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: SquareContextToolkit | None = None,
    ) -> ValidationResult[Square]:
        """
        Certify a candidate is a SquareContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Validation is not primed.
                    -   The enabled attribute fails a safety check.
                    -   There is no validation path for the attribute.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            toolkit: SquareContextToolkit,
        Returns:
            ValidationResult[Square]
        Raises:
            SquareContextValidationException
            SquareContextValidationRouteException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = SquareContextToolkit()
        
        # handle the case that, priming the validator fails.
        priming_result = toolkit.context_validation_primer.build(
            candidate=candidate,
            context_model=toolkit.context_model_type,
            context_null_exception=toolkit.null_context_exception,
            validation_primer=toolkit.square_toolkit.validation_primer
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareContextValidationException.MSG,
                    err_code=SquareContextValidationException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into SquareContext for routing attribute testing. ---#
        context = cast(SquareContext, candidate)
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation_result = toolkit.square_toolkit.identity_service.validate_id(
                candidate=context.id
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareContextValidationException.MSG,
                        err_code=SquareContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-schema target.
        if context.name is not None:
            validation_result = toolkit.square_toolkit.identity_service.validate_name(
                candidate=context.name
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareContextValidationException.MSG,
                        err_code=SquareContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-coord target.
        if context.coord is not None:
            validation_result = toolkit.square_toolkit.coord_validator.validate(
                candidate=context.coord
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareContextValidationException.MSG,
                        err_code=SquareContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-board target.
        if context.board is not None:
            validation_result = toolkit.square_toolkit.board_validator.validate(
                candidate=context.board
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareContextValidationException.MSG,
                        err_code=SquareContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-occupant target.
        if context.occupant is not None:
            validation_result = toolkit.square_toolkit.token_validator.validate(
                candidate=context.occupant
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareContextValidationException.MSG,
                        err_code=SquareContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-state.
        if context.state is not None:
            validation_result = toolkit.square_toolkit.validation_primer.validate(
                candidate=context.state,
                model_type=SquareState,
                null_exception=SquareStateNullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareContextValidationException.MSG,
                        err_code=SquareContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-formation.
        if context.formation is not None:
            validation_result = toolkit.square_toolkit.validation_primer.validate(
                candidate=context.formation,
                model_type=Formation,
                null_exception=FormationNullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareContextValidationException.MSG,
                        err_code=SquareContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            SquareContextValidationException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=SquareContextValidationException.MSG,
                err_code=SquareContextValidationException.ERR_CODE,
                ex=SquareContextValidationRouteException(
                    msg=SquareContextValidationRouteException.MSG,
                    err_code=SquareContextValidationRouteException.ERR_CODE,
                )
            )
        )

