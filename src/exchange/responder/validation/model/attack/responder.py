# src/exchange/responder/validation/model/attack/exchange.py

"""
Module: exchange.responder.validation.model.attack.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, AttackValidationResponse
from exchange import ModelValidationResponder, AttackValidationRequest
from domain import Encounter
from err import AttackValidationResponderException
from transit import AttackCarrier, AttackValidationDispatcher
from util import LoggingLevelRouter


class AttackValidationResponder(ModelValidationResponder[Encounter]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Attack validation Request-Response workflow.

    Attributes:
        dispatcher: AttackValidationDispatcher[T]

    Provides:
        -   def submit(request: AttackValidationRequest[T]) -> AttackValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[AttackValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AttackValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or AttackValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> AttackValidationDispatcher:
        return cast(AttackValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: AttackValidationRequest
    ) -> AttackValidationResponse:
        """
        Certify a candidate is a AttackCarrier whose payload is either a Attack
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: AttackValidationRequest
        Result:
            AttackValidationResponse
        Raises:
            AttackValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return AttackValidationResponse.failure(
                request=request,
                result=result,
                exception=AttackValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationResponderException.MSG,
                    err_code=AttackValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(AttackCarrier, result.payload)
        return AttackValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )