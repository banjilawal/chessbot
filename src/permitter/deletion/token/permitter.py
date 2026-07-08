# src/deletion/token/py

"""
Module: deletion.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from err import PoppingEmptyTokenStackException, TokenDeletePermitterException
from report import DeletionApprovalReport
from request import DeletionRequest
from stack import TokenStackService
from tester import TokenDeletionRequestTester
from util import LoggingLevelRouter


class TokenDeletionPermitter:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a deletion.

    Attributes:
        request_tester: TokenDeletionRequestTester

    Provides:
        -   run(item_id: int, stack: TokenStackService) -> DeletionApprovalReport:

    Super Class:
        DeletionPermitter
    """
    _request_tester: TokenDeletionRequestTester
    
    def __init__(self, request_tester: TokenDeletionRequestTester | None = TokenDeletionRequestTester()):
        self._request_tester = request_tester
    
    @classmethod
    @LoggingLevelRouter.monitor
    def run(self, request: DeletionRequest,) -> DeletionApprovalReport:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The collision_detector
                    -   The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a deletion denial if
                    -   The TokenStack is full.
                    -   The item collides with an existing stack member.
                    -   The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            request: DeletionRequest
        Returns:
            DeletionApprovalReport
        Raises:
            TokenDeletePermitterException
            PoppingEmptyTokenStackException
        """
        method = f"{self.__class__.__name__}.run"
        
        # Handle the case that, the request is not bootstrapped successfully.
        bootstrap = self._request_tester.execute(candidate=request)
        if bootstrap.is_failure:
            # Send an exception chain in the permission denial.
            return DeletionApprovalReport.deny(
                TokenDeletePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDeletePermitterException.MSG,
                    err_code=TokenDeletePermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )

        stack = cast(TokenStackService, request.stack)
        if stack.is_empty:
            # Return the exception chain on failure
            return DeletionApprovalReport.deny(
                exception=TokenDeletePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDeletePermitterException.MSG,
                    err_code=TokenDeletePermitterException.ERR_CODE,
                    ex=PoppingEmptyTokenStackException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PoppingEmptyTokenStackException.MSG,
                        err_code=PoppingEmptyTokenStackException.ERR_CODE,
                    ),
                )
            )
        # --- Integrity and performance tests are passed. ---#
        return DeletionApprovalReport.approve(item_id=request.item_id, stack=stack)

    