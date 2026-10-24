# src/exchange/server/validation/struct/register/square/server.py

"""
Module: exchange.server.validation.struct.register.square.server
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import SquareRegisterValidationResponse, ValidationResult
from domain import Square, SquareBlueprint, SquareRegister, SquareRegisterBlueprint
from err import SquareRegisterValidationResponderException, SquareRegisterValidationServerException, SquareCarrierEmptyException
from exchange import (
    SquareRegisterValidationResponder, RegisterValidationService, SquareRegisterValidationRequest
)
from util import LoggingLevelRouter


class SquareRegisterValidationServer(
    RegisterValidationService[SquareRegister]
):
    """
    Role
        -   Server

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
        ValidationServer
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
            SquareRegisterValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServerException.MSG,
                    err_code=SquareRegisterValidationServerException.ERR_CODE,
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
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
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
            SquareRegisterValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServerException.MSG,
                    err_code=SquareRegisterValidationServerException.ERR_CODE,
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
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(SquareRegisterBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)