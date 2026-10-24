# src/authorization/authorizer/chain/search/token/authorizer.py

"""
Module: authorization.authorizer.chain.search.token.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain.search.context import TokenContext
from err import TokenSearchAuthorizerException
from domain.model import Token
from authorization.authorizer.crud.chain import SearchAuthorizer
from artifcat.report import SearchApprovalReport
from client.exchange import SearchAuthorizationRequest
from chain import TokenChainService
from authorization.adjudicator import TokenSearchAuthorizationRequestAdjudicator
from util import LoggingLevelRouter


class TokenSearchAuthorizer(SearchAuthorizer[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenChainService to execute a search.

    Attributes:
        request_adjudicator: TokenSearchAuthorizationRequestAdjudicator

    Provides:
        - execute(request: SearchAuthorizationRequest) -> SearchApprovalReport

    Super Class:
        SearchAuthorizer
    """
    _request_adjudicator: TokenSearchAuthorizationRequestAdjudicator
    
    def __init__(
            self,
            request_adjudicator: TokenSearchAuthorizationRequestAdjudicator | None = TokenSearchAuthorizationRequestAdjudicator()
    ):
        """
        Args:
            request_adjudicator: TokenSearchAuthorizationRequestAdjudicator
        """
        super().__init__()
        self._request_adjudicator = request_adjudicator
        
        
    @LoggingLevelRouter.monitor
    def execute(self, request: SearchAuthorizationRequest, ) -> SearchApprovalReport:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    - The collision_detector
                    - The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a search denial if
                    - The TokenChain is full.
                    - The item collides with an existing chain member.
                    - The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            request: SearchAuthorizationRequest
        Returns:
            AnalysisResult
        Raises:
            TokenSearchAuthorizerException
            TokenChainFullException
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
        chain = cast(TokenChainService, request.chain)

        # Forward the permission approval.
        return SearchApprovalReport.grant(context=context, chain=chain)