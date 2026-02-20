# src/chess/rank/model/abstract.py

"""
Module: chess.rank.model.abstract
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from chess.geometry import Quadrant
from chess.coord import Coord, CoordService
from chess.system import ComputationResult, LoggingLevelRouter
from chess.token import Token, TokenService
from chess.vector import Vector


class Rank(ABC):
    """
    # ROLE: Computation

    # RESPONSIBILITIES:
    1.  Single-source-of-truth of Coords reachable from a Token's updated position on the board.
    2.  Metadata for weighing edges in the GameGraph.
    3.  Hosting logic common to Rank subclasses.

    # PROVIDES:
    Rank

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   ransom (int)
        *   team_quota (int)
        *   designation(str)
        *   quadrants (List[Quadrant]):
        *   vectors (List[Vector])
    """
    _id: int
    _name: str
    _designation: str
    _ransom: int
    _team_quota: int
    _quadrants: List[Quadrant]
    _vectors: Optional[Vector]
    _coord_service: CoordService
    
    def __init__(self,
            id: int,
            name: str,
            designation: str,
            ransom: int,
            team_quota: int,
            quadrants: List[Quadrant],
            vectors: Optional[Vector] = None,
            coord_service: CoordService = CoordService(),
    ):
        self._id = id
        self._name = name
        self._ransom = ransom
        self._team_quota = team_quota
        self._designation = designation
        self._quadrants = quadrants
        self._vectors = vectors
        self._coord_service = coord_service

    @abstractmethod
    @LoggingLevelRouter.monitor
    def compute_span(self, token: Token,) -> ComputationResult[[Coord]]:
        """"""
        pass
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def designation(self) -> str:
        return self._designation
    
    @property
    def ransom(self) -> int:
        return self._ransom
    
    @property
    def quadrants(self) -> List[Quadrant]:
        return self._quadrants
    
    @property
    def vectors(self) -> Optional[List[Vector]]:
        return self._vectors
    
    @property
    def team_quota(self) -> int:
        return self._team_quota
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Rank):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return (
            "bounds: {"
            f"id:{self._id}, "
            f"designation:{self._name}, "
            f"designation:{self._designation}, "
            f"ransom:{self._ransom}, "
            f"team_quota:{self._team_quota}"
            "}"
        )