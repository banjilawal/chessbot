# src/exchange/responder/validation/struct/binder/team/responder.py

"""
Module: exchange.responder.validation.struct.binder.team.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, TeamBinderValidationResponse
from domain import TeamBinder
from exchange import BinderValidationResponder, TeamBinderValidationRequest
from err import TeamBinderValidationResponderException
from transit import TeamBinderCarrier, TeamBinderValidationDispatcher
from util import LoggingLevelRouter


class TeamBinderValidationResponder(BinderValidationResponder[TeamBinder]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the TeamBinder validation Request-Response workflow.

    Attributes:
        dispatcher: TeamBinderValidationDispatcher

    Provides:
        -   def submit(request: TeamBinderValidationRequest) -> TeamBinderValidationResponse

    Super Class:
        BinderValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TeamBinderValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TeamBinderValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TeamBinderValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> TeamBinderValidationDispatcher:
        return cast(TeamBinderValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TeamBinderValidationRequest
    ) -> TeamBinderValidationResponse:
        """
        Certify a candidate is a TeamBinderCarrier whose payload is either a Team
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TeamBinderValidationRequest
        Result:
            TeamBinderValidationResponse
        Raises:
            TeamValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TeamBinderValidationResponse.failure(
                request=request,
                result=result,
                exception=TeamBinderValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationResponderException.MSG,
                    err_code=TeamBinderValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TeamBinderCarrier, result.payload)
        return TeamBinderValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )