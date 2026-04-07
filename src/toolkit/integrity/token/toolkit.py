# src/toolkit/integrity/token/toolkit.py

"""
Module: toolkit.integrity.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

import dataclasses

from model import Token
from toolkit import IntegrityToolkit
from integrity import NumberValidator
from microservice import CoordService, FormationService, IdentityService, RankService, TeamService


@dataclasses.dataclass
class TokenIntegrityToolkit(IntegrityToolkit[Token]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Reduce number of params in Token builders and validators.
        2.  Simplifies entry points

    Attributes:
        team_service: TeamService
        rank_service: RankService
        coord_service: CoordService
        identity_service: IdentityService
        number_validation: NumberValidator
        formation_service: FormationService

    Provides:

    Super Class:
    IntegrityToolkit
    """
    team_service: TeamService
    rank_service: RankService
    coord_service: CoordService
    identity_service: IdentityService
    number_validator: NumberValidator
    formation_service: FormationService
 

        
