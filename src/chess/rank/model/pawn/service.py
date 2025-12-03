# src/chess/rank/model/pawn/service.py

"""
Module: chess.rank.model.pawn.service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import Pawn, PawnValidator, RankFactory
from chess.system import IntegrityService, Validator, id_emitter


class PawnIntegrityService(IntegrityService[Pawn]):
    DEFAULT_NAME = "PawnIntegrityService"
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            builder: RankFactory = RankFactory(),
            validator: Validator = PawnValidator()
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)