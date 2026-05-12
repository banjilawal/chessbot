# src/toolkit/square/toolkit.py

"""
Module: toolkit.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analysis import SquareCollisionAnalyst
from integrity import BoardValidator, CoordValidator
from microservice import FormationService, IdentityService
from model import Square
from operation import ValidationBootstrapper
from toolkit import Toolkit


class SquareToolkit(Toolkit[Square]):
    """
    Role:
        -   Container
        -   Data Holder
    
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
        board_validator: BoardValidator
        coord_validator: CoordValidator
        identity_service: IdentityService
        formation_service: FormationService
        collision_analyst: SquareCollisionAnalyst
    
    Provides:
    
    Super Class:
        Toolkit
    """
    [
        IdentityService,
        FormationService,
        BoardValidator,
        CoordValidator,
        SquareCollisionAnalyst,
        ValidationBootstrapper
    ]
    _coord_validator: CoordValidator
    _board_validator: BoardValidator
    _formation_service: FormationService
    _collision_analyst: SquareCollisionAnalyst
    
    def __init__(
            self,
            board_validator: BoardValidator | None = None,
            coord_validator: CoordValidator | None = None,
            formation_service: FormationService | None = None,
            collision_analyst: SquareCollisionAnalyst | None = None,
    ):
        """
        Args:
            board_validator: BoardValidator
            coord_validator: CoordValidator
            formation_service: FormationService
            collision_analyst: SquareCollisionAnalyst
        """
        super().__init__()
        self._board_validator = board_validator or BoardValidator()
        self._coord_validator = coord_validator or CoordValidator()
        self._formation_service = formation_service or FormationService()
        self._collision_analyst = collision_analyst or SquareCollisionAnalyst()
    
    @property
    def board_validator(self) -> BoardValidator:
        return self._board_validator
    
    @property
    def coord_validator(self) -> CoordValidator:
        return self._coord_validator
    
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
    
    @property
    def collision_analyst(self) -> SquareCollisionAnalyst:
        return self._collision_analyst