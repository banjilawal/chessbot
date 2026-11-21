# src/microservice/fabrication/account/microservice.py

"""
Module: microservice.fabrication.account.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from typing import Optional, cast

from artifcat import BuildResult
from domain import Account
from err import AccountBuildMicroserviceException
from microservice import FabricationMicroservice
from request import AccountBuildRequest
from transit import AccountBuildDispatcher
from util import LoggingLevelRouter


class AccountBuildMicroservice(FabricationMicroservice[AccountBuildRequest]):
    """
    Role:
        - API
        - Lifecycle Manager
        - Operations Provider
        - Stateless Microservice
        
    About:
        Avoids casting an entity's builders and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the build-validation security lifecycle.

    Attributes:
        dispatcher: Optional[AccountBuildDispatcher]

    Provides:

    Super Class:
        FabricationMicroservice
    """
  
    
    def __init__(
            self,
            dispatcher: Optional[AccountBuildDispatcher]
    ):
        """
        Args:
            dispatcher: Optional[AccountBuildDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AccountBuildDispatcher())
        
    @property
    def dispatcher(self) -> AccountBuildDispatcher:
        return cast(AccountBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountBuildRequest) -> BuildResult[Account]:
        """
        Handles AccountBuildRequests.

        Action:
            1.  Send an exception chain in the BuildRequest if the request is
                not fulfilled.
            2.  Otherwise, send the Account in the success result.
        Args:
            request: AccountSearchRequest
        Result:
            BuildResult[Account]
        Raises:
            AccountBuildMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        result = self.dispatcher.execute(request)
        if result.is_failure:
            BuildResult.failure(
                AccountBuildMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuildMicroserviceException.MSG,
                    err_code=AccountBuildMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        product = cast(Account, result.payload)
        return BuildResult.success(product)
    
    