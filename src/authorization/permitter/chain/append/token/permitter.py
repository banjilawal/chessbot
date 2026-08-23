# src/authorization/permitter/chain/append/token/permitter.py

"""
Module: authorization.permitter.chain.append.token.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from sensor.detector.token import TokenCollisionDetector
from err import TokenAppendPermitterException
from domain.model import Token
from authorization.permitter.chain import AppendPermitter, RankSlotPermitter
from artifcat.report import AppendApprovalReport
from domain.exchange.request import AppendRequest, RankSlotRequest
from chain import TokenChainService
from authorization.adjudicator import TokenAppendRequestAdjudicator
from util import IdFactory, LoggingLevelRouter


class TokenAppendPermitter(AppendPermitter[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenChainService to execute a append.

    Attributes:
        collision_detector: TokenCollisionDetector
        rank_slot_permitter: RankSlotPermitter
        request_adjudicator: TokenAppendRequestAdjudicator

    Provides:
        -   execute(request: AppendRequest) -> AppendApprovalReport

    Super Class:
        AppendPermitter
    """
    _rank_slot_permitter: RankSlotPermitter
    _collision_detector: TokenCollisionDetector
    _request_adjudicator: TokenAppendRequestAdjudicator
    
    def __init__(
            self,
            rank_slot_permitter: RankSlotPermitter = RankSlotPermitter(),
            collision_detector: TokenCollisionDetector | None = TokenCollisionDetector(),
            request_adjudicator: TokenAppendRequestAdjudicator | None = TokenAppendRequestAdjudicator()
    ):
        """
        Args:
            collision_detector: TokenCollisionDetector
            rank_slot_permitter: RankSlotPermitter
            request_adjudicator: TokenAppendRequestAdjudicator
        """
        super().__init__()
        self._collision_detector = collision_detector
        self._rank_slot_permitter = rank_slot_permitter
        self._request_adjudicator = request_adjudicator
        
        
    @LoggingLevelRouter.monitor
    def execute(self, request: AppendRequest, ) -> AppendApprovalReport:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The collision_detector
                    -   The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a append denial if
                    -   The TokenChain is full.
                    -   The item collides with an existing chain member.
                    -   The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            request: AppendRequest
        Returns:
            AnalysisResult
        Raises:
            TokenAppendPermitterException
            TokenChainFullException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request is not bootstrapped successfully.
        bootstrap = self._request_adjudicator.execute(candidate=request)
        if bootstrap.is_failure:
            # Send an exception chain in the permission denial.
            return AppendApprovalReport.deny(
                TokenAppendPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenAppendPermitterException.MSG,
                    err_code=TokenAppendPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )

        token = cast(Token, request.item)
        chain = cast(TokenChainService, request.chain)
        
        # Handle the case that, there is no opening for the token's rank.
        rank_opening = self._rank_slot_permitter.execute(
            RankSlotRequest(
                id=IdFactory.next_id(class_name="RankSLotRequest"),
                token_chain=chain,
                rank=token.rank,
            )
        )
        if rank_opening.is_denied:
            # Send an exception chain in the permission denial.
            return AppendApprovalReport.deny(
                TokenAppendPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenAppendPermitterException.MSG,
                    err_code=TokenAppendPermitterException.ERR_CODE,
                    ex=rank_opening.exception,
                )
            )
        # Handle the case that, token conflicts with a current chain member.
        report = self._collision_detector.execute(attractor=token, stream=chain)
        if report.collision_exists:
            AppendApprovalReport.deny(
                exception=TokenAppendPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenAppendPermitterException.MSG,
                    err_code=TokenAppendPermitterException.ERR_CODE,
                    ex=report.exception,
                )
            )
        # Forward the permission approval.
        return AppendApprovalReport.grant(item=token, chain=chain)