# src/logic/tokenContext/query/query/service/validator.py

"""
Module: logic.tokenContext.query.query.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from logic.system import IntegrityMicroService, IdFactory
from logic.token import TokenContext, TokenContextBuilder, TokenContextValidator


class TokenContextService(IntegrityMicroService[TokenContext]):
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
        name: name
        build: TokenContextbuild
        validation: TokenContextValidation
        controller: TokenContextOpsController

    Provides:

    Super Class:
        IntegrityMicroService
    """
    SERVICE_NAME = "TokenContextService"
    _build: TokenContextBuilder
    _validation: TokenContextValidator
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="TokenContextService"),
            build: TokenContextBuilder =TokenContextBuilder(),
            validation: TokenContextValidator =TokenContextValidator(),
    ):
        """
        Args:
            id: int
            name: str
            build: TokenContextBuilder
            validation: TokenContextValidator
        """
        super().__init__(id=id, name=name)
        self._build = build
        self._validation = validation
    
    @property
    def builder(self) ->TokenContextBuilder:
        return self._build
    
    @property
    def validation(self) ->TokenContextValidator:
        return self._validation
    
    