# src/exchange/service/validation/context/token/service.py

"""
Module: exchange.service.validation.context.token.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TokenValidationResponse, ValidationResult
from domain import Token, TokenBlueprint
from err import TokenContextValidationServiceException, TokenContextValidationServiceException, TokenCarrierEmptyException
from exchange import (
    TokenContextValidationService, ContextValidationService, TokenValidationRequest
)
from util import LoggingLevelRouter


class TokenContextValidationService(
    ContextValidationService[Token]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Token
                _   TokenBlueprint
            products from TokenContextValidationService.

    Attributes:
        service: TokenContextValidationService
        
    Provides:
        -   def extract_context(
                    request: TokenValidationRequest
            ) -> ValidationResult[Token]
            
        -   def extract_blueprint(
                    request: TokenValidationRequest
            ) -> ValidationResult[TokenBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[TokenContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[TokenContextValidationService]
        """
        super().__init__(service=service or TokenContextValidationService())
    
    @property
    def service(self) -> TokenContextValidationService:
        return cast(TokenContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
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
            TokenContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationServiceException.MSG,
                    err_code=TokenContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TokenValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationServiceException.MSG,
                    err_code=TokenContextValidationServiceException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Token, response.valid_context)
        return ValidationResult.success(context)
    
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
            TokenContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationServiceException.MSG,
                    err_code=TokenContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TokenValidationResponse, result)
        if not response.valid_token:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationServiceException.MSG,
                    err_code=TokenContextValidationServiceException.ERR_CODE,
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