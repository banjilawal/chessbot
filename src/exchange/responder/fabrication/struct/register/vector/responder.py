# src/exchange/responder/fabrication/struct/register/vector/responder.py

"""
Module: exchange.responder.fabrication.struct.register.vector.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, VectorRegisterBuildResponse
from domain import VectorRegister
from exchange import RegisterBuildResponder, VectorRegisterBuildRequest
from err import VectorRegisterBuildResponderException
from transit import VectorCarrier, VectorRegisterCarrier, VectorRegisterBuildDispatcher
from util import LoggingLevelRouter


class VectorRegisterBuildResponder(RegisterBuildResponder[VectorRegister]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the VectorRegister build Request-Response workflow.

    Attributes:
        dispatcher: VectorRegisterBuildDispatcher[T]

    Provides:
        -   def submit(request: VectorRegisterBuildRequest[T]) -> VectorRegisterBuildResponse[T]

    Super Class:
        RegisterValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorRegisterBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorRegisterBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorRegisterBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorRegisterBuildDispatcher:
        return cast(VectorRegisterBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorRegisterBuildRequest
    ) -> VectorRegisterBuildResponse:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: VectorRegisterBuildRequest
        Result:
            VectorRegisterBuildResponse
        Raises:
            VectorValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorRegisterBuildResponse.failure(
                request=request,
                result=result,
                exception=VectorRegisterBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterBuildResponderException.MSG,
                    err_code=VectorRegisterBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorRegisterCarrier, result.payload)
        return VectorRegisterBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )