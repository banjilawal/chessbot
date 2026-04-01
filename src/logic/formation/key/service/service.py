# src/logic/formation/key/service/validator.py

"""
Module: logic.formation.key.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import cast

from logic.system import QueryService, id_emitter
from logic.formation import FormationLookupProcess, FormationKey, FormationKeyBuilder, FormationKeyValidator


class FormationKeyService(QueryService[FormationKey]):
    """
    Role:MicroService, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing FormationKey microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for FormationKey state.
    4.  Single entry and entry points to FormationKey lifecycle.

    Super Class:
        *   QueryService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "FormationKeyService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            lookup: FormationLookupProcess = FormationLookupProcess(),
            builder: FormationKeyBuilder = FormationKeyBuilder(),
            validator: FormationKeyValidator = FormationKeyValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   build (FormationKeyBuilder)
            *   validation (FormationKeyValidator)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=lookup)
    
    @property
    def build(self) -> FormationKeyBuilder:
        """get FormationKeyBuilder"""
        return cast(FormationKeyBuilder, self.entity_builder)
    
    @property
    def validation(self) -> FormationKeyValidator:
        """get FormationKeyValidator"""
        return cast(FormationKeyValidator, self.entity_validator)
    
    @property
    def lookup(self) -> FormationLookupProcess:
        return cast(FormationLookupProcess, self.entity_finder)