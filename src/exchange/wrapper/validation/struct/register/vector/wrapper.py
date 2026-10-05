# src/exchange/wrapper/validation/struct/register/vector/wrapper.py

"""
Module: exchange.wrapper.validation.struct.register.vector.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import VectorRegisterValidationResponse, ValidationResult
from domain import Vector, VectorBlueprint, VectorRegister, VectorRegisterBlueprint
from err import VectorRegisterValidationResponderException, VectorRegisterValidationResponseWrapperException, VectorCarrierEmptyException
from exchange import (
    VectorRegisterValidationResponder, RegisterValidationResponseWrapper, VectorRegisterValidationRequest
)
from util import LoggingLevelRouter


class VectorRegisterValidationResponseWrapper(
    RegisterValidationResponseWrapper[VectorRegister]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Vector
                _   VectorBlueprint
            products from VectorRegisterValidationResponder.

    Attributes:
        responder: VectorRegisterValidationResponder
        
    Provides:
        -   def extract_model(
                    request: VectorRegisterValidationRequest
            ) -> ValidationResult[Vector]
            
        -   def extract_blueprint(
                    request: VectorRegisterValidationRequest
            ) -> ValidationResult[VectorBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[VectorRegisterValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[VectorRegisterValidationResponder]
        """
        super().__init__(responder=responder or VectorRegisterValidationResponder())
    
    @property
    def responder(self) -> VectorRegisterValidationResponder:
        return cast(VectorRegisterValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: VectorRegisterValidationRequest,
    ) -> ValidationResult[VectorRegister]:
        """
        Extract a Vector safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Vector from the success response then send it 
                to the client.
        Args:
            request: VectorRegisterValidationRequest
        Result:
            ValidationResult[Vector]
        Raises:
            VectorRegisterValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationResponseWrapperException.MSG,
                    err_code=VectorRegisterValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorRegisterValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationResponderException.MSG,
                    err_code=VectorRegisterValidationResponderException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        register = cast(VectorRegister, response.valid_model)
        return ValidationResult.success(register)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: VectorRegisterValidationRequest,
    ) -> ValidationResult[VectorRegisterBlueprint]:
        """
        Extract a VectorBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the VectorBluprint from the success response
                then send it to the client.
        Args:
            request: VectorRegisterValidationRequest
        Result:
            ValidationResult[VectorBlueprint]
        Raises:
            VectorRegisterValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationResponseWrapperException.MSG,
                    err_code=VectorRegisterValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorRegisterValidationResponse, result)
        if not response.valid_vector:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationResponderException.MSG,
                    err_code=VectorRegisterValidationResponderException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(VectorRegisterBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)