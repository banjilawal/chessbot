# src/logic/tokenContext/query/query/service/compute.py

"""
Module: logic.tokenContext.query.query.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from logic.system import IntegrityService, IdFactory
from logic.token import TokenContext, TokenContextBuildProcess, TokenContextValidationProcess


class TokenContextService(IntegrityService[TokenContext]):
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
        IntegrityService
    """
    SERVICE_NAME = "TokenContextService"
    _build: TokenContextBuildProcess
    _validation: TokenContextValidationProcess
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="TokenContextService"),
            build: TokenContextBuildProcess =TokenContextBuildProcess(),
            validation: TokenContextValidationProcess =TokenContextValidationProcess(),
    ):
        """
        Args:
            id: int
            name: str
            build: TokenContextBuildProcess
            validation: TokenContextValidationProcess
        """
        super().__init__(id=id, name=name)
        self._build = build
        self._validation = validation
    
    @property
    def build(self) ->TokenContextBuildProcess:
        return self._build
    
    @property
    def validation(self) ->TokenContextValidationProcess:
        return self._validation
    
    