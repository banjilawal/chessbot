# src/exchange/service/validation/model/alert/service.py

"""
Module: exchange.service.validation.model.alert.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Alert, AlertBlueprint
from err import AlertCarrierEmptyException, AlertValidationServiceException
from exchange import AlertValidationRequest
from microservice import ValidationMicroservice
from transit import AlertCarrier, AlertValidationDispatcher
from util import LoggingLevelRouter


class AlertValidationService(ValidationMicroservice[Alert]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Alert
                _   AlertBlueprint
            products from AlertValidationService.

    Attributes:
        dispatcher: AlertValidationDispatcher
        
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
            dispatcher: Optional[AlertValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AlertValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AlertValidationDispatcher())
    
    @property
    def dispatcher(self) -> AlertValidationDispatcher:
        return cast(AlertValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: AlertValidationRequest) -> ValidationResult[Alert]:
        """
        Extract an Alert safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Alert from the result then send it to the client.
        Args:
            request: AlertValidationRequest
        Result:
            ValidationResult[Alert]
        Raises:
            AlertValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(AlertCarrier, result.content)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationServiceException.MSG,
                    err_code=AlertValidationServiceException.ERR_CODE,
                    ex=AlertCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AlertCarrierEmptyException.MSG,
                        err_code=AlertCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Alert, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: AlertValidationRequest,
    ) -> ValidationResult[AlertBlueprint]:
        """
        Extract an AlertBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the AlertBlueprint from the result then send it
                to the client.
        Args:
            request: AlertValidationRequest
        Result:
            ValidationResult[AlertBlueprint]
        Raises:
            AlertValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(AlertCarrier, result.content)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationServiceException.MSG,
                    err_code=AlertValidationServiceException.ERR_CODE,
                    ex=AlertCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AlertCarrierEmptyException.MSG,
                        err_code=AlertCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(AlertBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)