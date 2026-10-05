# src/exchange/wrapper/validation/struct/chart/coord/wrapper.py

"""
Module: exchange.wrapper.validation.struct.chart.coord.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CoordChartValidationResponse, ValidationResult
from domain import Coord, CoordBlueprint, CoordChart, CoordChartBlueprint
from err import CoordChartValidationResponderException, CoordChartValidationResponseWrapperException, EmptyCoordCarrierException
from exchange import (
    CoordChartValidationResponder, ChartValidationResponseWrapper, CoordChartValidationRequest
)
from util import LoggingLevelRouter


class CoordChartValidationResponseWrapper(
    ChartValidationResponseWrapper[CoordChart]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Coord
                _   CoordBlueprint
            products from CoordChartValidationResponder.

    Attributes:
        responder: CoordChartValidationResponder
        
    Provides:
        -   def extract_model(
                    request: CoordChartValidationRequest
            ) -> ValidationResult[Coord]
            
        -   def extract_blueprint(
                    request: CoordChartValidationRequest
            ) -> ValidationResult[CoordBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[CoordChartValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[CoordChartValidationResponder]
        """
        super().__init__(responder=responder or CoordChartValidationResponder())
    
    @property
    def responder(self) -> CoordChartValidationResponder:
        return cast(CoordChartValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: CoordChartValidationRequest,
    ) -> ValidationResult[CoordChart]:
        """
        Extract a Coord safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Coord from the success response then send it 
                to the client.
        Args:
            request: CoordChartValidationRequest
        Result:
            ValidationResult[Coord]
        Raises:
            CoordChartValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordChartValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordChartValidationResponseWrapperException.MSG,
                    err_code=CoordChartValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordChartValidationResponse, result)
        if not response.valid_chart:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordChartValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordChartValidationResponderException.MSG,
                    err_code=CoordChartValidationResponderException.ERR_CODE,
                    ex=EmptyCoordCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyCoordCarrierException.MSG,
                        err_code=EmptyCoordCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        chart = cast(CoordChart, response.valid_chart)
        return ValidationResult.success(chart)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: CoordChartValidationRequest,
    ) -> ValidationResult[CoordChartBlueprint]:
        """
        Extract a CoordBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the CoordBluprint from the success response
                then send it to the client.
        Args:
            request: CoordChartValidationRequest
        Result:
            ValidationResult[CoordBlueprint]
        Raises:
            CoordChartValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordChartValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordChartValidationResponseWrapperException.MSG,
                    err_code=CoordChartValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordChartValidationResponse, result)
        if not response.valid_coord:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordChartValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordChartValidationResponderException.MSG,
                    err_code=CoordChartValidationResponderException.ERR_CODE,
                    ex=EmptyCoordCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyCoordCarrierException.MSG,
                        err_code=EmptyCoordCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(CoordChartBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)