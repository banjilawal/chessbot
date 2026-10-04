# src/exchange/wrapper/validation/structure/register/coord/wrapper.py

"""
Module: exchange.wrapper.validation.structure.register.coord.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CoordRegisterValidationResponse, ValidationResult
from domain import Coord, CoordBlueprint, CoordRegister, CoordRegisterBlueprint
from err import CoordRegisterValidationResponderException, CoordRegisterValidationResponseWrapperException, EmptyCoordCarrierException
from exchange import (
    CoordRegisterValidationResponder, RegisterValidationResponseWrapper, CoordRegisterValidationRequest
)
from util import LoggingLevelRouter


class CoordRegisterValidationResponseWrapper(
    RegisterValidationResponseWrapper[CoordRegister]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Coord
                _   CoordBlueprint
            products from CoordRegisterValidationResponder.

    Attributes:
        responder: CoordRegisterValidationResponder
        
    Provides:
        -   def extract_register(
                    request: CoordRegisterValidationRequest
            ) -> ValidationResult[Coord]
            
        -   def extract_blueprint(
                    request: CoordRegisterValidationRequest
            ) -> ValidationResult[CoordBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[CoordRegisterValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[CoordRegisterValidationResponder]
        """
        super().__init__(responder=responder or CoordRegisterValidationResponder())
    
    @property
    def responder(self) -> CoordRegisterValidationResponder:
        return cast(CoordRegisterValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_register(
            self, 
            request: CoordRegisterValidationRequest,
    ) -> ValidationResult[CoordRegister]:
        """
        Extract a Coord safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Coord from the success response then send it 
                to the client.
        Args:
            request: CoordRegisterValidationRequest
        Result:
            ValidationResult[Coord]
        Raises:
            CoordRegisterValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_register"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationResponseWrapperException.MSG,
                    err_code=CoordRegisterValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordRegisterValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationResponderException.MSG,
                    err_code=CoordRegisterValidationResponderException.ERR_CODE,
                    ex=EmptyCoordCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyCoordCarrierException.MSG,
                        err_code=EmptyCoordCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        register = cast(CoordRegister, response.valid_model)
        return ValidationResult.success(register)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: CoordRegisterValidationRequest,
    ) -> ValidationResult[CoordRegisterBlueprint]:
        """
        Extract a CoordBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the CoordBluprint from the success response
                then send it to the client.
        Args:
            request: CoordRegisterValidationRequest
        Result:
            ValidationResult[CoordBlueprint]
        Raises:
            CoordRegisterValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_register"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationResponseWrapperException.MSG,
                    err_code=CoordRegisterValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordRegisterValidationResponse, result)
        if not response.valid_coord:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationResponderException.MSG,
                    err_code=CoordRegisterValidationResponderException.ERR_CODE,
                    ex=EmptyCoordCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyCoordCarrierException.MSG,
                        err_code=EmptyCoordCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(CoordRegisterBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)