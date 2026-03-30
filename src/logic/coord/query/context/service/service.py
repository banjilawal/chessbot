# src/logic/coord/query/context/service/service.py

"""
Module: logic.coord.query.context.service.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from logic.system import IntegrityService, IdFactory
from logic.coord import (
    CoordContext, CoordContextBuilder, CoordContextContextOpsController, CoordContextValidator
)


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
        name: str
        builder: CoordContextBuilder
        validator: CoordContextValidator

    Provides:

    Super Class:
        IntegrityService
    """
    SERVICE_NAME = "CoordContextService"
    _ops_controller: CoordContextContextOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="CoordContextService"),
            ops_controller: CoordContextContextOpsController = CoordContextContextOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: CoordContextOpsController
        """
        super().__init__(id=id, name=name)
        self._ops_controller = ops_controller
    
    @property
    def builder(self) -> CoordContextBuilder:
        return self._ops_controller.builder
    
    @property
    def validator(self) -> CoordContextValidator:
        return self._ops_controller.validator
    
    @property
    def ops_controller(self) -> CoordContextContextOpsController:
        return self._ops_controller
    