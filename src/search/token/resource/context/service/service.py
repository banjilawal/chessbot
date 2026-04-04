# src/logic/token/database/search/context/service/__init__.py

"""
Module: logic.token.database.search.context.service.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import IntegrityMicroservice, IdFactory
from model.token import TokenContext, TokenContextBuilder, TokenContextOpsController, TokenContextValidator


class TokenContextService(IntegrityMicroservice[TokenContext]):
    """
    Role:
        -   Microservice API
        -   Stateless Integrity Lifecycle Manager

    Responsibilities:
        1.  Mutates TokenContext instances
        2.  Ensure TokenContext integrity and consistency when its state changes.
        3.  Build TokenContext instances that satisfy integrity contracts
        4.  Maintain the TokenContext integrity lifecycle.

    Attributes:
        SERVICE_NAME: TokenContextService

        id: int
        schema: schema
        controller: TokenContextOpsController

    Provides:

    Super Class:
        IntegrityMicroservice
    """
    SERVICE_NAME = "TokenContextService"
    _ops_controller: TokenContextOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="TokenContextService"),
            ops_controller: TokenContextOpsController = TokenContextOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: TokenContextOpsController
        """
        super().__init__(id=id, name=name)
        self._ops_controller = ops_controller
    
    @property
    def builder(self) ->TokenContextBuilder:
        return self._ops_controller.builder
    
    @property
    def validator(self) ->TokenContextValidator:
        return self._ops_controller.validator
    
    