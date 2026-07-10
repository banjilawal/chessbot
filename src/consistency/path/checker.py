# src/consistency/path/consistency.py

"""
Module: consistency.path.consistency
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import CircularPathException, PathConsistencyCheckerException
from model import Path
from result import ValidationResult
from toolkit import PathToolkit
from util import LoggingLevelRouter


class PathConsistency:
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
        -   def consistencyChecker(
                    cls,
                    candidate,
                    identity_service: IdentityService,
                    square_consistency: SquareConsistency,
                    priming_consistency: PrimingConsistency,
            ) -> ValidationResult[Path]

    Super Class:
        Consistency
    """
    OPERATION_NAME = "path_consistency"
    
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
             PathConsistencyCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = PathToolkit()
        
        # Handle the case that, the consistency is not primed.
        consistency_priming_result = toolkit.priming_consistency.execute(
            candidate=candidate,
            target_model=toolkit.model,
            null_exception=toolkit.null_exception,
        )
        if consistency_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathConsistencyCheckerException.MSG,
                    err_code=PathConsistencyCheckerException.ERR_CODE,
                    ex=consistency_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Path for additional tests. ---#
        path = cast(Path, candidate)
        
        # Handle the case that, the path's id gets flagged.
        id_validation = toolkit.identity_service.validate_id(path.id)
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathConsistencyCheckerException.MSG,
                    err_code=PathConsistencyCheckerException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that either the source or destination are not safe.
        for square in [path.origin, path.destination]:
            square_validation_result = toolkit.square_consistency.execute(square)
            if square_validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PathConsistencyCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathConsistencyCheckerException.MSG,
                        err_code=PathConsistencyCheckerException.ERR_CODE,
                        ex=square_validation_result.exception,
                    )
                )
        # Handle the case that, the origin and the destination are the same.
        if path.origin == path.destination:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathConsistencyCheckerException.MSG,
                    err_code=PathConsistencyCheckerException.ERR_CODE,
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
        
        
