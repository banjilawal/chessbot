# src/logic/zone/service/validator.py

"""
Module: logic.zone.service.service
Author: Banji Lawal
Created: 2026-03-29
version: 1.0.0
"""

from __future__ import annotations

from logic.system import IdFactory, IntegrityService
from logic.zone import Zone, ZoneBuilder, ZoneOpsController, ZoneTable, ZoneValidator


class ZoneService(IntegrityService[Zone]):
    """
    Role:
        -   API
        -   Stateless microservice
        -   Lifecycle Manager
        -   Operations Provider

    Responsibilities:
        1.  Baremetal service request API for Zone operations.
        2.  Maintain the builder-validator security lifecycle for Zone instances.

    Attributes:
        SERVICE_NAME: ZoneService

        id: int
        name: name
        table: ZoneTable
        controller: ZoneOpsController

    Provides:

    Super Class:
        IntegrityService
    """
    SERVICE_NAME = "ZoneService"
    _table: ZoneTable
    _ops_controller: ZoneOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="ZoneService"),
            ops_controller: ZoneOpsController = ZoneOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: ZoneOpsController
        """
        super().__init__(id=id, name=name)
        self._table = ZoneTable()
        self._ops_controller = ops_controller

    @property
    def builder(self) -> ZoneBuilder:
        return self._ops_controller.builder
    
    @property
    def validator(self) -> ZoneValidator:
        return self._ops_controller.validator
    
    @property
    def ops_controller(self) -> ZoneOpsController:
        return self._ops_controller
    
