# template/service/service.py

"""
Module: template.service.service
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from chess.system import IntegrityService, Builder, Template, Validator


class TemplateService(IntegrityService[Template]):
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
        *   builder (Builder[Template])
        *   validator (Validator[Template])

    # INHERITED ATTRIBUTES:
        *   See IntegrityService class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   id (int)
        *   name (name)
        *   builder (Builder[Template])
        *   validator (Validator[Template])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "TemplateService"
    _builder: Builder[Template]
    _validator: Validator[Template]
    
    def __init__(
            self,
            id: int,
            name: str,
            builder: Builder[Template],
            validator: Validator[Template]
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)

    @property
    def builder(self) -> Builder[Template]:
        return self._builder
    
    @property
    def validator(self) -> Validator[Template]:
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