# src/exchange/wrapper/validation/model/maneuver/wrapper.py

"""
Module: exchange.wrapper.validation.model.maneuver.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverValidationResponse, ValidationResult
from domain import Maneuver, ManeuverBlueprint
from err import ManeuverValidationResponderException, ManeuverValidationResponseWrapperException, EmptyManeuverCarrierException
from exchange import (
    ManeuverValidationResponder, ModelValidationResponseWrapper, ManeuverValidationRequest
)
from util import LoggingLevelRouter


class ManeuverValidationResponseWrapper(
    ModelValidationResponseWrapper[Maneuver]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Maneuver
                _   ManeuverBlueprint
            products from ManeuverValidationResponder.

    Attributes:
        responder: ManeuverValidationResponder
        
    Provides:
        -   def extract_model(
                    request: ManeuverValidationRequest
            ) -> ValidationResult[Maneuver]
            
        -   def extract_blueprint(
                    request: ManeuverValidationRequest
            ) -> ValidationResult[ManeuverBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[ManeuverValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[ManeuverValidationResponder]
        """
        super().__init__(responder=responder or ManeuverValidationResponder())
    
    @property
    def responder(self) -> ManeuverValidationResponder:
        return cast(ManeuverValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: ManeuverValidationRequest,
    ) -> ValidationResult[Maneuver]:
        """
        Extract a Maneuver safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Maneuver from the success response then send it 
                to the client.
        Args:
            request: ManeuverValidationRequest
        Result:
            ValidationResult[Maneuver]
        Raises:
            ManeuverValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationResponseWrapperException.MSG,
                    err_code=ManeuverValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ManeuverValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationResponderException.MSG,
                    err_code=ManeuverValidationResponderException.ERR_CODE,
                    ex=EmptyManeuverCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyManeuverCarrierException.MSG,
                        err_code=EmptyManeuverCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Maneuver, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: ManeuverValidationRequest,
    ) -> ValidationResult[ManeuverBlueprint]:
        """
        Extract a ManeuverBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the ManeuverBluprint from the success response
                then send it to the client.
        Args:
            request: ManeuverValidationRequest
        Result:
            ValidationResult[ManeuverBlueprint]
        Raises:
            ManeuverValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationResponseWrapperException.MSG,
                    err_code=ManeuverValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ManeuverValidationResponse, result)
        if not response.valid_maneuver:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationResponderException.MSG,
                    err_code=ManeuverValidationResponderException.ERR_CODE,
                    ex=EmptyManeuverCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyManeuverCarrierException.MSG,
                        err_code=EmptyManeuverCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ManeuverBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)