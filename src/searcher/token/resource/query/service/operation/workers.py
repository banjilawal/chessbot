# src/logic/token/database/searcher/context/service/operation/workers.py

"""
Module: logic.token.database.searcher.context.service.operation.workers
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from schema.persona import PersonaService
from logic.rank import RankService
from logic.team import TeamService
from logic.coord import CoordService
from logic.square import SquareService
from system import GameColorValidator, IdentityService, NumberValidator

class TokenContextIntegrityWorkers:
    """
    Role:
        -   Container

    Responsibilities:
        1.  Reduces the number params in TokenContext Builder and Validator entry points.

    Attributes:
        team_service: TeamService
        rank_service: RankService
        coord_service: CoordService
        square_service: SquareService
        number_validator: NumberValidator
        identity_service: IdentityService
        color_validator: GameColorValidator

    Provides:

    Super Class:
    """
    _team_service: TeamService
    _rank_service: RankService
    _coord_service: CoordService
    _square_service: SquareService
    _persona_service: PersonaService
    _identity_service: IdentityService
    _number_validator: NumberValidator
    _color_validator: GameColorValidator
    
    def __init__(
            self,
            team_service: TeamService = TeamService(),
            rank_service: RankService = RankService(),
            coord_service: CoordService = CoordService(),
            square_service: SquareService = SquareService(),
            persona_service: PersonaService = PersonaService(),
            number_validator: NumberValidator = NumberValidator(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ):
        """
        Args:
            team_service: TeamService
            rank_service: RankService
            coord_service: CoordService
            square_service: SquareService
            identity_service: IdentityService
            number_validator: NumberValidator
            color_validator: GameColorValidator
          
        """
        self._team_service = team_service
        self._rank_service = rank_service
        self._coord_service = coord_service
        self._square_service = square_service
        self._color_validator = color_validator
        self._persona_service = persona_service
        self._number_validator = number_validator
        self._identity_service = identity_service
        
    @property
    def team_service(self) -> TeamService:
        return self._team_service
    
    @property
    def rank_service(self) -> RankService:
        return self._rank_service
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def square_service(self) -> SquareService:
        return self._square_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
    
    @property
    def color_validator(self) -> GameColorValidator:
        return self._color_validator
    
    @property
    def persona_service(self) -> PersonaService:
        return self._persona_service
    

        
