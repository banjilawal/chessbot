# src/permitter/push/token/permitter.py

"""
Module: permitter.push.token.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from detector.token import TokenCollisionDetector
from err import TokenPushPermitterException
from model import Token
from permitter import PushPermitter, RankSlotPermitter
from report import PushApprovalReport
from request import PushRequest, RankSlotRequest
from stack import TokenStackService
from tester import TokenPushRequestTester
from util import IdFactory, LoggingLevelRouter


class TokenPushPermitter(PushPermitter[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a push.

    Attributes:
        collision_detector: TokenCollisionDetector
        rank_slot_permitter: RankSlotPermitter
        request_tester: TokenPushRequestTester

    Provides:
        -   execute(request: PushRequest) -> PushApprovalReport

    Super Class:
        PushPermitter
    """
    _rank_slot_permitter: RankSlotPermitter
    _collision_detector: TokenCollisionDetector
    _request_tester: TokenPushRequestTester
    
    def __init__(
            self,
            rank_slot_permitter: RankSlotPermitter = RankSlotPermitter(),
            collision_detector: TokenCollisionDetector | None = TokenCollisionDetector(),
            request_tester: TokenPushRequestTester | None = TokenPushRequestTester()
    ):
        """
        Args:
            collision_detector: TokenCollisionDetector
            rank_slot_permitter: RankSlotPermitter
            request_tester: TokenPushRequestTester
        """
        super().__init__()
        self._collision_detector = collision_detector
        self._rank_slot_permitter = rank_slot_permitter
        self._request_tester = request_tester
        
        
    @LoggingLevelRouter.monitor
    def run(self, request: PushRequest, ) -> PushApprovalReport:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The collision_detector
                    -   The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a push denial if
                    -   The TokenStack is full.
                    -   The item collides with an existing stack member.
                    -   The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            request: PushRequest
        Returns:
            AnalysisResult
        Raises:
            TokenPushPermitterException
            TokenStackFullException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request is not bootstrapped successfully.
        bootstrap = self._request_tester.execute(candidate=request)
        if bootstrap.is_failure:
            # Send an exception chain in the permission denial.
            return PushApprovalReport.deny(
                TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )

        token = cast(Token, request.item)
        stack = cast(TokenStackService, request.stack)
        
        # Handle the case that, there is no opening for the token's rank.
        rank_opening = self._rank_slot_permitter.run(
            RankSlotRequest(
                id=IdFactory.next_id(class_name="RankSLotRequest"),
                token_stack=stack,
                rank=token.rank,
            )
        )
        if rank_opening.is_denied:
            # Send an exception chain in the permission denial.
            return PushApprovalReport.deny(
                TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    ex=rank_opening.exception,
                )
            )
        # Handle the case that, token conflicts with a current stack member.
        report = self._collision_detector.execute(attractor=token, stream=stack)
        if report.collision_exists:
            PushApprovalReport.deny(
                exception=TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    ex=report.exception,
                )
            )
        # Forward the permission approval.
        return PushApprovalReport.approve(item=token, stack=stack)