# src/tester/request/promotion/token/tester.py

"""
Module: tester.request.promotion.token.tester
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import Any, Type, cast

from bootstrapper import PromotionPermitterBootstrapper
from err import PromotionRequestTesterException
from microservice import IdentityService
from request.promotion import PromotionRequest
from result import MethodResultType, ValidationResult
from tester import PromotionLevelTester, PromotionPawnTester, RequestTester


class PromotionRequestTester(RequestTester):
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a promotion that can be promoted.
        
    Attributes:
        pawn_tester: PromotionPawnTester
        identity_service: IdentityService
        priming_validator: PrimingValidator
        bootstrapper: PromotionPermitterBootstrapper
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _pawn_tester: PromotionPawnTester
    _identity_service: IdentityService
    _bootstrapper: PromotionPermitterBootstrapper
    _promotion_level_tester: PromotionLevelTester
    
    def __init__(
            self,
            pawn_tester: PromotionPawnTester | None = PromotionPawnTester(),
            identity_service: IdentityService | None = IdentityService(),
            promotion_level_tester: PromotionLevelTester | None = PromotionLevelTester(),
            bootstrapper: PromotionPermitterBootstrapper | None = PromotionPermitterBootstrapper(),
    ):
        """
        Args:
            pawn_tester: PromotionPawnTester
            identity_service: IdentityService
            promotion_level_tester: PromotionLevelTester
            bootstrapper: PromotionPermitterBootstrapper
        """
        self._bootstrapper = bootstrapper
        self._pawn_tester = pawn_tester
        self._identity_service = identity_service
        self._promotion_level_tester = promotion_level_tester
    
    
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
            PromotionRequestTesterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the PromotionRequest is not bootstrapped successfully.
        bootstrap = self._bootstrapper.bootstrap_request(candidate)
        if bootstrap.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestTesterException.MSG,
                    err_code=PromotionRequestTesterException.ERR_CODE,
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
                PromotionRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestTesterException.MSG,
                    err_code=PromotionRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=id_test.exception
                )
            )
        # Handle the case that, the subject is not a pawn.
        pawn_test = self._pawn_tester.execute(subject=request.candidate)
        if pawn_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestTesterException.MSG,
                    err_code=PromotionRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=pawn_test.exception
                )
            )
        # Handle the case that, the request contains a malformed stack.
        rank_level_test = self._promotion_level_tester.execute(request.rank_level)
        # Send the exception chain in the permission denial.
        if rank_level_test.is_failure:
        # Send the exception chain in the result.
            return ValidationResult.failure(
                PromotionRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRequestTesterException.MSG,
                    err_code=PromotionRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=pawn_test.exception
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(request)