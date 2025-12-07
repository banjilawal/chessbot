# src/chess/rank/model/knight/entity_service.py

"""
Module: chess.rank.model.knight.entity_service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import Knight, KnightValidator, RankFactory
from chess.system import EntityService, Validator, id_emitter


class KnightService(EntityService[Knight]):
    DEFAULT_NAME = "KnightService"
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            builder: RankFactory = RankFactory(),
            validator: Validator = KnightValidator()
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)