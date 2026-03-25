# system/command/command/serviceservice.py

"""
Module: src.command.command.command.service.service
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from typing import cast

from logic.system import CommandBuilder, CommandValidator, IntegrityService, BuildProcess, Command, ValidationProcess


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
        *   build (BuildProcess[Command])
        *   validation (ValidationProcess[Command])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "CommandService"
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: CommandBuilder = CommandBuilder(),
            validator: CommandValidator = CommandValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)

    @property
    def build(self) -> CommandBuilder:
        return cast(CommandBuilder, self.build)

    @property
    def validation(self) -> ValidationProcess[Command]:
        return cast(CommandValidator, self.validation)
    #
    # def __eq__(self, other):
    #     if super().__eq__(other):
    #         if isinstance(other, CommandService):
    #             return True
    #     return False
    #
    # def __hash__(self):
    #     return hash(self._id)
    #
    # def __str__(self):
    #     return f"id:{self._id}, name:{self._name}"