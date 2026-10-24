# src/exchange/responder/fabrication/struct/register/coord/responder.py

"""
Module: exchange.responder.fabrication.struct.register.coord.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, CoordRegisterBuildResponse
from domain import CoordRegister
from exchange import RegisterBuildResponder, CoordRegisterBuildRequest
from err import CoordRegisterBuildResponderException
from transit import CoordCarrier, CoordRegisterCarrier, CoordRegisterBuildDispatcher
from util import LoggingLevelRouter


class CoordRegisterBuildResponder(RegisterBuildResponder[CoordRegister]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the CoordRegister build Request-Response workflow.

    Attributes:
        dispatcher: CoordRegisterBuildDispatcher[T]

    Provides:
        -   def execute(request: CoordRegisterBuildRequest[T]) -> CoordRegisterBuildResponse[T]

    Super Class:
        RegisterValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[CoordRegisterBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[CoordRegisterBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or CoordRegisterBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> CoordRegisterBuildDispatcher:
        return cast(CoordRegisterBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: CoordRegisterBuildRequest
    ) -> CoordRegisterBuildResponse:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: CoordRegisterBuildRequest
        Result:
            CoordRegisterBuildResponse
        Raises:
            CoordValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return CoordRegisterBuildResponse.failure(
                request=request,
                result=result,
                exception=CoordRegisterBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterBuildResponderException.MSG,
                    err_code=CoordRegisterBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(CoordRegisterCarrier, result.payload)
        return CoordRegisterBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )