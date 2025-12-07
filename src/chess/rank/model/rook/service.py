# src/chess/rank/model/rook/entity_service.py

"""
Module: chess.rank.model.rook.entity_service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import Rook, RookValidator, RankFactory
from chess.system import EntityService, Validator, id_emitter


class RookService(EntityService[Rook]):
    DEFAULT_NAME = "RookService"
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            builder: RankFactory = RankFactory(),
            validator: Validator = RookValidator()
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)