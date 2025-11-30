# src/chess/rank/king/service.py

"""
Module: chess.rank.king.service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import King, KingValidator, RankFactory
from chess.system import Service, Validator, id_emitter


class KingService(Service[King]):
    DEFAULT_NAME = "KingService"
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            builder: RankFactory = RankFactory(),
            validator: Validator = KingValidator()
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)