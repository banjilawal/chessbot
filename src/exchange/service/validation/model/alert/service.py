# src/exchange/service/validation/model/alert/service.py

"""
Module: exchange.service.validation.model.alert.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AlertValidationResponse, ValidationResult
from domain import Alert, AlertBlueprint
from err import AlertValidationServiceException, AlertValidationServiceException, EmptyAlertCarrierException
from exchange import (
    AlertValidationService, ModelValidationService, AlertValidationRequest
)
from util import LoggingLevelRouter


class AlertValidationService(
    ModelValidationService[Alert]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Alert
                _   AlertBlueprint
            products from AlertValidationService.

    Attributes:
        service: AlertValidationService
        
    Provides:
        -   def extract_model(
                    request: AlertValidationRequest
            ) -> ValidationResult[Alert]
            
        -   def extract_blueprint(
                    request: AlertValidationRequest
            ) -> ValidationResult[AlertBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[AlertValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[AlertValidationService]
        """
        super().__init__(service=service or AlertValidationService())
    
    @property
    def service(self) -> AlertValidationService:
        return cast(AlertValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: AlertValidationRequest,
    ) -> ValidationResult[Alert]:
        """
        Extract a Alert safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Alert from the success response then send it 
                to the client.
        Args:
            request: AlertValidationRequest
        Result:
            ValidationResult[Alert]
        Raises:
            AlertValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationServiceException.MSG,
                    err_code=AlertValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AlertValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationServiceException.MSG,
                    err_code=AlertValidationServiceException.ERR_CODE,
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
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the AlertBluprint from the success response
                then send it to the client.
        Args:
            request: AlertValidationRequest
        Result:
            ValidationResult[AlertBlueprint]
        Raises:
            AlertValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationServiceException.MSG,
                    err_code=AlertValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AlertValidationResponse, result)
        if not response.valid_alert:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationServiceException.MSG,
                    err_code=AlertValidationServiceException.ERR_CODE,
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