# src/logic/token/database/searcher/context/service/__init__.py

"""
Module: logic.token.database.searcher.context.service.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from system import IntegrityMicroservice, IdFactory
from model.state.token import TokenQuery, TokenQueryBuilder, TokenQueryOpsController, TokenQueryValidator


class TokenQueryService(IntegrityMicroservice[TokenQuery]):
    """
    Role:
        -   Microservice API
        -   Stateless Integrity Lifecycle Manager

    Responsibilities:
        1.  Mutates TokenQuery instances
        2.  Ensure TokenQuery integrity and consistency when its state changes.
        3.  Build TokenQuery instances that satisfy integrity contracts
        4.  Maintain the TokenQuery integrity lifecycle.

    Attributes:
        SERVICE_NAME: TokenQueryService

        id: int
        schema: schema
        controller: TokenQueryOpsController

    Provides:

    Super Class:
        IntegrityMicroservice
    """
    SERVICE_NAME = "TokenQueryService"
    _ops_controller: TokenQueryOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="TokenQueryService"),
            ops_controller: TokenQueryOpsController = TokenQueryOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: TokenQueryOpsController
        """
        super().__init__(id=id, name=name)
        self._ops_controller = ops_controller
    
    @property
    def builder(self) ->TokenQueryBuilder:
        return self._ops_controller.builder
    
    @property
    def validator(self) ->TokenQueryValidator:
        return self._ops_controller.run
    
    