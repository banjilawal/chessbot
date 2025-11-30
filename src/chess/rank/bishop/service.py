# src/chess/rank/bishop/service.py

"""
Module: chess.rank.bishop.service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import Bishop, BishopValidator, RankFactory
from chess.system import Service, Validator, id_emitter


class BishopService(Service[Bishop]):
    DEFAULT_NAME = "BishopService"
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            builder: RankFactory = RankFactory(),
            validator: Validator = BishopValidator()
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)

