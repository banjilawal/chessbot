# src/integrity/toolkit/token/toolkit.py

"""
Module: integrity.toolkit.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import NumberValidator
from microservice import CoordService, FormationService, IdentityService, RankService, TeamService
from model import Token
from toolkit import Toolkit


class TokenToolkit(Toolkit[Token]):
    """
    Role:
        -   Container
        
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
    
    def __init__(
        self,
        team_service: TeamService | None = None,
        rank_service: RankService | None = None,
        coord_service: CoordService | None = None,
        identity_service: IdentityService | None = None,
        number_validation: NumberValidator | None = None,
        formation_service: FormationService | None = None,
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
        self._team_service = team_service
        self._rank_service = rank_service
        self._coord_service = coord_service
        self._identity_service = identity_service
        self._number_validation = number_validation
        self._formation_service = formation_service
        
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
        