# src/toolkit/token/toolkit.py

"""
Module: toolkit.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import NumberValidator, SquareValidator
from microservice import CoordService, FormationService, IdentityService, RankService, TeamService
from model import Token
from toolkit import Toolkit


class TokenToolkit(Toolkit[Token]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        team_service: TeamService
        rank_service: RankService
        coord_service: CoordService
        identity_service: IdentityService
        number_validation: NumberValidator
        formation_service: FormationService
        
    Provides:
    
    Super Class:
    """
    _team_service: TeamService
    _rank_service: RankService
    _coord_service: CoordService
    _identity_service: IdentityService
    _number_validation: NumberValidator
    _formation_service: FormationService
    _square_validator: SquareValidator
    
    def __init__(
        self,
        team_service: TeamService | None = None,
        rank_service: RankService | None = None,
        coord_service: CoordService | None = None,
        identity_service: IdentityService | None = None,
        number_validation: NumberValidator | None = None,
        formation_service: FormationService | None = None,
        square_validator: SquareValidator | None = None,
    ):
        """
        Args:
            team_service: TeamService
            rank_service: RankService
            coord_service: CoordService
            identity_service: IdentityService
            number_validation: NumberValidator
            formation_service: FormationService
        """
        super().__init__()
        self._team_service = team_service or TeamService()
        self._rank_service = rank_service or RankService()
        self._coord_service = coord_service or CoordService()
        self._identity_service = identity_service or IdentityService()
        self._number_validation = number_validation or NumberValidator()
        self._formation_service = formation_service or FormationService()
        self._square_validator = square_validator or SquareValidator()
        
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
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def number_validation(self) -> NumberValidator:
        return self._number_validation
    
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
    
    @property
    def square_validator(self) -> SquareValidator:
        return self._square_validator
        