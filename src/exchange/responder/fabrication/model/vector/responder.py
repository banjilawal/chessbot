# src/exchange/responder/fabrication/model/vector/responder.py

"""
Module: exchange.responder.fabrication.model.vector.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, VectorBuildResponse
from exchange import ModelBuildResponder, VectorBuildRequest
from domain import Vector
from err import VectorBuildResponderException
from transit import VectorCarrier, VectorBuildDispatcher
from util import LoggingLevelRouter


class VectorBuildResponder(ModelBuildResponder[Vector]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Vector build Request-Response workflow.

    Attributes:
        dispatcher: VectorBuildDispatcher[T]

    Provides:
        -   def execute(request: VectorBuildRequest[T]) -> VectorBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorBuildDispatcher:
        return cast(VectorBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorBuildRequest
    ) -> VectorBuildResponse:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: VectorBuildRequest
        Result:
            VectorBuildResponse
        Raises:
            VectorValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorBuildResponse.failure(
                request=request,
                result=result,
                exception=VectorBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorBuildResponderException.MSG,
                    err_code=VectorBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorCarrier, result.authorization_applicant)
        return VectorBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )