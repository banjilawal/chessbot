# src/exchange/service/validation/model/token/service.py

"""
Module: exchange.service.validation.model.token.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Token, TokenBlueprint
from err import TokenCarrierEmptyException, TokenValidationServiceException
from exchange import TokenValidationRequest
from microservice import ValidationMicroservice
from transit import TokenCarrier, TokenValidationDispatcher
from util import LoggingLevelRouter


class TokenValidationService(ValidationMicroservice[Token]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Token
                _   TokenBlueprint
            products from TokenValidationService.

    Attributes:
        dispatcher: TokenValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: TokenValidationRequest
            ) -> ValidationResult[Token]
            
        -   def extract_blueprint(
                    request: TokenValidationRequest
            ) -> ValidationResult[TokenBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[TokenValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TokenValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or TokenValidationDispatcher())
    
    @property
    def dispatcher(self) -> TokenValidationDispatcher:
        return cast(TokenValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: TokenValidationRequest) -> ValidationResult[Token]:
        """
        Extract an Token safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Token from the result then send it to the client.
        Args:
            request: TokenValidationRequest
        Result:
            ValidationResult[Token]
        Raises:
            TokenValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationServiceException.MSG,
                    err_code=TokenValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(TokenCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationServiceException.MSG,
                    err_code=TokenValidationServiceException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Token, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: TokenValidationRequest,
    ) -> ValidationResult[TokenBlueprint]:
        """
        Extract an TokenBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the TokenBlueprint from the result then send it
                to the client.
        Args:
            request: TokenValidationRequest
        Result:
            ValidationResult[TokenBlueprint]
        Raises:
            TokenValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationServiceException.MSG,
                    err_code=TokenValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(TokenCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationServiceException.MSG,
                    err_code=TokenValidationServiceException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(TokenBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)