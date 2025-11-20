# src/chess/piece/service/service.py

"""
Module: chess.piece.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""
from chess.coord import Coord, CoordService
from chess.rank import Rank, RankService
from chess.system import BuildResult, IdentityService, Service
from chess.piece import Piece, PieceValidator, PieceBuilder
from chess.team import Team, TeamService


class PieceService(Service[Piece]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for Piece, PieceValidator and PieceBuilder.
    2.  Protects Piece objects from direct manipulation.
    3.  Extends behavior and functionality of Piece objects.
    4.  Public facing API for Piece modules.
  
    # PROVIDES:
        *   Piece building
        *   Piece validation

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   builder (PieceBuilder)
        *   validator (PieceValidator)
        *   identity_service (IdentityService)
        *   coord_stack_service (CoordStackService)
    """
    SERVICE_NAME = "PieceService"
    
    _id: int
    _name: str
    _builder: type[PieceBuilder]
    _validator: type[PieceValidator]
    _identity_service: IdentityService
    _coord_service: CoordService
    _rank_service: RankService
    _team_service: TeamService
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: type[PieceBuilder] = PieceBuilder,
            validator: type[PieceValidator] = PieceValidator,
            rank_service: RankService = RankService(),
            team_service: TeamService = TeamService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            
    ):
        super().__init__(id=id, name=name)
        self._builder = builder
        self._validator = validator
        self._coord_service = coord_service
        self._rank_service = rank_service
        self._team_service = team_service
        self._identity_service = identity_service
    

    @property
    def validator(self) -> type[PieceValidator]:
        """
        CoordValidator is the single-source-of truth for certifying the safety of
        Piece instances, their organic row and column attributes. It makes sense
        providing direct access here and letting validator return its Validation
        result directly to the caller.
        """
        return self._validator
    
    def build_piece(
            self,
            id: int,
            name: str,
            coord: Coord,
            rank: Rank,
            team: Team
    ) -> BuildResult[Piece]:
        return self._builder.build(
            id=id,
            name=name,
            coord=coord,
            rank=rank,
            team=team,
            team_service=self._team_service,
            rank_service=self._rank_service,
            coord_service=self._coord_service,
            identity_service=self._identity_service,
        )
