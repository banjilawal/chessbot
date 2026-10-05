# src/exchange/wrapper/validation/struct/chart/walk/wrapper.py

"""
Module: exchange.wrapper.validation.struct.chart.walk.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import WalkValidationResponse, ValidationResult
from domain import Coord, CoordBlueprint, Walk, WalkBlueprint
from err import WalkValidationResponderException, WalkValidationResponseWrapperException, CoordCarrierEmptyException
from exchange import (
    WalkValidationResponder, ChartValidationResponseWrapper, WalkValidationRequest
)
from util import LoggingLevelRouter


class WalkValidationResponseWrapper(
    ChartValidationResponseWrapper[Walk]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Coord
                _   CoordBlueprint
            products from WalkValidationResponder.

    Attributes:
        responder: WalkValidationResponder
        
    Provides:
        -   def extract_model(
                    request: WalkValidationRequest
            ) -> ValidationResult[Coord]
            
        -   def extract_blueprint(
                    request: WalkValidationRequest
            ) -> ValidationResult[CoordBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[WalkValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[WalkValidationResponder]
        """
        super().__init__(responder=responder or WalkValidationResponder())
    
    @property
    def responder(self) -> WalkValidationResponder:
        return cast(WalkValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: WalkValidationRequest,
    ) -> ValidationResult[Walk]:
        """
        Extract a Coord safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Coord from the success response then send it 
                to the client.
        Args:
            request: WalkValidationRequest
        Result:
            ValidationResult[Coord]
        Raises:
            WalkValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkValidationResponseWrapperException.MSG,
                    err_code=WalkValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(WalkValidationResponse, result)
        if not response.valid_chart:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkValidationResponderException.MSG,
                    err_code=WalkValidationResponderException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        chart = cast(Walk, response.valid_chart)
        return ValidationResult.success(chart)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: WalkValidationRequest,
    ) -> ValidationResult[WalkBlueprint]:
        """
        Extract a CoordBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the CoordBluprint from the success response
                then send it to the client.
        Args:
            request: WalkValidationRequest
        Result:
            ValidationResult[CoordBlueprint]
        Raises:
            WalkValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkValidationResponseWrapperException.MSG,
                    err_code=WalkValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(WalkValidationResponse, result)
        if not response.valid_coord:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkValidationResponderException.MSG,
                    err_code=WalkValidationResponderException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(WalkBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)