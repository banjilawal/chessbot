# src/tool/token/tool.py

"""
Module: tool.token.tool
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import NumberValidator
from microservice import CoordService, FormationService, RankService, TeamService, VectorService
from model import Token
from system import IdentityService
from tool import ToolSet


class TokenTool(ToolSet[Token]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Reduces the declarations of common security resources in Vector, Coord,
            and Scalar tokenic workers.

    Attributes:
        team_service: TeamService
        rank_service: RankService
        coord_service: CoordService
        identity_service: IdentityService
        number_validation: NumberValidator
        formation_service: FormationService

    Provides:

    Super Class:
    ToolSet
    """
    _team_service: TeamService
    _rank_service: RankService
    _coord_service: CoordService
    _identity_service: IdentityService
    _number_validation: NumberValidator
    _formation_service: FormationService
   
    def __init__(
            self,
            team_service: TeamService = TeamService(),
            rank_service: RankService = RankService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            number_validation: NumberValidator = NumberValidator(),
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
        self._coord_service = coord_service
        self._vector_service = vector_service
        self._number_validator = number_validator
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service

    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
    

        
