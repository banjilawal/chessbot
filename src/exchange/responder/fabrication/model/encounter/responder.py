# src/exchange/responder/fabrication/model/encounter/responder.py

"""
Module: exchange.responder.fabrication.model.encounter.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, EncounterBuildResponse
from exchange import ModelBuildResponder, EncounterBuildRequest
from domain import Encounter
from err import EncounterBuildResponderException
from transit import EncounterCarrier, EncounterBuildDispatcher
from util import LoggingLevelRouter


class EncounterBuildResponder(ModelBuildResponder[Encounter]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Encounter build Request-Response workflow.

    Attributes:
        dispatcher: EncounterBuildDispatcher[T]

    Provides:
        -   def submit(request: EncounterBuildRequest[T]) -> EncounterBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[EncounterBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[EncounterBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or EncounterBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> EncounterBuildDispatcher:
        return cast(EncounterBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: EncounterBuildRequest
    ) -> EncounterBuildResponse:
        """
        Certify a candidate is a EncounterCarrier whose payload is either a Encounter
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: EncounterBuildRequest
        Result:
            EncounterBuildResponse
        Raises:
            EncounterValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return EncounterBuildResponse.failure(
                request=request,
                result=result,
                exception=EncounterBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterBuildResponderException.MSG,
                    err_code=EncounterBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(EncounterCarrier, result.payload)
        return EncounterBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )