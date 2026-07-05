# src/validation/path/validator.py

"""
Module: validation.path.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import CircularPathException, PathValidatorException
from model import Path
from result import ValidationResult
from toolkit import PathToolkit
from util import LoggingLevelRouter


class PathValidator:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Path instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validator(
                    cls,
                    candidate,
                    identity_service: IdentityService,
                    square_validator: SquareValidator,
                    priming_validator: PrimingValidator,
            ) -> ValidationResult[Path]

    Super Class:
        Validator
    """
    OPERATION_NAME = "path_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: PathToolkit | None = None,
    ) -> ValidationResult[Path]:
        """
        Verify the object is a Path that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null
                    -   It's not a Path.
                    _   An id check fails.
                    -   Either the origin or destination are not safe square.
                    -   The origin and destination are the same.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: PathToolkit
        Returns:
            ValidationResult[Path]
        Raises:
             PathValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = PathToolkit()
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = toolkit.priming_validator.validate(
            candidate=candidate,
            target_model=toolkit.model,
            null_exception=toolkit.null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Path for additional tests. ---#
        path = cast(Path, candidate)
        
        # Handle the case that, the path's id gets flagged.
        id_validation = toolkit.identity_service.validate_id(path.id)
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that either the source or destination are not safe.
        for square in [path.origin, path.destination]:
            square_validation_result = toolkit.square_validator.validate(square)
            if square_validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PathValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PathValidatorException.MSG,
                        err_code=PathValidatorException.ERR_CODE,
                        ex=square_validation_result.exception,
                    )
                )
        # Handle the case that, the origin and the destination are the same.
        if path.origin == path.destination:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=CircularPathException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=CircularPathException.MSG,
                        err_code=CircularPathException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(path)
        
        
