# src/authorization/loader/promotion/loader.py

"""
Module: authorization.loader.promotion.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from authorization import AuthorizationLoader, PromotionAuthorizationForm
from domain import PawnToken, Token
from err import ChessException, PromotionRequestNullException
from exchange import PromotionRequest, RankValidationService, TokenValidationRequest, TokenValidationService
from transit import PawnTokenCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionAuthorizationLoader(AuthorizationLoader[PromotionRequest]):


    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PromotionRequest]:
        method = f"{self.__class__.__name__}.execute"
        
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=PromotionRequest,
            null_exception=PromotionRequestNullException(),
        )
        if priming.is_failure:
            return ValidationResult.failure(
               ChessException(
                   cls_mthd=method,
                   cls_name=self.__class__.__name__,
                   msg=ChessException.MSG,
                   err_code=ChessException.ERR_CODE,
                   ex=priming.exception,
                )
            )
        request = cast(Type[PromotionRequest], priming.payload)
        return ValidationResult.success(request)
        

        

        form_id = cast(int, form_id_validation.payload)
        operation_id = cast(int, op_number_validation.payload)
        verified_form = PromotionAuthorizationForm(
            id=form_id,
            operation=PromotionRequest(id=operation_id, applicant=pawn)
        )
        return ValidationResult.success(verified_form)