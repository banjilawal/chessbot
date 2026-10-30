# src/exchange/service/validation/context/alert/service.py

"""
Module: exchange.service.validation.context.alert.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AlertValidationResponse, ValidationResult
from domain import Alert, AlertBlueprint
from err import AlertContextValidationServiceException, AlertContextValidationServiceException, EmptyAlertCarrierException
from exchange import (
    AlertContextValidationService, ContextValidationService, AlertValidationRequest
)
from util import LoggingLevelRouter


class AlertContextValidationService(
    ContextValidationService[Alert]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Alert
                _   AlertBlueprint
            products from AlertContextValidationService.

    Attributes:
        service: AlertContextValidationService
        
    Provides:
        -   def extract_context(
                    request: AlertValidationRequest
            ) -> ValidationResult[Alert]
            
        -   def extract_blueprint(
                    request: AlertValidationRequest
            ) -> ValidationResult[AlertBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[AlertContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[AlertContextValidationService]
        """
        super().__init__(service=service or AlertContextValidationService())
    
    @property
    def service(self) -> AlertContextValidationService:
        return cast(AlertContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
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
            AlertContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertContextValidationServiceException.MSG,
                    err_code=AlertContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AlertValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertContextValidationServiceException.MSG,
                    err_code=AlertContextValidationServiceException.ERR_CODE,
                    ex=EmptyAlertCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyAlertCarrierException.MSG,
                        err_code=EmptyAlertCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Alert, response.valid_context)
        return ValidationResult.success(context)
    
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
            AlertContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertContextValidationServiceException.MSG,
                    err_code=AlertContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AlertValidationResponse, result)
        if not response.valid_alert:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertContextValidationServiceException.MSG,
                    err_code=AlertContextValidationServiceException.ERR_CODE,
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