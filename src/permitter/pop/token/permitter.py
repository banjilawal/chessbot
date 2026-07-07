# src/pop/token/py

"""
Module: pop.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from err import PoppingEmptyTokenStackException, TokenPopPermitterException, TokenStackNullException
from model import Token
from permitter import PopPermitter
from report import PopApprovalReport
from request import PopRequest
from stack import TokenStackService
from util import LoggingLevelRouter


class TokenPopPermitter(PopPermitter[Token]):
    """
    Role:
        -   Request Analyzer
        -   Rights Granter
        -   Consistency, Integrity Maintenance

    Responsibilities:
        1.  Evaluate if a TokenStack popping request can be granted.

    Attributes:
        priming_validator: PrimingValidator

    Provides:
        -   run(self, request: PopRequest,) -> PopApprovalReport:

    Super Class:
        PopPermitter
    """

    @LoggingLevelRouter.monitor
    def run(self, request: PopRequest) -> PopApprovalReport:
        """
        Evaluate a TokenStack pop request.
        
        Action:
            1.  Deny the request if any of the following occur.
                    -   The request cannot be bootstrapped.
                    -   The request does not contain a TokenStackService.
                    -   The TokenStack is empty.
            2.  Otherwise, approve the request.
        Args:
            request: PopRequest
        Returns:
            PopApprovalReport
        Raises:
            TokenPopperPermitterException
            PoppingEmptyTokenStackException
        """
        method =  f"{self.__class__.__name__}.run"
        
        # Handle the case that, the request is not bootstrapped successfully.
        bootstrap_result = self.bootstrap_request(request)
        if bootstrap_result.is_failure:
            # Send an exception chain in the permission denial.
            return PopApprovalReport.deny(
                TokenPopPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPopPermitterException.MSG,
                    err_code=TokenPopPermitterException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # Handle the case that, the candidate is not a TokenStack.
        stack_validation_result = self.priming_validator.execute(
            candidate=request.stack,
            target_model=Type[TokenStackService],
            null_exception=TokenStackNullException()
        )
        if stack_validation_result.is_failure:
            # Send an exception chain in the permission denial.
            return PopApprovalReport.deny(
                TokenPopPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPopPermitterException.MSG,
                    err_code=TokenPopPermitterException.ERR_CODE,
                    ex=stack_validation_result.exception,
                )
            )
        # Handle the case that, the stack is empty.
        if request.stack.is_empty:
            # Send an exception chain in the permission denial.
            return PopApprovalReport.deny(
                TokenPopPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPopPermitterException.MSG,
                    err_code=TokenPopPermitterException.ERR_CODE,
                    ex=PoppingEmptyTokenStackException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PoppingEmptyTokenStackException.MSG,
                        err_code=PoppingEmptyTokenStackException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the request approval to the caller. ---#
        return PopApprovalReport.approve(stack=request.stack)

    