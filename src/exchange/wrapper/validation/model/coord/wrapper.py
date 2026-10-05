# src/exchange/wrapper/validation/model/coord/wrapper.py

"""
Module: exchange.wrapper.validation.model.coord.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CoordValidationResponse, ValidationResult
from domain import Coord, CoordBlueprint
from err import CoordValidationResponderException, CoordValidationResponseWrapperException, CoordCarrierEmptyException
from exchange import (
    CoordValidationResponder, ModelValidationResponseWrapper, CoordValidationRequest
)
from util import LoggingLevelRouter


class CoordValidationResponseWrapper(
    ModelValidationResponseWrapper[Coord]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Coord
                _   CoordBlueprint
            products from CoordValidationResponder.

    Attributes:
        responder: CoordValidationResponder
        
    Provides:
        -   def extract_model(
                    request: CoordValidationRequest
            ) -> ValidationResult[Coord]
            
        -   def extract_blueprint(
                    request: CoordValidationRequest
            ) -> ValidationResult[CoordBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[CoordValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[CoordValidationResponder]
        """
        super().__init__(responder=responder or CoordValidationResponder())
    
    @property
    def responder(self) -> CoordValidationResponder:
        return cast(CoordValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: CoordValidationRequest,
    ) -> ValidationResult[Coord]:
        """
        Extract a Coord safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Coord from the success response then send it 
                to the client.
        Args:
            request: CoordValidationRequest
        Result:
            ValidationResult[Coord]
        Raises:
            CoordValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidationResponseWrapperException.MSG,
                    err_code=CoordValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidationResponderException.MSG,
                    err_code=CoordValidationResponderException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Coord, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: CoordValidationRequest,
    ) -> ValidationResult[CoordBlueprint]:
        """
        Extract a CoordBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the CoordBluprint from the success response
                then send it to the client.
        Args:
            request: CoordValidationRequest
        Result:
            ValidationResult[CoordBlueprint]
        Raises:
            CoordValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidationResponseWrapperException.MSG,
                    err_code=CoordValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordValidationResponse, result)
        if not response.valid_coord:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidationResponderException.MSG,
                    err_code=CoordValidationResponderException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(CoordBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)