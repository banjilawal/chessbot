# src/bootstrapper/permitter/deletion/bootstrapper.py

"""
Module: bootstrapper.permitter.deletion.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from bootstrapper import PermitterBootstrapper
from err import DeletionRequestNullException, DeletionPermitterBootstrapperException
from request import DeletionRequest
from result import ValidationResult
from util import LoggingLevelRouter


class DeletionPermitterBootstrapper(PermitterBootstrapper):
    """
    Role:
        - Bootstrapper

    Responsibilities:
        1.  Verfiy a DeletionPermitter receives a well formed DeletionRequest.

    Attributes:

    Provides:
        -   bootstrap_request(self, request) -> ValidationResult:

    Super Class:
        Permitter
    """
    def __init__(self):
        super().__init__()
        
    
    @LoggingLevelRouter.monitor
    def bootstrap_request(self, request) -> ValidationResult:
        """
        Evaluate a pawn promotion request.

        Action:
            1.  Send an exception chain in the ValidationResult if the request is either
                    -   Null
                    -   Not a DeletionRequest.
            2.  Otherwise, send the success
        Args:
            request
        Returns:
            ValidationResult
        Raises:
            DeletionPermitterBootstrapperException
        """
        method = f"{self.__class__.__name__}.bootstrap_request"
        
        # Handle the case that, the request is malformed
        validation_result = self.priming_validator.execute(
            candidate=request,
            target_model=Type[DeletionRequest],
            null_exception=DeletionRequestNullException()
        )
        if validation_result.is_failure:
            # Send the exception chain in the ValidationResult.
            return ValidationResult.failure(
                DeletionPermitterBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DeletionPermitterBootstrapperException.MSG,
                    err_code=DeletionPermitterBootstrapperException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)