# src/client/validation/model/maneuver/client.py

"""
Module: client.validation.model.maneuver.client
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, ManeuverValidationResponse
from client import ModelValidatorClient, ManeuverValidationRequest
from domain import Maneuver
from err import ManeuverValidatorClientException
from transit import ManeuverCarrier, ManeuverValidationDispatcher
from util import LoggingLevelRouter


class ManeuverValidatorClient(ModelValidatorClient[Maneuver]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Maneuver validation Request-Response workflow.

    Attributes:
        dispatcher: ManeuverValidationDispatcher[T]

    Provides:
        -   def submit(request: ManeuverValidationRequest[T]) -> ManeuverValidationResponse[T]

    Super Class:
        ModelValidatorClient
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ManeuverValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ManeuverValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ManeuverValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> ManeuverValidationDispatcher:
        return cast(ManeuverValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def transmit(
            self,
            request: ManeuverValidationRequest
    ) -> ManeuverValidationResponse:
        """
        Certify a candidate is a ManeuverCarrier whose payload is either a Maneuver
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ManeuverValidationRequest
        Result:
            ManeuverValidationResponse
        Raises:
            ManeuverValidatorClientException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ManeuverValidationResponse.failure(
                request=request,
                result=result,
                exception=ManeuverValidatorClientException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorClientException.MSG,
                    err_code=ManeuverValidatorClientException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ManeuverCarrier, result.payload)
        return ManeuverValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )