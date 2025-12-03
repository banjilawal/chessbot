# src/chess/rank/service/service.py

"""
Module: chess.rank.service.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import IntegrityService, id_emitter
from chess.rank import Rank, RankFactory, RankSpecValidator, RankValidatorFactory


class RankIntegrityService(IntegrityService[Rank]):
    DEFAULT_NAME = "RankIntegrityService"
    _spec_validator: RankSpecValidator
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: RankFactory = RankFactory(),
            spec_validator: RankSpecValidator = RankSpecValidator(),
            validator: RankValidatorFactory = RankValidatorFactory(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._spec_validator = spec_validator
    
    @property
    def spec_validator(self) -> RankSpecValidator:
        return self._spec_validator
    

