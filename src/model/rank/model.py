# src/model/rank/model.py

"""
Module: model.rank.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict

from geometry import CoordSpan
from microservice import CoordService, VectorService
from model import Persona
from result import ComputationResult
from system import LoggingLevelRouter


class Rank(ABC):
    """
    Role:Computation
    
    Responsibilities:
        1.  Determines how a Token can move.
        2.  How many points its worth.
        
    Attributes:
        id: int
        persona: Persona
        coord_service: CoordService
        vector_service: VectorService

    Provides:
        -   dict span_dict(self) -> ComputationResult[Dict[str, CoordSpan]]:
        
    Super Class:
    """
    _persona: Persona
    _coord_service: CoordService
    _vector_service: VectorService
    
    def __init__(self,
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