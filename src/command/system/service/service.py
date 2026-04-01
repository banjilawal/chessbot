# system/command/root/serviceservice.py

"""
Module: src.command.root.command.service.service
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations


from command import Command, CommandBuilder, CommandOpsController
from logic.system import IntegrityService


class CommandService(IntegrityService[Command]):
    """
    Role:Microservice API, Integrity Lifecycle Manager, APLifecycle Management.

    Responsibilities:
    1.  Integrity Lifecycle Management Microservice API.
    2.  Bundles primitives for assuring integrity and consistency in the two phases of
        the integrity lifecycle.
            *   At object creation.
            *   At object invocation.

    Super Class:
        *   IntegrityService

    Provides:

    # LOCAL ATTRIBUTES:
        *   build (Builder[Command])
        *   validation (Validator[Command])

    # INHERITED ATTRIBUTES:
        *   See IntegrityService class for inherited attributes.

    Attributes:
        *   id (int)
        *   name (name)
        *   build (Builder[Command])
        *   validation (Validator[Command])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "CommandService"
    _ops_controller = CommandOpsController
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            ops_controller: CommandOpsController = CommandOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: CommandOpsController
        """
        super().__init__(id=id, name=name,)
        self._ops_controller = ops_controller

    @property
    def builder(self) -> CommandBuilder:
        return self._ops_controller.builder

    @property
    def validation(self) -> CommandValidator:
        return self._ops_controller.validator
    
    @property
    def ops_controller(self) -> CommandOpsController:
        return self._ops_controller
