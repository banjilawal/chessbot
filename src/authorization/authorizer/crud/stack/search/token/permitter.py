# src/authorization/authorizer/stack/search/token/authorizer.py

"""
Module: authorization.authorizer.stack.search.token.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain.search.context import TokenContext
from err import TokenSearchAuthorizerException
from domain.model import Token
from authorization.authorizer.crud.stack import SearchAuthorizer
from artifcat.report import SearchApprovalReport
from client.exchange import SearchPermissionRequest
from collection.stack import TokenStackService
from authorization.adjudicator import TokenSearchPermissionRequestAdjudicator
from util import LoggingLevelRouter


class TokenSearchAuthorizer(SearchAuthorizer[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a search.

    Attributes:
        request_adjudicator: TokenSearchPermissionRequestAdjudicator

    Provides:
        - execute(request: SearchPermissionRequest) -> SearchApprovalReport

    Super Class:
        SearchAuthorizer
    """
    _request_adjudicator: TokenSearchPermissionRequestAdjudicator
    
    def __init__(
            self,
            request_adjudicator: TokenSearchPermissionRequestAdjudicator | None = TokenSearchPermissionRequestAdjudicator()
    ):
        """
        Args:
            request_adjudicator: TokenSearchPermissionRequestAdjudicator
        """
        super().__init__()
        self._request_adjudicator = request_adjudicator
        
        
    @LoggingLevelRouter.monitor
    def execute(self, request: SearchPermissionRequest, ) -> SearchApprovalReport:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    - The collision_detector
                    - The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a search denial if
                    - The TokenStack is full.
                    - The item collides with an existing stack member.
                    - The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            request: SearchPermissionRequest
        Returns:
            AnalysisResult
        Raises:
            TokenSearchAuthorizerException
            TokenStackFullException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is not bootstrapped successfully.
        bootstrap = self._request_adjudicator.execute(candidate=request)
        if bootstrap.is_failure:
            # Send an exception chain in the permission denial.
            return SearchApprovalReport.denial(
                TokenSearchAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearchAuthorizerException.MSG,
                    err_code=TokenSearchAuthorizerException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )

        context = cast(TokenContext, request.context)
        stack = cast(TokenStackService, request.stack)

        # Forward the permission approval.
        return SearchApprovalReport.grant(context=context, stack=stack)