# src/exchange/responder/fabrication/model/account/responder.py

"""
Module: exchange.responder.fabrication.model.account.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, AccountBuildResponse
from exchange import ModelBuildResponder, AccountBuildRequest
from domain import Account
from err import AccountBuildResponderException
from transit import AccountCarrier, AccountBuildDispatcher
from util import LoggingLevelRouter


class AccountBuildResponder(ModelBuildResponder[Account]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Account build Request-Response workflow.

    Attributes:
        dispatcher: AccountBuildDispatcher[T]

    Provides:
        -   def execute(request: AccountBuildRequest[T]) -> AccountBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[AccountBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AccountBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or AccountBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> AccountBuildDispatcher:
        return cast(AccountBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: AccountBuildRequest
    ) -> AccountBuildResponse:
        """
        Certify a candidate is a AccountCarrier whose payload is either a Account
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: AccountBuildRequest
        Result:
            AccountBuildResponse
        Raises:
            AccountValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return AccountBuildResponse.failure(
                request=request,
                result=result,
                exception=AccountBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuildResponderException.MSG,
                    err_code=AccountBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(AccountCarrier, result.payload)
        return AccountBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )