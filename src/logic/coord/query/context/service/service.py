# src/logic/coordContext/query/query/service/transaction.py

"""
Module: logic.coordContext.query.query.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from logic.system import IntegrityService, IdFactory


class CoordContextService(IntegrityService[CoordContext]):
    """
    Role:
        -   Microservice API
        -   Stateless Integrity Lifecycle Manager

    Responsibilities:
        1.  Mutates CoordContext instances
        2.  Ensure CoordContext integrity and consistency when its state changes.
        3.  Build CoordContext instances that satisfy integrity contracts
        4.  Maintain the CoordContext integrity lifecycle.

    Attributes:
        SERVICE_NAME: CoordContextService

        id: int
        name: name
        build: CoordContextbuild
        validation: CoordContextValidation
        controller: CoordContextOpsController

    Provides:

    Super Class:
        IntegrityService
    """
    SERVICE_NAME = "CoordContextService"
    _build: CoordContextBuildProcess
    _validation: CoordContextValidationProcess
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="CoordContextService"),
            build: CoordContextBuildProcess =CoordContextBuildProcess(),
            validation: CoordContextValidationProcess =CoordContextValidationProcess(),
    ):
        """
        Args:
            id: int
            name: str
            build: CoordContextBuilder
            validation: CoordContextValidationTransaction
        """
        super().__init__(id=id, name=name)
        self._build = build
        self._validation = validation
    
    @property
    def build(self) -> CoordContextBuildProcess:
        return self._build
    
    @property
    def validation(self) -> CoordContextValidationProcess:
        return self._validation
    
    