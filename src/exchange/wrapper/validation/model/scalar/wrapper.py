# src/exchange/wrapper/validation/model/scalar/wrapper.py

"""
Module: exchange.wrapper.validation.model.scalar.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ScalarValidationResponse, ValidationResult
from domain import Scalar, ScalarBlueprint
from err import ScalarValidationResponderException, ScalarValidationResponseWrapperException, EmptyScalarCarrierException
from exchange import (
    ScalarValidationResponder, ModelValidationResponseWrapper, ScalarValidationRequest
)
from util import LoggingLevelRouter


class ScalarValidationResponseWrapper(
    ModelValidationResponseWrapper[Scalar]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Scalar
                _   ScalarBlueprint
            products from ScalarValidationResponder.

    Attributes:
        responder: ScalarValidationResponder
        
    Provides:
        -   def extract_model(
                    request: ScalarValidationRequest
            ) -> ValidationResult[Scalar]
            
        -   def extract_blueprint(
                    request: ScalarValidationRequest
            ) -> ValidationResult[ScalarBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[ScalarValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[ScalarValidationResponder]
        """
        super().__init__(responder=responder or ScalarValidationResponder())
    
    @property
    def responder(self) -> ScalarValidationResponder:
        return cast(ScalarValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: ScalarValidationRequest,
    ) -> ValidationResult[Scalar]:
        """
        Extract a Scalar safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Scalar from the success response then send it 
                to the client.
        Args:
            request: ScalarValidationRequest
        Result:
            ValidationResult[Scalar]
        Raises:
            ScalarValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationResponseWrapperException.MSG,
                    err_code=ScalarValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ScalarValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationResponderException.MSG,
                    err_code=ScalarValidationResponderException.ERR_CODE,
                    ex=EmptyScalarCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyScalarCarrierException.MSG,
                        err_code=EmptyScalarCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Scalar, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: ScalarValidationRequest,
    ) -> ValidationResult[ScalarBlueprint]:
        """
        Extract a ScalarBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the ScalarBluprint from the success response
                then send it to the client.
        Args:
            request: ScalarValidationRequest
        Result:
            ValidationResult[ScalarBlueprint]
        Raises:
            ScalarValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationResponseWrapperException.MSG,
                    err_code=ScalarValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ScalarValidationResponse, result)
        if not response.valid_scalar:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationResponderException.MSG,
                    err_code=ScalarValidationResponderException.ERR_CODE,
                    ex=EmptyScalarCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyScalarCarrierException.MSG,
                        err_code=EmptyScalarCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ScalarBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)