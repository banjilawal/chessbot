# src/permitter/deletion/permitter.py

"""
Module: permitter.deletion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import abstractmethod
from typing import Type

from err import DeletionRequestNullException, DeleterPermitterException, PopRequestNullException
from permitter import Permitter
from report import DeletionApprovalReport, PushApprovalReport
from request import DeletionRequest, PopRequest, PushRequest
from result import ValidationResult
from util import LoggingLevelRouter


class DeleterPermitter(Permitter):
    """
    Role:
        -   Request Analyzer
        -   Rights Granter
        -   Consistency, Integrity Maintenance

    Responsibilities:
        1.  Evaluate if permission to remove a stack member can be granted.

    Attributes:

    Provides:
        -   run(self, request: DeletionRequest,) -> DeletionApprovalReport:

    Super Class:
        Permitter
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def run(self, request: DeletionRequest,) -> DeletionApprovalReport:
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
            DeleterPermitterException
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
                DeleterPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DeleterPermitterException.MSG,
                    err_code=DeleterPermitterException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)