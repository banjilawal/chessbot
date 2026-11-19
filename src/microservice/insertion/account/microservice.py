# src/microservice/insertion/account/microservice.py

"""
Module: microservice.insertion.account.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from typing import Optional, cast

from artifcat import InsertionResult
from domain import Account
from err import AccountInsertionMicroserviceException
from exchange import AccountPushRequest
from microservice import InsertionMicroservice
from transit import AccountPushDispatcher
from util import LoggingLevelRouter


class AccountInsertionMicroservice(InsertionMicroservice[AccountPushRequest]):
    """
    Role:
        - API
        - Lifecycle Manager
        - Operations Provider
        - Stateless Microservice
        
    About:
        Avoids casting an entity's insertioners and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the insertion-validation security lifecycle.

    Attributes:
        dispatcher: Optional[AccountPushDispatcher]

    Provides:

    Super Class:
        InsertionMicroservice
    """
  
    
    def __init__(
            self,
            dispatcher: Optional[AccountPushDispatcher]
    ):
        """
        Args:
            dispatcher: Optional[AccountPushDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AccountPushDispatcher())
        
    @property
    def dispatcher(self) -> AccountPushDispatcher:
        return cast(AccountPushDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountPushRequest) -> InsertionResult[Account]:
        """
        Handles AccountPushRequests.

        Action:
            1.  Send an exception chain in the PushRequest if the request is
                not fulfilled.
            2.  Otherwise, send the Account in the success result.
        Args:
            request: AccountSearchRequest
        Result:
            InsertionResult[Account]
        Raises:
            AccountInsertionMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        result = self.dispatcher.execute(request)
        if result.is_failure:
            InsertionResult.failure(
                AccountInsertionMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountInsertionMicroserviceException.MSG,
                    err_code=AccountInsertionMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        return InsertionResult.success()
    
    