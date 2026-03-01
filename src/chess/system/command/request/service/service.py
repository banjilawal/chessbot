# system/command/command/serviceservice.py

"""
Module: src.chess.system.command.command.service.service
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from chess.system import (
    IntegrityService, Builder, Command, ServiceRequest, ServiceRequestBuilder,
    ServiceRequestValidator, Validator
)


class ChessServiceRequest(IntegrityService[Command]):
    """
    # ROLE: Microservice API, Integrity Lifecycle Manager, APLifecycle Management.

    # RESPONSIBILITIES:
    1.  Integrity Lifecycle Management Microservice API.
    2.  Bundles primitives for assuring integrity and consistency in the two phases of
        the integrity lifecycle.
            *   At object creation.
            *   At object invocation.

    # PARENT:
        *   IntegrityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   builder (Builder[Command])
        *   validator (Validator[Command])

    # INHERITED ATTRIBUTES:
        *   See IntegrityService class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   id (int)
        *   name (name)
        *   builder (Builder[Command])
        *   validator (Validator[Command])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "ServiceRequest"
    # _builder: Builder[ServiceRequestBuilder]
    # _validator: Validator[ServiceRequestValidator]
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: ServiceRequestBuilder = ServiceRequestBuilder(),
            validator:ServiceRequestValidator = ServiceRequestValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)

    # @property
    # def builder(self) -> Builder[Command]:
    #     return self.builder
    #
    # @property
    # def validator(self) -> Validator[Command]:
    #     return self.certifier
    #
    # def __eq__(self, other):
    #     if super().__eq__(other):
    #         if isinstance(other, ChessServiceRequest):
    #             return True
    #     return False
    #
    # def __hash__(self):
    #     return hash(self._id)
    #
    # def __str__(self):
    #     return f"id:{self._id}, name:{self._name}"