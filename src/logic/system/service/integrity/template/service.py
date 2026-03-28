# template/service/transaction.py

"""
Module: template.service.service
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from logic.system import IntegrityService, BuildTransaction, Template, ValidationTransaction


class TemplateService(IntegrityService[Template]):
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
        *   build (Builder[Template])
        *   validation (Validator[Template])

    # INHERITED ATTRIBUTES:
        *   See IntegrityService class for inherited attributes.

    Attributes:
        *   id (int)
        *   name (name)
        *   build (BuildTransaction[Template])
        *   validation (ValidationTransaction[Template])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "TemplateService"
    _builder: BuildTransaction[Template]
    _validator: ValidationTransaction[Template]
    
    def __init__(
            self,
            id: int,
            name: str,
            builder: BuildTransaction[Template],
            validator: ValidationTransaction[Template]
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)

    @property
    def build(self) -> BuildTransaction[Template]:
        return self._builder
    
    @property
    def validation(self) -> ValidationTransaction[Template]:
        return self.certifier
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, TemplateService):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"