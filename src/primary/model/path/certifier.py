# src/validator/model/path/validator.py

"""
Module: validator.model.path.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional, cast

from err import CircularPathException, PathValidatorException
from model import Path
from primary import ModelRootCertifier
from result import ValidationResult
from toolkit import PathToolkit
from util import LoggingLevelRouter


class PathRootCertifier(ModelRootCertifier[Path]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Path instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: Optional[PathToolkit]
        
    Provides:
        -   def execute(candidate: Any,) -> ValidationResult[Path]

    Super Class:
        ModelValidator
    """
    
    def __init__(self, toolkit: Optional[PathToolkit] | None = PathToolkit()):
        """
        Args:
            toolkit: Optional[PathToolkit]
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> PathToolkit:
        return cast(PathToolkit, self.toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult[Path]:
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
             PathValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        

        
        # Handle the case that, the validator is not primed.
        validator_priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.model,
            null_exception=self.toolkit.null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Path for additional tests. ---#
        path = cast(Path, candidate)
        
        # Handle the case that, the path's id gets flagged.
        id_validation = self.toolkit.identity_service.validate_id(path.id)
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that either the source or destination are not safe.
        for square in [path.endpoints.to_list]:
            square_validation_result = self.toolkit.square_validator.execute(square)
            if square_validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PathValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathValidatorException.MSG,
                        err_code=PathValidatorException.ERR_CODE,
                        ex=square_validation_result.exception,
                    )
                )
        # Handle the case that, the origin and the destination are the same.
        if path.endpoints.origin_is_destination:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidatorException.MSG,
                    err_code=PathValidatorException.ERR_CODE,
                    ex=CircularPathException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CircularPathException.MSG,
                        err_code=CircularPathException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(path)
        
        
