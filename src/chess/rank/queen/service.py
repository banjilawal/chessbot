# src/chess/rank/queen/service.py

"""
Module: chess.rank.queen.service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import Queen, QueenValidator, RankFactory
from chess.system import Service, Validator, id_emitter


class QueenService(Service[Queen]):
    DEFAULT_NAME = "QueenService"
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            builder: RankFactory = RankFactory(),
            validator: Validator = QueenValidator()
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)