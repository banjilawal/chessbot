# src/carrier_validator/permitter/push/carrier_validator.py

"""
Module: carrier_validator.permitter.push.carrier_validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from bootstrapper import PermitterBootstrapper
from err import PushRequestNullException, PushPermitterBootstrapperException
from request import PushRequest
from result import ValidationResult
from util import LoggingLevelRouter


class PushPermitterBootstrapper(PermitterBootstrapper):
    """
    Role:
        - Bootstrapper

    Responsibilities:
        1.  Verfiy a PushPermitter receives a well formed PushRequest.

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
                    -   Not a PushRequest.
            2.  Otherwise, send the success
        Args:
            request
        Returns:
            ValidationResult
        Raises:
            PushPermitterBootstrapperException
        """
        method = f"{self.__class__.__name__}.bootstrap_request"
        
        # Handle the case that, the request is malformed
        validation_result = self.priming_validator.execute(
            candidate=request,
            target_model=Type[PushRequest],
            null_exception=PushRequestNullException()
        )
        if validation_result.is_failure:
            # Send the exception chain in the ValidationResult.
            return ValidationResult.failure(
                PushPermitterBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PushPermitterBootstrapperException.MSG,
                    err_code=PushPermitterBootstrapperException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)