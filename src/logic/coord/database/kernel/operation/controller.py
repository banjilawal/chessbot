# src/logic/coord/database/kernel/operation/controller.py

"""
Module: logic.coord.database.kernel.operation.controller
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import CoordService, CoordStackCrudController


class CoordStackOpsController:
    """
    Role:
        -   Operations Controller

    Responsibilities:
        1.  Provide a single entry point for transactions CoordStackService operates.

    Attributes:
        integrity_service: CoordService
        crud_controller: CoordStackCrudController

    Provides:
    
    Super Class:
    """
    _integrity_service: CoordService
    _crud_controller: CoordStackCrudController
    
    def __init__(
            self,
            integrity_service: CoordService = CoordService(),
            crud_controller: CoordStackCrudController = CoordStackCrudController(),

    ):
        self._crud_controller = crud_controller
        self._integrity_service = integrity_service
    
    @property
    def integrity_service(self) -> CoordService:
        return self._integrity_service

    @property
    def crud_controller(self) -> CoordStackCrudController:
        return self._crud_controller