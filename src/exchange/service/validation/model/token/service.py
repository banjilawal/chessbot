# src/exchange/service/validation/model/token/service.py

"""
Module: exchange.service.validation.model.token.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TokenValidationResponse, ValidationResult
from domain import Token, TokenBlueprint
from err import TokenValidationServiceException, TokenValidationServiceException, TokenCarrierEmptyException
from exchange import (
    TokenValidationService, ModelValidationService, TokenValidationRequest
)
from util import LoggingLevelRouter


class TokenValidationService(
    ModelValidationService[Token]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Token
                _   TokenBlueprint
            products from TokenValidationService.

    Attributes:
        service: TokenValidationService
        
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
            service: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[TokenValidationService]
        """
        super().__init__(service=service or TokenValidationService())
    
    @property
    def service(self) -> TokenValidationService:
        return cast(TokenValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: TokenValidationRequest,
    ) -> ValidationResult[Token]:
        """
        Extract a Token safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Token from the success response then send it 
                to the client.
        Args:
            request: TokenValidationRequest
        Result:
            ValidationResult[Token]
        Raises:
            TokenValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
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
        response = cast(TokenValidationResponse, result)
        if not response.valid_model:
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
        model = cast(Token, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: TokenValidationRequest,
    ) -> ValidationResult[TokenBlueprint]:
        """
        Extract a TokenBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the TokenBluprint from the success response
                then send it to the client.
        Args:
            request: TokenValidationRequest
        Result:
            ValidationResult[TokenBlueprint]
        Raises:
            TokenValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
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
        response = cast(TokenValidationResponse, result)
        if not response.valid_token:
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
        blueprint = cast(TokenBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)