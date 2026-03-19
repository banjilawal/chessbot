# src/logic/formation/key/service/service.py

"""
Module: logic.formation.key.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import cast

from logic.system import ContextService, id_emitter
from logic.formation import FormationLookup, FormationKey, FormationKeyBuilder, FormationKeyValidationProcess


class FormationKeyService(ContextService[FormationKey]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing FormationKey microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for FormationKey state.
    4.  Single entry and entry points to FormationKey lifecycle.

    Super Class:
        *   ContextService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "FormationKeyService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            lookup: FormationLookup = FormationLookup(),
            builder: FormationKeyBuilder = FormationKeyBuilder(),
            validator: FormationKeyValidationProcess = FormationKeyValidationProcess(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (FormationKeyBuilder)
            *   validator (FormationKeyValidationProcess)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=lookup)
    
    @property
    def builder(self) -> FormationKeyBuilder:
        """get FormationKeyBuilder"""
        return cast(FormationKeyBuilder, self.entity_builder)
    
    @property
    def validator(self) -> FormationKeyValidationProcess:
        """get FormationKeyValidationProcess"""
        return cast(FormationKeyValidationProcess, self.entity_validator)
    
    @property
    def lookup(self) -> FormationLookup:
        return cast(FormationLookup, self.entity_finder)