# src/tool/square/tool.py

"""
Module: tool.square.tool
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import BoardService, CoordService
from microservice.square.operation import SquareCollisionAnalyst
from system import IdentityService, NumberValidator


class SquareTool:
    """
    Role:
        -   Container

    Responsibilities:
        1.  Reduces the declarations of common security resources in Vector, Coord,
            and Scalar square ic workers.

    Attributes:
        board_service: BoardService
        coord_service: CoordService
        identity_service: IdentityService
        collision_analyst: SquareCollisionAnalyst
        
    Provides:

    Super Class:
    ToolSet
    """
    _coord_service: CoordService
    _board_service: BoardService
    _number_validator: NumberValidator
    _identity_service: IdentityService
    _collision_analyst: SquareCollisionAnalyst
   
    def __init__(
            self,
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            collision_analyst: SquareCollisionAnalyst = SquareCollisionAnalyst(),
    ):
        """
        Args:
            board_service: BoardService
            coord_service: CoordService
            identity_service: IdentityService
            collision_analyst: SquareCollisionAnalyst
        """
        self._board_service = board_service
        self._coord_service = coord_service
        self._identity_service = identity_service
        self._collision_analyst = collision_analyst
        
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

    

        
