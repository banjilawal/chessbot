# src/exchange/wrapper/validation/model/token/wrapper.py

"""
Module: exchange.wrapper.validation.model.token.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TokenValidationResponse, ValidationResult
from domain import Token, TokenBlueprint
from err import TokenValidationResponderException, TokenValidationResponseWrapperException, TokenCarrierEmptyException
from exchange import (
    TokenValidationResponder, ModelValidationResponseWrapper, TokenValidationRequest
)
from util import LoggingLevelRouter


class TokenValidationResponseWrapper(
    ModelValidationResponseWrapper[Token]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Token
                _   TokenBlueprint
            products from TokenValidationResponder.

    Attributes:
        responder: TokenValidationResponder
        
    Provides:
        -   def extract_model(
                    request: TokenValidationRequest
            ) -> ValidationResult[Token]
            
        -   def extract_blueprint(
                    request: TokenValidationRequest
            ) -> ValidationResult[TokenBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[TokenValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[TokenValidationResponder]
        """
        super().__init__(responder=responder or TokenValidationResponder())
    
    @property
    def responder(self) -> TokenValidationResponder:
        return cast(TokenValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: TokenValidationRequest,
    ) -> ValidationResult[Token]:
        """
        Extract a Token safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Token from the success response then send it 
                to the client.
        Args:
            request: TokenValidationRequest
        Result:
            ValidationResult[Token]
        Raises:
            TokenValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationResponseWrapperException.MSG,
                    err_code=TokenValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TokenValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationResponderException.MSG,
                    err_code=TokenValidationResponderException.ERR_CODE,
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
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the TokenBluprint from the success response
                then send it to the client.
        Args:
            request: TokenValidationRequest
        Result:
            ValidationResult[TokenBlueprint]
        Raises:
            TokenValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationResponseWrapperException.MSG,
                    err_code=TokenValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TokenValidationResponse, result)
        if not response.valid_token:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationResponderException.MSG,
                    err_code=TokenValidationResponderException.ERR_CODE,
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