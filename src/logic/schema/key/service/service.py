# src/logic/schema/key/service/service.py

"""
Module: logic.schema.key.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import cast


from logic.system import ContextService, id_emitter
from logic.schema import SchemaLookupProcess, SchemaKey, SchemaKeyBuildProcess, SchemaKeyValidationProcess


class SchemaKeyService(ContextService[SchemaKey]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing SchemaKey microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for SchemaKey state.
    4.  Single entry and entry points to SchemaKey lifecycle.

    Super Class:
        *   ContextService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "SchemaKeyService"
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            lookup: SchemaLookupProcess = SchemaLookupProcess(),
            builder: SchemaKeyBuildProcess = SchemaKeyBuildProcess(),
            validator: SchemaKeyValidationProcess = SchemaKeyValidationProcess(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (SchemaKeyBuildProcess)
            *   validator (SchemaKeyValidationProcess)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=lookup)
        
    @property
    def builder(self) -> SchemaKeyBuildProcess:
        """get SchemaKeyBuildProcess"""
        return cast(SchemaKeyBuildProcess, self.entity_builder)
    
    @property
    def validator(self) -> SchemaKeyValidationProcess:
        """get SchemaKeyValidationProcess"""
        return cast(SchemaKeyValidationProcess, self.entity_validator)
    
    @property
    def lookup(self) -> SchemaLookupProcess:
        return cast(SchemaLookupProcess, self.entity_finder)