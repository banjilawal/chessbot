# src/permitter/pop/permitter.py

"""
Module: permitter.pop.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import abstractmethod
from typing import Type

from err import PopRequestNullException, PopperPermitterException
from permitter import Permitter
from report import PopApprovalReport
from request import PopRequest
from result import ValidationResult
from util import LoggingLevelRouter


class PopPermitter(Permitter):
    """
    Role:
        -   Request Analyzer
        -   Rights Granter
        -   Consistency, Integrity Maintenance

    Responsibilities:
        1.  Evaluate if a stack popping request can be granted.

    Attributes:
        priming_validator: PrimingValidator

    Provides:
        -   run(self, request: PopRequest,) -> PopApprovalReport:

    Super Class:
        Permitter
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def run(self, request: PopRequest,) -> PopApprovalReport:
        pass
    
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
            PopperPermitterException
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
                PopperPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PopperPermitterException.MSG,
                    err_code=PopperPermitterException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)