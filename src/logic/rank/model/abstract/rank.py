# src/logic/rank/model/abstract/rank.py

"""
Module: logic.rank.model.abstract.rank
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from logic.persona import Persona
from logic.span import Span
from logic.vector import Vector, VectorService
from logic.geometry import Quadrant
from logic.coord import CoordService
from logic.system import ComputationResult, LoggingLevelRouter

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
    _persona: Persona
    # _name: str
    # _designation: str
    # _ransom: int
    # _team_quota: int
    # _quadrants: List[Quadrant]
    # _vectors: Optional[Vector]
    _coord_service: CoordService
    _vector_service: VectorService
    
    def __init__(self,
            id: int,
            persona: Persona,
            # name: str,
            # persona: Persona,
            # designation: str,
            # ransom: int,
            # team_quota: int,
            # quadrants: List[Quadrant],
            # vectors: Optional[Vector] = None,
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ):
        self._id = id
        self._persona = persona
        # self._name = name
        # self._ransom = ransom
        # self._persona = persona
        # self._team_quota = team_quota
        # self._designation = designation
        # self._quadrants = quadrants
        # self._vectors = vectors
        self._coord_service = coord_service
        self._vector_service = vector_service
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service
    
    @property
    def persona(self) -> Persona:
        return self._persona
    
    @property
    def id(self) -> int:
        return self._id
    #
    # @property
    # def name(self) -> str:
    #     return self._name
    #
    # @property
    # def designation(self) -> str:
    #     return self._designation
    #
    # @property
    # def ransom(self) -> int:
    #     return self._ransom
    #
    # @property
    # def quadrants(self) -> List[Quadrant]:
    #     return self._quadrants
    #
    # @property
    # def vectors(self) -> Optional[List[Vector]]:
    #     return self._vectors
    #
    # @property
    # def team_quota(self) -> int:
    #     return self._team_quota
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def span_dict(self) -> ComputationResult[Dict[str, Span]]:
        pass
    
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
    
    # def __str__(self):
    #     return (
    #         "bounds: {"
    #         f"id:{self._id}, "
    #         f"designation:{self._name}, "
    #         f"designation:{self._designation}, "
    #         f"ransom:{self._ransom}, "
    #         f"team_quota:{self._team_quota}"
    #         "}"
    #     )