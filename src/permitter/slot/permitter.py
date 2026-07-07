# src/permitter/slot/permitter.py

"""
Module: permitter.slot.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Type, cast

from analyzer import RankQuotaAnalyzer
from bootstrapper import PrimingValidator
from err import RankQuotaFullException, RankSlotPermitterException, RankSlotRequestNullException
from permitter import Permitter
from report import RankQuotaReport, RankSlotApprovalReport
from request import RankSlotRequest
from util import LoggingLevelRouter
from validator import RankValidator


class RankSlotPermitter(Permitter):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a RankStackService to execute a push.

    Attributes:
        rank_validator: RankValidator
        slot_analyzer: RankQuotaAnalyzer
        priming_validator: PrimingValidator

    Provides:
        -   execute(request: RankSlotRequest) -> RankSlotApprovalReport

    Super Class:
    """
    _rank_validator: RankValidator
    _slot_analyzer: RankQuotaAnalyzer
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            rank_validator: RankValidator | None = RankValidator(),
            slot_analyzer: RankQuotaAnalyzer | None = RankQuotaAnalyzer(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            rank_validator: RankValidator
            slot_analyzer: RankQuotaAnalyzer
            priming_validator: PrimingValidator
        """
        self._rank_validator = rank_validator
        self._slot_analyzer = slot_analyzer
        self._priming_validator = priming_validator
        
        
    @LoggingLevelRouter.monitor
    def run(self, request: RankSlotRequest) -> RankSlotApprovalReport:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The collision_detector
                    -   The rank_slot_analyzer
                do not complete their work.
            2.  Otherwise, send a push denial if
                    -   The RankStack is full.
                    -   The item collides with an existing stack member.
                    -   The slot for the rank's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            request: RankSlotRequest
        Returns:
            AnalysisResult
        Raises:
            RankSlotPermitterException
            RankStackFullException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request is malformed
        request_type_validation_result  = self._priming_validator.execute(
            candidate=request,
            target_model=Type[RankSlotRequest],
            null_exception=RankSlotRequestNullException()
        )
        # Send the exception chain in the permission denial.
        if request_type_validation_result.is_failure:
            RankSlotApprovalReport.deny(
                exception=RankSlotPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankSlotPermitterException.MSG,
                    err_code=RankSlotPermitterException.ERR_CODE,
                    ex=request_type_validation_result.exception,
                )
            )
        quota_analysis_result = self._slot_analyzer.execute(
            rank=request.rank,
            token_stack=request.token_stack,
        )
        # Send a permission denial if the analyzer aborts.
        if quota_analysis_result.is_failure:
            RankSlotApprovalReport.deny(
                exception=RankSlotPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankSlotPermitterException.MSG,
                    err_code=RankSlotPermitterException.ERR_CODE,
                    ex=quota_analysis_result.exception,
                )
            )
        quota = cast(RankQuotaReport, quota_analysis_result.payload)
        # Send a permission denial if there ar no openings for the rank.
        if not quota.openings_exist:
            RankSlotApprovalReport.deny(
                exception=RankSlotPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankSlotPermitterException.MSG,
                    err_code=RankSlotPermitterException.ERR_CODE,
                    ex=RankQuotaFullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankQuotaFullException.MSG,
                        err_code=RankQuotaFullException.ERR_CODE,
                    ),
                )
            )
        return RankSlotApprovalReport.approve(rank=request.rank, token_stack=request.token_stack)

    