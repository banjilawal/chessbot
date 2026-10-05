# src/exchange/wrapper/validation/struct/register/square/wrapper.py

"""
Module: exchange.wrapper.validation.struct.register.square.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import SquareRegisterValidationResponse, ValidationResult
from domain import Square, SquareBlueprint, SquareRegister, SquareRegisterBlueprint
from err import SquareRegisterValidationResponderException, SquareRegisterValidationResponseWrapperException, EmptySquareCarrierException
from exchange import (
    SquareRegisterValidationResponder, RegisterValidationResponseWrapper, SquareRegisterValidationRequest
)
from util import LoggingLevelRouter


class SquareRegisterValidationResponseWrapper(
    RegisterValidationResponseWrapper[SquareRegister]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Square
                _   SquareBlueprint
            products from SquareRegisterValidationResponder.

    Attributes:
        responder: SquareRegisterValidationResponder
        
    Provides:
        -   def extract_model(
                    request: SquareRegisterValidationRequest
            ) -> ValidationResult[Square]
            
        -   def extract_blueprint(
                    request: SquareRegisterValidationRequest
            ) -> ValidationResult[SquareBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[SquareRegisterValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[SquareRegisterValidationResponder]
        """
        super().__init__(responder=responder or SquareRegisterValidationResponder())
    
    @property
    def responder(self) -> SquareRegisterValidationResponder:
        return cast(SquareRegisterValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: SquareRegisterValidationRequest,
    ) -> ValidationResult[SquareRegister]:
        """
        Extract a Square safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Square from the success response then send it 
                to the client.
        Args:
            request: SquareRegisterValidationRequest
        Result:
            ValidationResult[Square]
        Raises:
            SquareRegisterValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationResponseWrapperException.MSG,
                    err_code=SquareRegisterValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(SquareRegisterValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationResponderException.MSG,
                    err_code=SquareRegisterValidationResponderException.ERR_CODE,
                    ex=EmptySquareCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptySquareCarrierException.MSG,
                        err_code=EmptySquareCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        register = cast(SquareRegister, response.valid_model)
        return ValidationResult.success(register)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: SquareRegisterValidationRequest,
    ) -> ValidationResult[SquareRegisterBlueprint]:
        """
        Extract a SquareBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the SquareBluprint from the success response
                then send it to the client.
        Args:
            request: SquareRegisterValidationRequest
        Result:
            ValidationResult[SquareBlueprint]
        Raises:
            SquareRegisterValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationResponseWrapperException.MSG,
                    err_code=SquareRegisterValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(SquareRegisterValidationResponse, result)
        if not response.valid_square:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationResponderException.MSG,
                    err_code=SquareRegisterValidationResponderException.ERR_CODE,
                    ex=EmptySquareCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptySquareCarrierException.MSG,
                        err_code=EmptySquareCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(SquareRegisterBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)