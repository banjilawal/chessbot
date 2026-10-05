# src/exchange/wrapper/validation/struct/chart/participate/wrapper.py

"""
Module: exchange.wrapper.validation.struct.chart.participate.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ParticipationValidationResponse, ValidationResult
from domain import Token, TokenBlueprint, Participation, ParticipationBlueprint
from err import ParticipationValidationResponderException, ParticipationValidationResponseWrapperException, TokenCarrierEmptyException
from exchange import (
    ParticipationValidationResponder, ChartValidationResponseWrapper, WalkValidationRequest
)
from util import LoggingLevelRouter


class ParticipationValidationResponseWrapper(
    ChartValidationResponseWrapper[Participation]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Token
                _   TokenBlueprint
            products from ParticipationValidationResponder.

    Attributes:
        responder: ParticipationValidationResponder
        
    Provides:
        -   def extract_model(
                    request: ParticipationValidationRequest
            ) -> ValidationResult[Token]
            
        -   def extract_blueprint(
                    request: ParticipationValidationRequest
            ) -> ValidationResult[TokenBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[ParticipationValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[ParticipationValidationResponder]
        """
        super().__init__(responder=responder or ParticipationValidationResponder())
    
    @property
    def responder(self) -> ParticipationValidationResponder:
        return cast(ParticipationValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: WalkValidationRequest,
    ) -> ValidationResult[Participation]:
        """
        Extract a Token safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Token from the success response then send it 
                to the client.
        Args:
            request: ParticipationValidationRequest
        Result:
            ValidationResult[Token]
        Raises:
            ParticipationValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationResponseWrapperException.MSG,
                    err_code=ParticipationValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ParticipationValidationResponse, result)
        if not response.valid_chart:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationResponderException.MSG,
                    err_code=ParticipationValidationResponderException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        chart = cast(Participation, response.valid_chart)
        return ValidationResult.success(chart)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: WalkValidationRequest,
    ) -> ValidationResult[ParticipationBlueprint]:
        """
        Extract a TokenBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the TokenBluprint from the success response
                then send it to the client.
        Args:
            request: ParticipationValidationRequest
        Result:
            ValidationResult[TokenBlueprint]
        Raises:
            ParticipationValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationResponseWrapperException.MSG,
                    err_code=ParticipationValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ParticipationValidationResponse, result)
        if not response.valid_token:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationResponderException.MSG,
                    err_code=ParticipationValidationResponderException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ParticipationBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)