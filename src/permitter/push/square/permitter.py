# src/permitter/push/square/permitter.py

"""
Module: permitter.push.square.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from detector import SquareCollisionDetector
from err import SquarePushPermitterException
from model import Square
from permitter import PushPermitter, RankSlotPermitter
from report import PushApprovalReport
from request import PushRequest, RankSlotRequest
from stack import SquareStackService
from tester import SquarePushRequestTester
from util import IdFactory, LoggingLevelRouter


class SquarePushPermitter(PushPermitter[Square]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a SquareStackService to execute a push.

    Attributes:
        collision_detector: SquareCollisionDetector
        rank_slot_permitter: RankSlotPermitter
        request_tester: SquarePushRequestTester

    Provides:
        -   execute(request: PushRequest) -> PushApprovalReport

    Super Class:
        PushPermitter
    """
    _collision_detector: SquareCollisionDetector
    _request_tester: SquarePushRequestTester
    
    def __init__(
            self,
            collision_detector: SquareCollisionDetector | None = SquareCollisionDetector(),
            request_tester: SquarePushRequestTester | None = SquarePushRequestTester()
    ):
        """
        Args:
            collision_detector: SquareCollisionDetector
            request_tester: SquarePushRequestTester
        """
        super().__init__()
        self._collision_detector = collision_detector
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
                    -   The SquareStack is full.
                    -   The item collides with an existing stack member.
                    -   The quota for the square's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            request: PushRequest
        Returns:
            AnalysisResult
        Raises:
            SquarePushPermitterException
            SquareStackFullException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request is not bootstrapped successfully.
        bootstrap = self._request_tester.execute(candidate=request)
        if bootstrap.is_failure:
            # Send an exception chain in the permission denial.
            return PushApprovalReport.deny(
                SquarePushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquarePushPermitterException.MSG,
                    err_code=SquarePushPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )

        square = cast(Square, request.item)
        stack = cast(SquareStackService, request.stack)
        
        # Handle the case that, square conflicts with a current stack member.
        report = self._collision_detector.execute(attractor=square, stream=stack)
        if report.collision_exists:
            PushApprovalReport.deny(
                exception=SquarePushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquarePushPermitterException.MSG,
                    err_code=SquarePushPermitterException.ERR_CODE,
                    ex=report.exception,
                )
            )
        # Forward the permission approval.
        return PushApprovalReport.approve(item=square, stack=stack)