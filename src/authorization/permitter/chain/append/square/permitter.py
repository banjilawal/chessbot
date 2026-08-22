# src/authorization/permitter/chain/append/square/permitter.py

"""
Module: authorization.permitter.chain.append.square.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from sensor.detector import SquareCollider
from err import SquareAppendPermitterException
from domain.model import Square
from authorization.permitter.chain import AppendPermitter
from report import AppendApprovalReport
from domain.exchange.request import AppendRequest
from chain import SquareChainService
from authorization.adjudicator import SquareAppendRequestAdjudicator
from util import LoggingLevelRouter


class SquareAppendPermitter(AppendPermitter[Square]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a SquareChainService to execute a append.

    Attributes:
        collision_detector: SquareCollisionDetector
        rank_slot_permitter: RankSlotPermitter
        request_adjudicator: SquareAppendRequestAdjudicator

    Provides:
        -   execute(request: AppendRequest) -> AppendApprovalReport

    Super Class:
        AppendPermitter
    """
    _collision_detector: SquareCollider
    _request_adjudicator: SquareAppendRequestAdjudicator
    
    def __init__(
            self,
            collision_detector: SquareCollider | None = SquareCollider(),
            request_adjudicator: SquareAppendRequestAdjudicator | None = SquareAppendRequestAdjudicator()
    ):
        """
        Args:
            collision_detector: SquareCollisionDetector
            request_adjudicator: SquareAppendRequestAdjudicator
        """
        super().__init__()
        self._collision_detector = collision_detector
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
                    -   The SquareChain is full.
                    -   The item collides with an existing chain member.
                    -   The quota for the square's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            request: AppendRequest
        Returns:
            AnalysisResult
        Raises:
            SquareAppendPermitterException
            SquareChainFullException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request is not bootstrapped successfully.
        bootstrap = self._request_adjudicator.execute(candidate=request)
        if bootstrap.is_failure:
            # Send an exception chain in the permission denial.
            return AppendApprovalReport.deny(
                SquareAppendPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareAppendPermitterException.MSG,
                    err_code=SquareAppendPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )

        square = cast(Square, request.item)
        chain = cast(SquareChainService, request.chain)
        
        # Handle the case that, square conflicts with a current chain member.
        report = self._collision_detector.execute(attractor=square, stream=chain)
        if report.collision_exists:
            AppendApprovalReport.deny(
                exception=SquareAppendPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareAppendPermitterException.MSG,
                    err_code=SquareAppendPermitterException.ERR_CODE,
                    ex=report.exception,
                )
            )
        # Forward the permission approval.
        return AppendApprovalReport.grant(item=square, chain=chain)