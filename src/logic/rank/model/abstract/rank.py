# src/logic/rank/model/abstract/rank.py

"""
Module: logic.rank.model.abstract.rank
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict

from logic.persona import Persona
from logic.span import CoordSpan
from logic.vector import VectorService
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
    _coord_service: CoordService
    _vector_service: VectorService
    
    def __init__(self,
            id: int,
            persona: Persona,
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ):
        """
        Args:
            id: int
            persona: Persona
            coord_service: CoordService
            vector_service: VectorService
        """
        self._id = id
        self._persona = persona
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
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def span_dict(self) -> ComputationResult[Dict[str, CoordSpan]]:
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