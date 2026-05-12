# src/toolkit/token/toolkit.py

"""
Module: toolkit.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from microservice import CoordValidator, FormationService, RankService, TeamValidator
from model import Token
from operation import SquareValidator, ValidationBootstrapper
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
        team_validator: TeamValidator
        rank_service: RankService
        coord_validator: CoordValidator
        formation_service: FormationService
        validation_bootstrapper: ValidationBootstrapper
        
    Provides:
    
    Super Class:
    """
    REQUIRED_OPERATIONS = [
        RankService,
        SquareValidator,
        CoordValidator,
        ValidationBootstrapper,
    ]
    _rank_service: RankService
    _coord_validator: CoordValidator
    _team_validator: TeamValidator
    _square_validator: SquareValidator
    _formation_service: FormationService
    _validation_bootstrapper: ValidationBootstrapper
    
    def __init__(
        self,
        team_validator: TeamValidator | None = None,
        rank_service: RankService | None = None,
        coord_validator: CoordValidator | None = None,
        formation_service: FormationService | None = None,
        square_validator: SquareValidator | None = None,
    ):
        """
        Args:
            team_validator: TeamValidator
            rank_service: RankService
            coord_validator: CoordValidator
            formation_service: FormationService
        """
        super().__init__()
        self._rank_service = rank_service or RankService()
        self._team_validator = team_validator or TeamValidator()
        self._coord_validator = coord_validator or CoordValidator()
        self._square_validator = square_validator or SquareValidator()
        self._formation_service = formation_service or FormationService()
        
    @property
    def team_validator(self) -> TeamValidator:
        return self._team_validator
    
    @property
    def rank_service(self) -> RankService:
        return self._rank_service
    
    @property
    def coord_validator(self) -> CoordValidator:
        return self._coord_validator
    
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
    
    @property
    def square_validator(self) -> SquareValidator:
        return self._square_validator
        