# src/exchange/wrapper/validation/model/alert/wrapper.py

"""
Module: exchange.wrapper.validation.model.alert.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AlertValidationResponse, ValidationResult
from domain import Alert, AlertBlueprint
from err import AlertValidationResponderException, AlertValidationServerException, EmptyAlertCarrierException
from exchange import (
    AlertValidationResponder, ModelValidationServer, AlertValidationRequest
)
from util import LoggingLevelRouter


class AlertValidationServer(
    ModelValidationServer[Alert]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Alert
                _   AlertBlueprint
            products from AlertValidationResponder.

    Attributes:
        responder: AlertValidationResponder
        
    Provides:
        -   def extract_model(
                    request: AlertValidationRequest
            ) -> ValidationResult[Alert]
            
        -   def extract_blueprint(
                    request: AlertValidationRequest
            ) -> ValidationResult[AlertBlueprint]

    Super Class:
        ValidationServer
    """
    
    def __init__(
            self,
            responder: Optional[AlertValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[AlertValidationResponder]
        """
        super().__init__(responder=responder or AlertValidationResponder())
    
    @property
    def responder(self) -> AlertValidationResponder:
        return cast(AlertValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: AlertValidationRequest,
    ) -> ValidationResult[Alert]:
        """
        Extract a Alert safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Alert from the success response then send it 
                to the client.
        Args:
            request: AlertValidationRequest
        Result:
            ValidationResult[Alert]
        Raises:
            AlertValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationServerException.MSG,
                    err_code=AlertValidationServerException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AlertValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationResponderException.MSG,
                    err_code=AlertValidationResponderException.ERR_CODE,
                    ex=EmptyAlertCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyAlertCarrierException.MSG,
                        err_code=EmptyAlertCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Alert, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: AlertValidationRequest,
    ) -> ValidationResult[AlertBlueprint]:
        """
        Extract a AlertBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the AlertBluprint from the success response
                then send it to the client.
        Args:
            request: AlertValidationRequest
        Result:
            ValidationResult[AlertBlueprint]
        Raises:
            AlertValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationServerException.MSG,
                    err_code=AlertValidationServerException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AlertValidationResponse, result)
        if not response.valid_alert:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationResponderException.MSG,
                    err_code=AlertValidationResponderException.ERR_CODE,
                    ex=EmptyAlertCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyAlertCarrierException.MSG,
                        err_code=EmptyAlertCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(AlertBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)