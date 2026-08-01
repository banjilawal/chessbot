# src/core/adjudicator/request/promotion/token/adjudicator.py

"""
Module: core.adjudicator.request.promotion.token.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import Any, cast

from bootstrapper import PromotionRequestBootstrapper
from err import PromotionRequestAdjudicatorException
from microservice import IdentityService
from request.promotion import PromotionRequest
from result import MethodResultType, ValidationResult
from core.adjudicator import PromotionLevelRequestAdjudicator, PromotionPawnRequestAdjudicator, RequestAdjudicator
from util import LoggingLevelRouter


class PromotionRequestAdjudicator(RequestAdjudicator):
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a promotion that can be promoted.
        
    Attributes:
        pawn_adjudicator: PromotionPawnAdjudicator
        identity_service: IdentityService
        priming_validator: PrimingValidator
        carrier_validator: PromotionPermitterBootstrapper
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _pawn_adjudicator: PromotionPawnRequestAdjudicator
    _identity_service: IdentityService
    _bootstrapper: PromotionRequestBootstrapper
    _promotion_level_adjudicator: PromotionLevelRequestAdjudicator
    
    def __init__(
            self,
            pawn_adjudicator: PromotionPawnRequestAdjudicator | None = PromotionPawnRequestAdjudicator(),
            identity_service: IdentityService | None = IdentityService(),
            promotion_level_adjudicator: PromotionLevelRequestAdjudicator | None = PromotionLevelRequestAdjudicator(),
            bootstrapper: PromotionRequestBootstrapper | None = PromotionRequestBootstrapper(),
    ):
        """
        Args:
            pawn_adjudicator: PromotionPawnAdjudicator
            identity_service: IdentityService
            promotion_level_adjudicator: PromotionLevelAdjudicator
            bootstrapper: PromotionPermitterBootstrapper
        """
        self._bootstrapper = bootstrapper
        self._pawn_adjudicator = pawn_adjudicator
        self._identity_service = identity_service
        self._promotion_level_adjudicator = promotion_level_adjudicator
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        """
        Verifies the subject is a promotable promotion.
        
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following occur:
                    -   The subject is flagged unsafe.
                    -   The subject is not a free promotion.
                    -   The promotion has already been promoted.
                    -   Is not on its enemy's rank_row.
            2.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult
        Raises:
            PromotionRequestAdjudicatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the PromotionRequest is not bootstrapped successfully.
        bootstrap = self._bootstrapper.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
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
        
        # handle the case that, the item is not a safe token.
        id_test = self._identity_service.validate_id(request.id)
        if id_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestAdjudicatorException.MSG,
                    err_code=PromotionRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=id_test.exception
                )
            )
        # Handle the case that, the subject is not a pawn.
        pawn_test = self._pawn_adjudicator.execute(candidate=request.candidate)
        if pawn_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestAdjudicatorException.MSG,
                    err_code=PromotionRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=pawn_test.exception
                )
            )
        # Handle the case that, the request contains a malformed stack.
        rank_level_test = self._promotion_level_adjudicator.execute(request.rank_level)
        # Send the exception chain in the permission denial.
        if rank_level_test.is_failure:
        # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestAdjudicatorException.MSG,
                    err_code=PromotionRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=pawn_test.exception
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(request)