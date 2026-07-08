# src/bootstrapper/permitter/pop/bootstrapper.py

"""
Module: bootstrapper.permitter.pop.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from err import PopRequestNullException, PopPermitterBootstrapperException
from permitter import PermitterBootstrapper
from request import PopRequest
from result import ValidationResult
from util import LoggingLevelRouter


class PopPermitterBootstrapper(PermitterBootstrapper):
    """
    Role:
        - Bootstrapper

    Responsibilities:
        1.  Verfiy a PopPermitter receives a well formed PopRequest.

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
                    -   Not a PopRequest.
            2.  Otherwise, send the success
        Args:
            request
        Returns:
            ValidationResult
        Raises:
            PopPermitterBootstrapperException
        """
        method = f"{self.__class__.__name__}.bootstrap_request"
        
        # Handle the case that, the request is malformed
        validation_result = self.priming_validator.execute(
            candidate=request,
            target_model=Type[PopRequest],
            null_exception=PopRequestNullException()
        )
        if validation_result.is_failure:
            # Send the exception chain in the ValidationResult.
            return ValidationResult.failure(
                PopPermitterBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PopPermitterBootstrapperException.MSG,
                    err_code=PopPermitterBootstrapperException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)