# src/exchange/responder/authorization/model/encounter/responder.py

"""
Module: exchange.responder.authorization.model.encounter.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, EncounterDecision
from exchange import ModelAuthorizationResponder, EncounterAuthorizationRequest
from domain import Encounter
from err import EncounterAuthorizationResponderException
from transit import EncounterCarrier, EncounterAuthorizationDispatcher
from util import LoggingLevelRouter


class EncounterAuthorizationResponder(ModelAuthorizationResponder[Encounter]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Encounter authorization Request-Response workflow.

    Attributes:
        dispatcher: EncounterAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: EncounterAuthorizationRequest[T]) -> EncounterDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[EncounterAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[EncounterAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or EncounterAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> EncounterAuthorizationDispatcher:
        return cast(EncounterAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: EncounterAuthorizationRequest
    ) -> EncounterDecision:
        """
        Certify a candidate is a EncounterCarrier whose payload is either a Encounter
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: EncounterAuthorizationRequest
        Result:
            EncounterDecision
        Raises:
            EncounterAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return EncounterDecision.failure(
                request=request,
                result=result,
                exception=EncounterAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterAuthorizationResponderException.MSG,
                    err_code=EncounterAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(EncounterCarrier, result.payload)
        return EncounterDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )