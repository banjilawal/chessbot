# src/chess/rank/service/service.py

"""
Module: chess.rank.service.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import Service, id_emitter
from chess.rank import Rank, RankFactory, RankSpec, RankSpecValidator, RankValidatorFactory


class RankService(Service[Rank]):
    DEFAULT_NAME = "RankService"
    _spec: RankSpec
    _spec_validator: RankSpecValidator
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            spec: RankSpec = RankSpec(),
            id: int = id_emitter.service_id,
            builder: RankFactory = RankFactory(),
            spec_validator: RankSpecValidator = RankSpecValidator(),
            validator: RankValidatorFactory = RankValidatorFactory(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._spec = spec
        self._spec_validator = spec_validator
        
    @property
    def spec(self) -> RankSpec:
        return self._spec
    
    @property
    def spec_validator(self) -> RankSpecValidator:
        return self._spec_validator
    

