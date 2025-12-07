# src/chess/rank/model/king/service.py

"""
Module: chess.rank.model.king.entity_service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import King, KingValidator, RankFactory
from chess.system import EntityService, Validator, id_emitter


class KingService(EntityService[King]):
    DEFAULT_NAME = "KingService"
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            builder: RankFactory = RankFactory(),
            validator: Validator = KingValidator()
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)