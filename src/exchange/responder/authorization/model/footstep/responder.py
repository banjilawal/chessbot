# src/exchange/responder/authorization/model/footstep/responder.py

"""
Module: exchange.responder.authorization.model.footstep.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import FootstepDecision, AuthorizationResult
from domain import Footstep
from err import FootstepAuthorizationResponderException
from exchange import FootstepAuthorizationRequest, ModelAuthorizationResponder
from transit import FootstepCarrier, FootstepAuthorizationDispatcher
from util import LoggingLevelRouter


class FootstepAuthorizationResponder(ModelAuthorizationResponder[Footstep]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Footstep authorization Request-Response workflow.

    Attributes:
        dispatcher: FootstepAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: FootstepAuthorizationRequest[T]) -> FootstepDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[FootstepAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[FootstepAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or FootstepAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> FootstepAuthorizationDispatcher:
        return cast(FootstepAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: FootstepAuthorizationRequest
    ) -> FootstepDecision:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: FootstepAuthorizationRequest
        Result:
            FootstepDecision
        Raises:
            CoordAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return FootstepDecision.failure(
                request=request,
                result=result,
                exception=FootstepAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepAuthorizationResponderException.MSG,
                    err_code=FootstepAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(FootstepCarrier, result.payload)
        return FootstepDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )