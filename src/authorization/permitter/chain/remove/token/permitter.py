# src/remove/token/py

"""
Module: remove.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type

from err import RemovepingEmptyTokenChainException, TokenRemovePermitterException, TokenChainNullException
from domain.model import Token
from authorization.permitter.chain import RemovePermitter
from artifcat.report import RemoveApprovalReport
from domain.exchange.request import RemoveRequest
from chain import TokenChainService
from util import LoggingLevelRouter


class TokenRemovePermitter(RemovePermitter[Token]):
    """
    Role:
        - Request Analyzer
        -  Rights Granter
        -  Consistency, Integrity Maintenance

    Responsibilities:
        1.  Evaluate if a TokenChain removeping request can be granted.

    Attributes:
        priming_validator: PrimingValidator

    Provides:
        -  run(self, request: RemoveRequest,) -> RemoveApprovalReport:

    Super Class:
        RemovePermitter
    """

    @LoggingLevelRouter.monitor
    def execute(self, request: RemoveRequest) -> RemoveApprovalReport:
        """
        Evaluate a TokenChain remove request.
        
        Action:
            1.  Deny the request if any of the following occur.
                    -  The request cannot be bootstrapped.
                    -  The request does not contain a TokenChainService.
                    -  The TokenChain is empty.
            2.  Otherwise, approve the request.
        Args:
            request: RemoveRequest
        Returns:
            RemoveApprovalReport
        Raises:
            TokenRemoveperPermitterException
            RemovepingEmptyTokenChainException
        """
        method =  f"{self.__class__.__name__}.run"
        
        # Handle the case that, the request is not bootstrapped successfully.
        bootstrap_result = self.bootstrap_request(request)
        if bootstrap_result.is_failure:
            # Send an exception chain in the permission denial.
            return RemoveApprovalReport.deny(
                TokenRemovePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenRemovePermitterException.MSG,
                    err_code=TokenRemovePermitterException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # Handle the case that, the candidate is not a TokenChain.
        chain_validation_result = self.priming_validator.execute(
            candidate=request.chain,
            target_model=Type[TokenChainService],
            null_exception=TokenChainNullException()
        )
        if chain_validation_result.is_failure:
            # Send an exception chain in the permission denial.
            return RemoveApprovalReport.deny(
                TokenRemovePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenRemovePermitterException.MSG,
                    err_code=TokenRemovePermitterException.ERR_CODE,
                    ex=chain_validation_result.exception,
                )
            )
        # Handle the case that, the chain is empty.
        if request.chain.is_blank:
            # Send an exception chain in the permission denial.
            return RemoveApprovalReport.deny(
                TokenRemovePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenRemovePermitterException.MSG,
                    err_code=TokenRemovePermitterException.ERR_CODE,
                    ex=RemovepingEmptyTokenChainException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RemovepingEmptyTokenChainException.MSG,
                        err_code=RemovepingEmptyTokenChainException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the request approval to the caller. ---#
        return RemoveApprovalReport.grant(chain=request.chain)

    