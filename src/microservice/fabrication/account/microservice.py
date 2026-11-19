# src/microservice/fabrication/microservice.py

"""
Module: microservice.fabrication.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from typing import Optional, cast

from artifcat import BuildResult
from exchange import AccountBuildRequest, BuildRequest
from microservice import FabricationMicroservice
from transit import AccountBuildDispatcher, BuildDispatcher
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
        id: int
        controller: Controller[T]
        name: Optional[str]

    Provides:

    Super Class:
        Microservice
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
        return cast(AccountBuildDispatcher, super()._dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountBuildRequest) -> BuildResult[Account]:
        result = self.dispatcher.execute()
    
    
    