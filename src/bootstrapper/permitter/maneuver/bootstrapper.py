# src/bootstrapper/permitter/maneuver/bootstrapper.py

"""
Module: bootstrapper/permitter.maneuver.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from err import ManeuverRequestNullException, ManeuverPermitterBootstrapperException
from permitter import PermitterBootstrapper
from request import ManeuverRequest
from result import ValidationResult
from util import LoggingLevelRouter


class ManeuverPermitterBootstrapper(PermitterBootstrapper):
    """
    Role:
        - Bootstrapper

    Responsibilities:
        1.  Verfiy a ManeuverPermitter receives a well formed ManeuverRequest.

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
                    -   Not a ManeuverRequest.
            2.  Otherwise, send the success
        Args:
            request
        Returns:
            ValidationResult
        Raises:
            ManeuverPermitterBootstrapperException
        """
        method = f"{self.__class__.__name__}.bootstrap_request"
        
        # Handle the case that, the request is malformed
        validation_result = self.priming_validator.execute(
            candidate=request,
            target_model=Type[ManeuverRequest],
            null_exception=ManeuverRequestNullException()
        )
        if validation_result.is_failure:
            # Send the exception chain in the ValidationResult.
            return ValidationResult.failure(
                ManeuverPermitterBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPermitterBootstrapperException.MSG,
                    err_code=ManeuverPermitterBootstrapperException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)