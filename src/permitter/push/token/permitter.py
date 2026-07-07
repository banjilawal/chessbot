# src/permitter/push/token/permitter.py

"""
Module: permitter.push.token.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Type, cast

from bootstrapper import PrimingValidator
from detector import TokenCollisionDetector
from err import PushRequestNullException, TokenPushPermitterException, TokenStackNullException
from model import Token
from permitter import PushPermitter, RankSlotPermitter
from report import PushApprovalReport
from request import PushRequest, RankSlotRequest
from stack import TokenStackService
from util import IdFactory, LoggingLevelRouter
from validator import TokenValidator


class TokenPushPermitter(PushPermitter):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a push.

    Attributes:
        token_validator: TokenValidator
        rank_service: RankService
        quota_analyzer: RankQuotaAnalyzer
        collision_detector: TokenCollisionDetector
        priming_validator: PrimingValidator

    Provides:
        -   execute(request: PushRequest) -> PushApprovalReport

    Super Class:
    """
    _token_validator: TokenValidator
    _rank_slot_permitter: RankSlotPermitter
    _collision_detector: TokenCollisionDetector
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            token_validator: TokenValidator | None = TokenValidator(),
            rank_slot_permitter: RankSlotPermitter = RankSlotPermitter(),
            collision_detector: TokenCollisionDetector | None = TokenCollisionDetector(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            collision_detector: TokenCollisionDetector
            priming_validator: PrimingValidator
            rank_slot_permitter: RankSlotPermitter
        """
        self._token_validator = token_validator
        self._collision_detector = collision_detector
        self._priming_validator = priming_validator
        self._rank_slot_permitter = rank_slot_permitter
        
        
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
        
        # Handle the case that, the request is malformed
        request_type_validation_result  = self._priming_validator.execute(
            candidate=request,
            target_model=Type[PushRequest],
            null_exception=PushRequestNullException()
        )
        # Send the exception chain in the permission denial.
        if request_type_validation_result.is_failure:
            PushApprovalReport.deny(
                exception=TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    ex=request_type_validation_result.exception,
                )
            )
        # Handle the case that, the item is not a safe token.
        token_validation_result = self._token_validator.execute(
            candidate=request.item
        )
        # Send the exception chain in the permission denial.
        if token_validation_result.is_failure:
            PushApprovalReport.deny(
                exception=TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    ex=request_type_validation_result.exception,
                )
            )
        # Handle the case that, the request contains a malformed stack.
        stack_validation_result = self._priming_validator.execute(
            candidate=request.stack,
            target_model=Type[TokenStackService],
            null_exception=TokenStackNullException()
        )
        # Send the exception chain in the permission denial.
        if stack_validation_result.is_failure:
            PushApprovalReport.deny(
                exception=TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    ex=request_type_validation_result.exception,
                )
            )
        # Extract the token and stack for additional testing.
        token = cast(Token, token_validation_result.payload)
        stack = cast(TokenStackService, stack_validation_result.payload)
        
        # Handle the case that, there are no openings for the token's rank.
        rank_slot_permission = self._rank_slot_permitter.run(
            request=RankSlotRequest(
                id=IdFactory.next_id(class_name="RankSlotRequest"),
                rank=token.rank,
                token_stack=stack,
            )
        )
        # Send the exception chain in the permission denial.
        if rank_slot_permission.is_denied:
            PushApprovalReport.deny(
                exception=TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    ex=rank_slot_permission.exception,
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