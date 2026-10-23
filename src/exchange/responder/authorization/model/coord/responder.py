# src/exchange/responder/authorization/model/coord/responder.py

"""
Module: exchange.responder.authorization.model.coord.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, CoordDecision
from exchange import ModelAuthorizationResponder, CoordAuthorizationRequest
from domain import Coord
from err import CoordAuthorizationResponderException
from transit import CoordCarrier, CoordAuthorizationDispatcher
from util import LoggingLevelRouter


class CoordAuthorizationResponder(ModelAuthorizationResponder[Coord]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Coord authorization Request-Response workflow.

    Attributes:
        dispatcher: CoordAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: CoordAuthorizationRequest[T]) -> CoordDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[CoordAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[CoordAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or CoordAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> CoordAuthorizationDispatcher:
        return cast(CoordAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: CoordAuthorizationRequest
    ) -> CoordDecision:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: CoordAuthorizationRequest
        Result:
            CoordDecision
        Raises:
            CoordAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return CoordDecision.failure(
                request=request,
                result=result,
                exception=CoordAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordAuthorizationResponderException.MSG,
                    err_code=CoordAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(CoordCarrier, result.payload)
        return CoordDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )