# chess/rank/service.py

"""
Module: chess.rank.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from chess.coord import CoordService
from chess.rank import RankFactory, RankSearchService, RankValidatorFactory



class RankService:
    _factory: type[RankFactory] = RankFactory
    _validator: type[RankValidatorFactory]
    _search_service: type[RankSearchService]
    _coord_service: CoordService
    
    
    def __init__(
            self,
            factory: type[RankFactory]=RankFactory,
            search_service: type[RankSearchService] = RankSearchService,
            validator: type[RankValidatorFactory]=RankValidatorFactory,
            coord_service: CoordService=CoordService()
    ):

        self._factory = factory
        self._validator = validator
        self._search_service = search_service
        self._coord_service = coord_service
        self._search_service = RankSearchService
        
    @property
    def build(self) -> type[RankFactory]:
        return self._factory
    
    @property
    def validate(self) -> type[RankValidatorFactory]:
        return self._validator
        
    @property
    def search(self) -> type[RankSearchService]:
        return self._search_service