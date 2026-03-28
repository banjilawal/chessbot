# src/command/request/service/transaction.py

"""
Module: command.request.service.service
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import cast

from logic.system import (
    IntegrityService, BuildTransaction, Command, Request, RequestBuilder,
    RequestValidator, ValidationTransaction
)


class RequestService(IntegrityService[Command]):
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
        *   build (BuildTransaction[Command])
        *   validation (ValidationTransaction[Command])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "RequestService"
    # _builder: BuildTransaction[RequestBuildTransaction]
    # _validator: ValidationTransaction[RequestValidationTransaction]
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: RequestBuilder = RequestBuilder(),
            validator:RequestValidator = RequestValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)

    @property
    def build(self) -> RequestBuilder:
        return cast(RequestBuilder, self.build)

    @property
    def validation(self) -> RequestValidator:
        return cast(RequestValidator, self.validation)
    #
    # def __eq__(self, other):
    #     if super().__eq__(other):
    #         if isinstance(other, RequestService):
    #             return True
    #     return False
    #
    # def __hash__(self):
    #     return hash(self._id)
    #
    # def __str__(self):
    #     return f"id:{self._id}, name:{self._name}"