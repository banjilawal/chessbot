# src/exchange/responder/authorization/model/maneuver/responder.py

"""
Module: exchange.responder.authorization.model.maneuver.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, ManeuverDecision
from exchange import ModelAuthorizationResponder, ManeuverAuthorizationRequest
from domain import Maneuver
from err import ManeuverAuthorizationResponderException
from transit import ManeuverCarrier, ManeuverAuthorizationDispatcher
from util import LoggingLevelRouter


class ManeuverAuthorizationResponder(ModelAuthorizationResponder[Maneuver]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Maneuver authorization Request-Response workflow.

    Attributes:
        dispatcher: ManeuverAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: ManeuverAuthorizationRequest[T]) -> ManeuverDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ManeuverAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ManeuverAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ManeuverAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> ManeuverAuthorizationDispatcher:
        return cast(ManeuverAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ManeuverAuthorizationRequest
    ) -> ManeuverDecision:
        """
        Certify a candidate is a ManeuverCarrier whose payload is either a Maneuver
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ManeuverAuthorizationRequest
        Result:
            ManeuverDecision
        Raises:
            ManeuverAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ManeuverDecision.failure(
                request=request,
                result=result,
                exception=ManeuverAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizationResponderException.MSG,
                    err_code=ManeuverAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ManeuverCarrier, result.payload)
        return ManeuverDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )