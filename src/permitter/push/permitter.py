# src/permitter/push/permitter.py

"""
Module: permitter.push.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import abstractmethod
from typing import Type

from err import PusherPermitterException, PushRequestNullException
from permitter import Permitter
from report import PushApprovalReport
from request import PushRequest
from result import ValidationResult
from util import LoggingLevelRouter


class PushPermitter(Permitter):
    """
    Role:
        - Analysis Worker
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Checks if an object satisfies the conditions to perform an operation.

    Attributes:

    Provides:
        -   def execute(cls, requestor: T, *args, **kwargs) -> AnalysisResult

    Super Class:
        Permitter
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def run(self, request: PushRequest,) -> PushApprovalReport:
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
            PusherPermitterException
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
                PusherPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PusherPermitterException.MSG,
                    err_code=PusherPermitterException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)