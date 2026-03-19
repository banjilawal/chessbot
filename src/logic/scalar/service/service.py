# src/logic/scalar/service/service.py

"""
Module: logic.scalar.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from logic.scalar import Scalar

# src/logic/system/service/integrity/service.py

"""
Module: logic.system.service.integrity.service
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from logic.system import IntegrityService, BuildProcess, ValidationProcess


class ScalarService(IntegrityService[Scalar]):
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
        *   builder (Builder[Scalar])
        *   validator (Validator[Scalar])

    # INHERITED ATTRIBUTES:
        *   See IntegrityService class for inherited attributes.

    Attributes:
        *   id (int)
        *   name (name)
        *   builder (BuildProcess[Scalar])
        *   validator (ValidationProcess[Scalar])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "ScalarService"
    _builder: BuildProcess[Scalar]
    _validator: ValidationProcess[Scalar]
    
    def __init__(
            self,
            id: int,
            name: str,
            builder: BuildProcess[Scalar],
            validator: ValidationProcess[Scalar]
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> BuildProcess[Scalar]:
        return self._builder
    
    @property
    def validator(self) -> ValidationProcess[Scalar]:
        return self.certifier
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, ScalarService):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
