# src/authorization/adjudicator/token/request/promotion/token/adjudicator.py

"""
Module: authorization.adjudicator.token.request.promotion.token.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Any, Type, cast

from authorization import (
    PromotionLevelRequestAdjudicator, PromotionPawnRequestAdjudicator, PromotionRequest,
    RequestAdjudicator
)
from err import PromotionRequestNullException
from microservice import IdentityService
from domain.model import Pawn
from artifcat.report import PromotionRequestDecision
from artifcat import MethodResultType
from util import LoggingLevelRouter


class PromotionRequestAdjudicator(RequestAdjudicator[PromotionRequest]):
    """
    Role:
        - Helper
        -  Test Runner
        
    Responsibilities:
        1.  Check if the subject is a promotion that can be promoted.
        
    Attributes:
        identity_service: IdentityService
        pawn_adjudicator: PromotionPawnAdjudicator
        promotion_level_adjudicator: PromotionLevelAdjudicator
          
    Provides:
        - def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _identity_service: IdentityService
    _pawn_adjudicator: PromotionPawnRequestAdjudicator
    _promotion_level_adjudicator: PromotionLevelRequestAdjudicator
    
    def __init__(
            self,
            identity_service: IdentityService | None = None,
            pawn_adjudicator: PromotionPawnRequestAdjudicator | None = None,
            promotion_level_adjudicator: PromotionLevelRequestAdjudicator | None = None,
    ):
        """
        Args:
            identity_service: IdentityService
            pawn_adjudicator: PromotionPawnAdjudicator
            promotion_level_adjudicator: PromotionLevelAdjudicator
        """
        self._identity_service = identity_service or IdentityService()
        self._pawn_adjudicator = pawn_adjudicator or PromotionPawnRequestAdjudicator()
        self._promotion_level_adjudicator = promotion_level_adjudicator or PromotionLevelRequestAdjudicator()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> PromotionRequestDecision:
        """
        Verifies the subject is a promotable promotion.
        
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following occur:
                    -  The subject is flagged unsafe.
                    -  The subject is not a free promotion.
                    -  The promotion has already been promoted.
                    -  Is not on its enemy's rank_row.
            2.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            PromotionApprovalReport
        Raises:
            PromotionRequestAdjudicatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the, the candidate is either null or the wrong type.
        bootstrap = self.priming_validator.execute(
            candidate=candidate,
            target_mode=[PromotionRequest],
            null_exception=PromotionRequestNullException(),
        )
        if bootstrap.is_failure:
            # Send the exception chain in the result.
            return PromotionRequestDecision.deny(
                PromotionRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestAdjudicatorException.MSG,
                    err_code=PromotionRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=bootstrap.exception
                )
            )
        request = cast(PromotionRequest, bootstrap.payload)
        
        # handle the case that, of a malformed request id.
        id_validation = self._identity_service.validate_id(request.id)
        if id_validation.is_failure:
            # Send the exception chain in the result.
            return PromotionRequestDecision.deny(
                PromotionRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestAdjudicatorException.MSG,
                    err_code=PromotionRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=id_validation.exception
                )
            )
        # Handle the case that, the subject is not a pawn.
        pawn_test = self._pawn_adjudicator.execute(candidate=request.candidate)
        if pawn_test.is_failure:
            # Send the exception chain in the result.
            return PromotionRequestDecision.deny(
                PromotionRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestAdjudicatorException.MSG,
                    err_code=PromotionRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=pawn_test.exception
                )
            )
        pawn = cast(Pawn, pawn_test.payload)
        
        # Handle the case that, the promotion rank is wrong.
        rank_test = self._promotion_level_adjudicator.execute(request.rank_level)
        if rank_test.is_failure:
            # Send the exception chain in the permission denial.
            return PromotionRequestDecision.deny(
                PromotionRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestAdjudicatorException.MSG,
                    err_code=PromotionRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=rank_test.exception
                )
            )
        rank = cast(Type[request.rank_level], rank_test.payload)
        # --- Send the work product. ---#
        return PromotionRequestDecision.grant(pawn=pawn, rank_level=rank)