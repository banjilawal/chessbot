# src/exchange/responder/validation/model/encounter/responder.py

"""
Module: exchange.responder.validation.model.encounter.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, EncounterValidationResponse
from exchange import ModelValidationResponder, EncounterValidationRequest
from domain import Encounter
from err import EncounterValidationResponderException
from transit import EncounterCarrier, EncounterValidationDispatcher
from util import LoggingLevelRouter


class EncounterValidationResponder(ModelValidationResponder[Encounter]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Encounter validation Request-Response workflow.

    Attributes:
        dispatcher: EncounterValidationDispatcher[T]

    Provides:
        -   def submit(request: EncounterValidationRequest[T]) -> EncounterValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[EncounterValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[EncounterValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or EncounterValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> EncounterValidationDispatcher:
        return cast(EncounterValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: EncounterValidationRequest
    ) -> EncounterValidationResponse:
        """
        Certify a candidate is a EncounterCarrier whose payload is either a Encounter
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: EncounterValidationRequest
        Result:
            EncounterValidationResponse
        Raises:
            EncounterValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return EncounterValidationResponse.failure(
                request=request,
                result=result,
                exception=EncounterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationResponderException.MSG,
                    err_code=EncounterValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(EncounterCarrier, result.payload)
        return EncounterValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )