# src/exchange/responder/fabrication/model/scalar/responder.py

"""
Module: exchange.responder.fabrication.model.scalar.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ScalarBuildResponse
from exchange import ModelBuildResponder, ScalarBuildRequest
from domain import Scalar
from err import ScalarBuildResponderException
from transit import ScalarCarrier, ScalarBuildDispatcher
from util import LoggingLevelRouter


class ScalarBuildResponder(ModelBuildResponder[Scalar]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Scalar build Request-Response workflow.

    Attributes:
        dispatcher: ScalarBuildDispatcher[T]

    Provides:
        -   def execute(request: ScalarBuildRequest[T]) -> ScalarBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ScalarBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ScalarBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ScalarBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> ScalarBuildDispatcher:
        return cast(ScalarBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ScalarBuildRequest
    ) -> ScalarBuildResponse:
        """
        Certify a candidate is a ScalarCarrier whose payload is either a Scalar
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ScalarBuildRequest
        Result:
            ScalarBuildResponse
        Raises:
            ScalarValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ScalarBuildResponse.failure(
                request=request,
                result=result,
                exception=ScalarBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuildResponderException.MSG,
                    err_code=ScalarBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ScalarCarrier, result.payload)
        return ScalarBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )