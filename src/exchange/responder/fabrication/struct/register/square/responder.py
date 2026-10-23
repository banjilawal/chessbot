# src/exchange/responder/fabrication/struct/register/square/responder.py

"""
Module: exchange.responder.fabrication.struct.register.square.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, SquareRegisterBuildResponse
from domain import SquareRegister
from exchange import RegisterBuildResponder, SquareRegisterBuildRequest
from err import SquareRegisterBuildResponderException
from transit import SquareCarrier, SquareRegisterCarrier, SquareRegisterBuildDispatcher
from util import LoggingLevelRouter


class SquareRegisterBuildResponder(RegisterBuildResponder[SquareRegister]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the SquareRegister build Request-Response workflow.

    Attributes:
        dispatcher: SquareRegisterBuildDispatcher[T]

    Provides:
        -   def submit(request: SquareRegisterBuildRequest[T]) -> SquareRegisterBuildResponse[T]

    Super Class:
        RegisterValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[SquareRegisterBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[SquareRegisterBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or SquareRegisterBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> SquareRegisterBuildDispatcher:
        return cast(SquareRegisterBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: SquareRegisterBuildRequest
    ) -> SquareRegisterBuildResponse:
        """
        Certify a candidate is a SquareCarrier whose payload is either a Square
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: SquareRegisterBuildRequest
        Result:
            SquareRegisterBuildResponse
        Raises:
            SquareValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return SquareRegisterBuildResponse.failure(
                request=request,
                result=result,
                exception=SquareRegisterBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterBuildResponderException.MSG,
                    err_code=SquareRegisterBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(SquareRegisterCarrier, result.payload)
        return SquareRegisterBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )