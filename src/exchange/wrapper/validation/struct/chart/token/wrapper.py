# src/exchange/wrapper/validation/struct/chart/token/wrapper.py

"""
Module: exchange.wrapper.validation.struct.chart.token.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TokenChartValidationResponse, ValidationResult
from domain import Token, TokenBlueprint, TokenChart, TokenChartBlueprint
from err import TokenChartValidationResponderException, TokenChartValidationResponseWrapperException, TokenCarrierEmptyException
from exchange import (
    TokenChartValidationResponder, ChartValidationResponseWrapper, TokenChartValidationRequest
)
from util import LoggingLevelRouter


class TokenChartValidationResponseWrapper(
    ChartValidationResponseWrapper[TokenChart]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Token
                _   TokenBlueprint
            products from TokenChartValidationResponder.

    Attributes:
        responder: TokenChartValidationResponder
        
    Provides:
        -   def extract_model(
                    request: TokenChartValidationRequest
            ) -> ValidationResult[Token]
            
        -   def extract_blueprint(
                    request: TokenChartValidationRequest
            ) -> ValidationResult[TokenBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[TokenChartValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[TokenChartValidationResponder]
        """
        super().__init__(responder=responder or TokenChartValidationResponder())
    
    @property
    def responder(self) -> TokenChartValidationResponder:
        return cast(TokenChartValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: TokenChartValidationRequest,
    ) -> ValidationResult[TokenChart]:
        """
        Extract a Token safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Token from the success response then send it 
                to the client.
        Args:
            request: TokenChartValidationRequest
        Result:
            ValidationResult[Token]
        Raises:
            TokenChartValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenChartValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenChartValidationResponseWrapperException.MSG,
                    err_code=TokenChartValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TokenChartValidationResponse, result)
        if not response.valid_chart:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenChartValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenChartValidationResponderException.MSG,
                    err_code=TokenChartValidationResponderException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        chart = cast(TokenChart, response.valid_chart)
        return ValidationResult.success(chart)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: TokenChartValidationRequest,
    ) -> ValidationResult[TokenChartBlueprint]:
        """
        Extract a TokenBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the TokenBluprint from the success response
                then send it to the client.
        Args:
            request: TokenChartValidationRequest
        Result:
            ValidationResult[TokenBlueprint]
        Raises:
            TokenChartValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenChartValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenChartValidationResponseWrapperException.MSG,
                    err_code=TokenChartValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TokenChartValidationResponse, result)
        if not response.valid_token:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenChartValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenChartValidationResponderException.MSG,
                    err_code=TokenChartValidationResponderException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(TokenChartBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)