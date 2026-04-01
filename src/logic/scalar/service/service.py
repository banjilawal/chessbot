# src/logic/scalar/service/validator.py

"""
Module: logic.scalar.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from logic.scalar import Scalar, ScalarBuilder

# src/logic/system/service/integrity/validator.py

"""
Module: logic.system.service.integrity.service
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from logic.system import IdFactory, IntegrityMicroservice, Builder, Validator


class ScalarService(IntegrityMicroservice[Scalar]):
    """
    Role:Microservice API, Integrity Lifecycle Manager, APLifecycle Management.

    Responsibilities:
    1.  Integrity Lifecycle Management Microservice API.
    2.  Bundles primitives for assuring integrity and consistency in the two phases of
        the integrity lifecycle.
            *   At object creation.
            *   At object invocation.

    Super Class:
        *   IntegrityMicroservice

    Provides:

    # LOCAL ATTRIBUTES:
        *   build (Builder[Scalar])
        *   validation (Validator[Scalar])

    # INHERITED ATTRIBUTES:
        *   See IntegrityMicroservice class for inherited attributes.

    Attributes:
        *   id (int)
        *   name (name)
        *   build (Builder[Scalar])
        *   validation (Validator[Scalar])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    *   See IntegrityMicroservice class for inherited methods.
    """
    SERVICE_NAME = "ScalarService"
    _builder: Builder[Scalar]
    _validator: Validator[Scalar]
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="ScalarService"),
            builder: Builder[Scalar] = ScalarBuilder(),
            validator: Validator[Scalar] = Validator(),
    ):
        super().__init__(id=id, name=name)
        self._builder = builder
        self._validator = validator
    
    @property
    def builder(self) -> Builder[Scalar]:
        return self._builder
    
    @property
    def validator(self) -> Validator[Scalar]:
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
