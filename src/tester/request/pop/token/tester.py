# src/tester/request/pop/token/tester.py

"""
Module: tester.request.pop.token.tester
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import Any, Type, cast

from bootstrapper import PrimingValidator, PopPermitterBootstrapper
from err import TokenStackNullException, TokenPopRequestTesterException
from request import PopRequest
from result import MethodResultType, ValidationResult
from stack import TokenStackService
from tester import PopRequestTester
from util import LoggingLevelRouter


class TokenPopRequestTester(PopRequestTester):
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a pop that can be promoted.
        
    Attributes:
        priming_validator: PrimingValidator
        carrier_validator: PopPermitterBootstrapper
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _priming_validator: PrimingValidator
    _bootstrapper: PopPermitterBootstrapper
    
    def __init__(
            self,
            priming_validator: PrimingValidator | None = PrimingValidator(),
            bootstrapper: PopPermitterBootstrapper | None = PopPermitterBootstrapper(),
    ):
        """
        Args:
            priming_validator: PrimingValidator
            bootstrapper: PopPermitterBootstrapper
        """
        self._bootstrapper = bootstrapper
        self._priming_validator = priming_validator
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        """
        Verifies the subject is a promotable pop.
        
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following occur:
                    -   The subject is flagged unsafe.
                    -   The subject is not a free pop.
                    -   The pop has already been promoted.
                    -   Is not on its enemy's rank_row.
            2.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[PopToken]
        Raises:
            TokenStackPopTesterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the PopRequest is not bootstrapped successfully.
        bootstrap = self._bootstrapper.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenPopRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPopRequestTesterException.MSG,
                    err_code=TokenPopRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=bootstrap.exception
                )
            )
        request = cast(PopRequest, bootstrap.payload)
        # Handle the case that, the request contains a malformed stack.
        stack_test = self._priming_validator.execute(
            candidate=request.stack,
            target_model=Type[TokenStackService],
            null_exception=TokenStackNullException()
        )
        # Send the exception chain in the permission denial.
        if stack_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenPopRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPopRequestTesterException.MSG,
                    err_code=TokenPopRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=stack_test.exception
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(request)