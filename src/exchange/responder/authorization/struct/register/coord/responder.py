# src/exchange/responder/authorization/struct/register/coord/responder.py

"""
Module: exchange.responder.authorization.struct.register.coord.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, CoordRegisterDecision
from domain import CoordRegister
from exchange import RegisterAuthorizationResponder, CoordRegisterPermissionRequest
from err import CoordRegisterAuthorizationResponderException
from transit import CoordCarrier, CoordRegisterCarrier, CoordRegisterAuthorizationDispatcher
from util import LoggingLevelRouter


class CoordRegisterAuthorizationResponder(RegisterAuthorizationResponder[CoordRegister]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the CoordRegister authorization Request-Response workflow.

    Attributes:
        dispatcher: CoordRegisterAuthorizationDispatcher[T]

    Provides:
        -   def execute(request: CoordRegisterPermissionRequest[T]) -> CoordRegisterDecision[T]

    Super Class:
        RegisterValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[CoordRegisterAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[CoordRegisterAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or CoordRegisterAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> CoordRegisterAuthorizationDispatcher:
        return cast(CoordRegisterAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: CoordRegisterPermissionRequest
    ) -> CoordRegisterDecision:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: CoordRegisterPermissionRequest
        Result:
            CoordRegisterDecision
        Raises:
            CoordAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return CoordRegisterDecision.failure(
                request=request,
                result=result,
                exception=CoordRegisterAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterAuthorizationResponderException.MSG,
                    err_code=CoordRegisterAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(CoordRegisterCarrier, result.authorization_applicant)
        return CoordRegisterDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )