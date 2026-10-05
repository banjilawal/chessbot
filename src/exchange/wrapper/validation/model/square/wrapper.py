# src/exchange/wrapper/validation/model/square/wrapper.py

"""
Module: exchange.wrapper.validation.model.square.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import SquareValidationResponse, ValidationResult
from domain import Square, SquareBlueprint
from err import SquareValidationResponderException, SquareValidationResponseWrapperException, SquareCarrierEmptyException
from exchange import (
    SquareValidationResponder, ModelValidationResponseWrapper, SquareValidationRequest
)
from util import LoggingLevelRouter


class SquareValidationResponseWrapper(
    ModelValidationResponseWrapper[Square]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Square
                _   SquareBlueprint
            products from SquareValidationResponder.

    Attributes:
        responder: SquareValidationResponder
        
    Provides:
        -   def extract_model(
                    request: SquareValidationRequest
            ) -> ValidationResult[Square]
            
        -   def extract_blueprint(
                    request: SquareValidationRequest
            ) -> ValidationResult[SquareBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[SquareValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[SquareValidationResponder]
        """
        super().__init__(responder=responder or SquareValidationResponder())
    
    @property
    def responder(self) -> SquareValidationResponder:
        return cast(SquareValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: SquareValidationRequest,
    ) -> ValidationResult[Square]:
        """
        Extract a Square safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Square from the success response then send it 
                to the client.
        Args:
            request: SquareValidationRequest
        Result:
            ValidationResult[Square]
        Raises:
            SquareValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationResponseWrapperException.MSG,
                    err_code=SquareValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(SquareValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationResponderException.MSG,
                    err_code=SquareValidationResponderException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Square, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: SquareValidationRequest,
    ) -> ValidationResult[SquareBlueprint]:
        """
        Extract a SquareBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the SquareBluprint from the success response
                then send it to the client.
        Args:
            request: SquareValidationRequest
        Result:
            ValidationResult[SquareBlueprint]
        Raises:
            SquareValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationResponseWrapperException.MSG,
                    err_code=SquareValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(SquareValidationResponse, result)
        if not response.valid_square:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationResponderException.MSG,
                    err_code=SquareValidationResponderException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(SquareBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)