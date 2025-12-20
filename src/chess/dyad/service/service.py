# src/chess/dyad/service/service.py

"""
Module: chess.dyad.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import cast

from chess.system import EntityService, id_emitter
from chess.dyad import SchemaAgentPair, SchemaAgentPairBuilder, SchemaAgentPairValidator


class SchemaAgentPairService(EntityService[SchemaAgentPair]):
    """"""
    SERVICE_NAME = "SchemaAgentPairService"
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: SchemaAgentPairBuilder = SchemaAgentPairBuilder(),
            validator: SchemaAgentPairValidator = SchemaAgentPairValidator(),
    ):
        """"""
        method_name = "SchemaAgentPairService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> SchemaAgentPairBuilder:
        return cast(SchemaAgentPairBuilder, self._builder)
    
    
    @property
    def validator(self) -> SchemaAgentPairValidator:
        return cast(SchemaAgentPairValidator, self._validator)