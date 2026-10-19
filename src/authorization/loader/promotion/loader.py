# src/authorization/loader/promotion/loader.py

"""
Module: authorization.loader.promotion.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import BuildResult
from authorization import AuthorizationLoader, PromotionAuthorizationForm
from domain import PawnToken, Token
from err import ChessException, PromotionRequestNullException
from exchange import PromotionRequest, TokenValidationRequest, TokenValidationService
from transit import PawnTokenCarrier
from util import IdFactory, LoggingLevelRouter


class PromotionAuthorizationLoader(AuthorizationLoader[PromotionRequest]):
    
    def __init__(
            self,
            validation_service: Optional[TokenValidationService] | None = None
    ):
        """
        Args:
            validation_service: Optional[TokenValidationService]
        """
        super().__init__(
            validation_service=validation_service or TokenValidationService()
        )
    
    @property
    def validation_service(self) -> TokenValidationService:
        return cast(TokenValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[PromotionAuthorizationForm]:
        method = f"{self.__class__.__name__}.execute"
        
        priming = self.priming_validator.execute(
            candidate=candidate,
            target_model=PromotionAuthorizationForm,
            null_exception=PromotionAuthorizationFormNullException(),
        )
        if priming.is_failure:
            return BuildResult.failure(
               ChessException(
                   cls_mthd=method,
                   cls_name=self.__class__.__name__,
                   msg=ChessException.MSG,
                   err_code=ChessException.ERR_CODE,
                   ex=priming.exception,
                   
                )
            )
        form = cast(Type[PromotionAuthorizationForm], priming.payload)
        
        form_id_validation = self.identity_service.validate_id(form.id)
        if form_id_validation.is_failure:
            return BuildResult.failure(
                ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=form_id_validation.exception,
                )
            )
        
        operation_validation = self.priming_validator.execute(
            candidate=form.operation,
            target_model=PromotionRequest,
            null_exception=PromotionRequestNullException(),
        )
        if operation_validation.is_failure:
            return BuildResult.failure(
                ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=operation_validation.exception,
                )
            )
        operation = cast(PromotionRequest, operation_validation.payload)
        operation_id_validation = self.identity_service.validate_id(form.id)
        if operation_id_validation.is_failure:
            return BuildResult.failure(
                ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=operation_id_validation.exception,
                )
            )
        token_validation = self.validation_service.extract_model(
            request=TokenValidationRequest(
                item=PawnTokenCarrier(model=operation.candidate_pawn),
                id=IdFactory.next_id(class_name="TokenValidationRequest")
            )
        )
        if token_validation.is_failure:
            return BuildResult.failure(
                ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=token_validation.exception,
                )
            )
        token = cast(Token, token_validation.payload)
        if not isinstance(token, PawnToken):
            return BuildResult.failure(
                ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=token_validation.exception,
                )
            )
        pawn = cast(PawnToken, token)
        form_id = cast(int, form_id_validation.payload)
        operation_id = cast(int, operation_id_validation.payload)
        verified_form = PromotionAuthorizationForm(
            id=form_id,
            operation=PromotionRequest(
                id=operation_id,
                candidate_pawn=pawn,
                
            )
        )
        return BuildResult.success(verified_form)