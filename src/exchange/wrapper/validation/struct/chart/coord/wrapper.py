# src/exchange/wrapper/validation/struct/chart/footstep/wrapper.py

"""
Module: exchange.wrapper.validation.struct.chart.footstep.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import FootstepValidationResponse, ValidationResult
from domain import Coord, CoordBlueprint, Footstep, FootstepBlueprint
from err import FootstepValidationResponderException, FootstepValidationResponseWrapperException, CoordCarrierEmptyException
from exchange import (
    FootstepValidationResponder, ChartValidationResponseWrapper, FootstepValidationRequest
)
from util import LoggingLevelRouter


class FootstepValidationResponseWrapper(
    ChartValidationResponseWrapper[Footstep]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Coord
                _   CoordBlueprint
            products from FootstepValidationResponder.

    Attributes:
        responder: FootstepValidationResponder
        
    Provides:
        -   def extract_model(
                    request: FootstepValidationRequest
            ) -> ValidationResult[Coord]
            
        -   def extract_blueprint(
                    request: FootstepValidationRequest
            ) -> ValidationResult[CoordBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[FootstepValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[FootstepValidationResponder]
        """
        super().__init__(responder=responder or FootstepValidationResponder())
    
    @property
    def responder(self) -> FootstepValidationResponder:
        return cast(FootstepValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: FootstepValidationRequest,
    ) -> ValidationResult[Footstep]:
        """
        Extract a Coord safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Coord from the success response then send it 
                to the client.
        Args:
            request: FootstepValidationRequest
        Result:
            ValidationResult[Coord]
        Raises:
            FootstepValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationResponseWrapperException.MSG,
                    err_code=FootstepValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(FootstepValidationResponse, result)
        if not response.valid_chart:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationResponderException.MSG,
                    err_code=FootstepValidationResponderException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        chart = cast(Footstep, response.valid_chart)
        return ValidationResult.success(chart)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: FootstepValidationRequest,
    ) -> ValidationResult[FootstepBlueprint]:
        """
        Extract a CoordBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the CoordBluprint from the success response
                then send it to the client.
        Args:
            request: FootstepValidationRequest
        Result:
            ValidationResult[CoordBlueprint]
        Raises:
            FootstepValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationResponseWrapperException.MSG,
                    err_code=FootstepValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(FootstepValidationResponse, result)
        if not response.valid_coord:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationResponderException.MSG,
                    err_code=FootstepValidationResponderException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(FootstepBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)