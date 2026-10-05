# src/exchange/responder/validation/struct/node/warning/exchange.py

"""
Module: exchange.responder.validation.struct.node.warning.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, EncounterWaningNodeValidationResponse
from domain import EncounterWaningNode
from exchange import NodeValidationResponder, EncounterWaningNodeValidationRequest
from err import EncounterWaningNodeValidationResponderException
from transit import WarningCarrier, EncounterWaningNodeCarrier, EncounterWaningNodeValidationDispatcher
from util import LoggingLevelRouter


class EncounterWaningNodeValidationResponder(NodeValidationResponder[EncounterWaningNode]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the EncounterWaningNode validation Request-Response workflow.

    Attributes:
        dispatcher: EncounterWaningNodeValidationDispatcher[T]

    Provides:
        -   def submit(request: EncounterWaningNodeValidationRequest[T]) -> EncounterWaningNodeValidationResponse[T]

    Super Class:
        NodeValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[EncounterWaningNodeValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[EncounterWaningNodeValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or EncounterWaningNodeValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> EncounterWaningNodeValidationDispatcher:
        return cast(EncounterWaningNodeValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: EncounterWaningNodeValidationRequest
    ) -> EncounterWaningNodeValidationResponse:
        """
        Certify a candidate is a WarningCarrier whose payload is either a Warning
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: EncounterWaningNodeValidationRequest
        Result:
            EncounterWaningNodeValidationResponse
        Raises:
            WarningValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return EncounterWaningNodeValidationResponse.failure(
                request=request,
                result=result,
                exception=EncounterWaningNodeValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWaningNodeValidationResponderException.MSG,
                    err_code=EncounterWaningNodeValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(EncounterWaningNodeCarrier, result.payload)
        return EncounterWaningNodeValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )