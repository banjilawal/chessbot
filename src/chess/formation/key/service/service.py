# src/chess/formation/key/service/service.py

"""
Module: chess.formation.key.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import cast

from chess.system import ContextService, id_emitter
from chess.formation import FormationLookup, FormationSuperKey, FormationSuperKeyBuilder, FormationSuperKeyValidator


class FormationSuperKeyService(ContextService[FormationSuperKey]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing FormationSuperKey microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for FormationSuperKey state.
    4.  Single entry and entry points to FormationSuperKey lifecycle.

    # PARENT:
        *   ContextService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "FormationSuperKeyService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            lookup: FormationLookup = FormationLookup(),
            builder: FormationSuperKeyBuilder = FormationSuperKeyBuilder(),
            validator: FormationSuperKeyValidator = FormationSuperKeyValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (FormationSuperKeyBuilder)
            *   validator (FormationSuperKeyValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=lookup)
    
    @property
    def builder(self) -> FormationSuperKeyBuilder:
        """get FormationSuperKeyBuilder"""
        return cast(FormationSuperKeyBuilder, self.entity_builder)
    
    @property
    def validator(self) -> FormationSuperKeyValidator:
        """get FormationSuperKeyValidator"""
        return cast(FormationSuperKeyValidator, self.entity_validator)
    
    @property
    def lookup(self) -> FormationLookup:
        return cast(FormationLookup, self.entity_finder)