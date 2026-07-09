# src/bootstrapper/permitter/promotion/bootstrapper.py

"""
Module: bootstrapper.permitter.promotion.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from bootstrapper import PermitterBootstrapper
from err import PromotionRequestNullException, PromotionPermitterBootstrapperException
from request.promotion import PromotionRequest
from result import ValidationResult
from util import LoggingLevelRouter


class PromotionPermitterBootstrapper(PermitterBootstrapper):
    """
    Role:
        - Bootstrapper

    Responsibilities:
        1.  Verfiy a PromotionPermitter receives a well-formed PromotionRequest.

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
                    -   Not a PromotionRequest.
            2.  Otherwise, send the success
        Args:
            request
        Returns:
            ValidationResult
        Raises:
            PromotionPermitterBootstrapperException
        """
        method = f"{self.__class__.__name__}.bootstrap_request"
        
        # Handle the case that, the request is malformed
        validation_result = self.priming_validator.execute(
            candidate=request,
            target_model=Type[PromotionRequest],
            null_exception=PromotionRequestNullException()
        )
        if validation_result.is_failure:
            # Send the exception chain in the ValidationResult.
            return ValidationResult.failure(
                PromotionPermitterBootstrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterBootstrapperException.MSG,
                    err_code=PromotionPermitterBootstrapperException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)