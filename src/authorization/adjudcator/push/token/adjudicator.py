# src/core/adjudicator/request/push/token/adjudicator.py

"""
Module: core.adjudicator.request.push.token.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import Any, Type, cast

from bootstrapper import PrimingValidator, PushRequestBootstrapper
from err import TokenStackNullException, TokenPushRequestAdjudicatorException
from authorization.request import PushRequest
from result import MethodResultType, ValidationResult
from stack import TokenStackService
from core.adjudicator import PushRequestAdjudicator
from util import LoggingLevelRouter
from assurance.validator import TokenValidator


class TokenPushRequestAdjudicator(PushRequestAdjudicator):
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a push that can be promoted.
        
    Attributes:
        item_validator: TokenValidator
        priming_validator: PrimingValidator
        carrier_validator: PushPermitterBootstrapper
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _item_validator: TokenValidator
    _priming_validator: PrimingValidator
    _bootstrapper: PushRequestBootstrapper
    
    def __init__(
            self,
            item_validator: TokenValidator | None = TokenValidator(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
            bootstrapper: PushRequestBootstrapper | None = PushRequestBootstrapper(),
    ):
        """
        Args:
            item_validator: TokenValidator
            priming_validator: PrimingValidator
            bootstrapper: PushPermitterBootstrapper
        """
        self._bootstrapper = bootstrapper
        self._item_validator = item_validator
        self._priming_validator = priming_validator
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        """
        Verifies the subject is a promotable push.
        
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following occur:
                    -   The subject is flagged unsafe.
                    -   The subject is not a free push.
                    -   The push has already been promoted.
                    -   Is not on its enemy's rank_row.
            2.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[PushToken]
        Raises:
            TokenStackPushAdjudicatorException
            PromoteInactivePushException
            PushDoubleStackException
            PushStackRowException
            TypeError
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the PushRequest is not bootstrapped successfully.
        bootstrap = self._bootstrapper.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenPushRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushRequestAdjudicatorException.MSG,
                    err_code=TokenPushRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=bootstrap.exception
                )
            )
        request = cast(PushRequest, bootstrap.payload)
        # handle the case that, the item is not a safe token.
        token_test = self._item_validator.execute(request.item)
        if token_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenPushRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushRequestAdjudicatorException.MSG,
                    err_code=TokenPushRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=token_test.exception
                )
            )
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
                TokenPushRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushRequestAdjudicatorException.MSG,
                    err_code=TokenPushRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=stack_test.exception
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(request)