# chess/rank/service.py

"""
Module: chess.rank.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.coord import CoordService
from chess.rank import (
    Bishop, King, Knight, Pawn, Queen, Rank, RankFactory, RankSearchService, RankSpec,
    RankValidatorFactory, Rook
)
from chess.system import BuildResult, ValidationResult


class RankService:
    _factory: type[RankFactory] = RankFactory
    _validator: type[RankValidatorFactory]
    _search_service: type[RankSearchService]
    _coord_service: CoordService
    
    def __init__(
            self,
            factory: type[RankFactory] = RankFactory,
            search_service: type[RankSearchService] = RankSearchService,
            validator: type[RankValidatorFactory] = RankValidatorFactory,
            coord_service: CoordService = CoordService()
    ):
        self._factory = factory
        self._validator = validator
        self._search_service = search_service
        self._coord_service = coord_service
        self._search_service = RankSearchService
    


    
    @property
    def search(self) -> type[RankSearchService]:
        return self._search_service
    
    def validate_rank(self, candidate) -> ValidationResult[Rank]:
        return self._validator.validate(candidate)
    
    def build_king_rank(self) -> BuildResult[King]:
        return self._factory.build_king_rank()
    
    def build_queen_rank(self) -> BuildResult[Queen]:
        return self._factory.build_queen_rank()
    
    def build_rook_rank(self) -> BuildResult[Rook]:
        return self._factory.build_rook_rank()
    
    def build_bishop_rank(self) -> BuildResult[Bishop]:
        return self._factory.build_bishop_rank()
    
    def build_knight_rank(self) -> BuildResult[Knight]:
        return self._factory.build_knight_rank()
    
    def build_pawn_rank(self) -> BuildResult[Pawn]:
        return self._factory.build_pawn_rank()
    

