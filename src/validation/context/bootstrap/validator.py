# src/validation/context/bootstrap/operation.py

"""
Module: validation.context.bootstrap.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import ContextNullException, ContextValidationException, ZeroContextFlagsException
from model import Context
from result import ValidationResult
from util import LoggingLevelRouter
from validation import Validator, ValidatorBootstrapper


class BootstrapContextValidator(Validator[Context]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a BootstrapContext instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    rank: Any,
                    workers: BootstrapContextIntegrityWorkers,
            ) -> BuildResult[Context]:

    Super Class:
        Validator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            target_context_model: Context,
            null_exception: ContextNullException,
            validator_bootstrapper: ValidatorBootstrapper | None = None,
    ) -> ValidationResult[Context]:
        """
        Certify a rank is a BootstrapContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The rank is null.
                    -   The rank is not a BootstrapContext.
                    -   It has no attributes enabled.
                    -   It has more than one attribute enabled.
                    -   The enabled attribute fails a safety check.
                    -   There is no validation path for the attribute.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            workers: BootstrapContextIntegrityWorkers
        Returns:
            ValiationResult[Context]
        Raises:
            TypeError
            NullBootstrapContextException
            ZeroBootstrapContextFlagsException
            BootstrapContextValidationException
            ExcessBootstrapContextFlagsException
            TeamContextValidationRouteException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if validator_bootstrapper is None:
            validator_bootstrapper = ValidatorBootstrapper()
        
        # Handle the case that, either the null or type check fails.
        validation_bootstrap_result = validator_bootstrapper.validate(
            candidate=candidate,
            target_model=target_context_model,
            null_exception=null_exception,
        )
        if validation_bootstrap_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ContextValidationException.MSG,
                    err_code=ContextValidationException.ERR_CODE,
                    ex=validation_bootstrap_result.exception,
                )
            )
        # --- Cast the candidate into the targeted Context subclass for additional tests. ---#
        context = cast(target_context_model, candidate)

        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ContextValidationException.MSG,
                    err_code=ContextValidationException.ERR_CODE,
                    ex=ZeroContextFlagsException(
                        msg=f"{target_context_model.__class__.__name__} does not have any flags enabled.",
                        err_code=ZeroContextFlagsException.ERR_CODE,
                        var=target_context_model.__class__.__name__
                    ),
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ContextValidationException.MSG,
                    err_code=ContextValidationException.ERR_CODE,
                    ex=ZeroContextFlagsException(
                        msg=f"{target_context_model.__class__.__name__} has more than one flag enabled.",
                        err_code=ZeroContextFlagsException.ERR_CODE,
                        var=target_context_model.__class__.__name__
                    ),
                )
            )
        
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(context)
    
