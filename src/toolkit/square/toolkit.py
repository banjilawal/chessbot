# src/toolkit/square/toolkit.py

"""
Module: toolkit.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import nonmember

from analysis import SquareCollisionAnalyst
from integrity import NumberValidator
from microservice import BoardService, CoordService, IdentityService
from model import Square
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
        board_service: BoardService
        coord_service: CoordService
        number_validator: NumberValidator
        identity_service: IdentityService
        collision_analyst: SquareCollisionAnalyst
    
    Provides:
    
    Super Class:
        Toolkit
    """
    _coord_service: CoordService
    _board_service: BoardService
    _number_validator: NumberValidator
    _identity_service: IdentityService
    _collision_analyst: SquareCollisionAnalyst
    
    def __init__(
            self,
            board_service: BoardService | None = None,
            coord_service: CoordService | None = None,
            number_validator: NumberValidator | None = None,
            identity_service: IdentityService  | None = None,
            collision_analyst: SquareCollisionAnalyst | None = None,
    ):
        """
        Args:
            board_service: BoardService
            coord_service: CoordService
            number_validator: NumberValidator
            identity_service: IdentityService
            collision_analyst: SquareCollisionAnalyst
        """
        self._board_service = board_service or BoardService()
        self._coord_service = coord_service or CoordService()
        self._number_validator = number_validator or NumberValidator()
        self._identity_service = identity_service or (IdentityService())
        self._collision_analyst = collision_analyst or SquareCollisionAnalyst()
    
    @property
    def board_service(self) -> BoardService:
        return self._board_service
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def collision_analyst(self) -> SquareCollisionAnalyst:
        return self._collision_analyst