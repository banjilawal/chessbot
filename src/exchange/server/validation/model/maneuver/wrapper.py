# src/exchange/server/validation/model/maneuver/server.py

"""
Module: exchange.server.validation.model.maneuver.server
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverValidationResponse, ValidationResult
from domain import Maneuver, ManeuverBlueprint
from err import ManeuverValidationResponderException, ManeuverValidationServerException, ManeuverCarrierEmptyException
from exchange import (
    ManeuverValidationResponder, ModelValidationServer, ManeuverValidationRequest
)
from util import LoggingLevelRouter


class ManeuverValidationServer(
    ModelValidationServer[Maneuver]
):
    """
    Role
        -   Server

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
        ValidationServer
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
            ManeuverValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationServerException.MSG,
                    err_code=ManeuverValidationServerException.ERR_CODE,
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
                    ex=ManeuverCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverCarrierEmptyException.MSG,
                        err_code=ManeuverCarrierEmptyException.ERR_CODE,
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
            ManeuverValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationServerException.MSG,
                    err_code=ManeuverValidationServerException.ERR_CODE,
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
                    ex=ManeuverCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverCarrierEmptyException.MSG,
                        err_code=ManeuverCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ManeuverBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)