# src/model/rank/model.py

"""
Module: model.rank.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import CoordService, VectorService
from model import Model
from schema import Persona


class Rank(Model):
    """
    Role:Computation
    
    Responsibilities:
        1.  Determines how a Token can move.
        2.  How many points its worth.
        
    Attributes:
        persona: Persona
        coord_service: CoordService
        vector_service: VectorService

    Provides:
        -   dict span_dict(self) -> ComputationResult[Dict[str, CoordSpan]]:
        
    Super Class:
        Model
    """
    _persona: Persona
    _coord_service: CoordService
    _vector_service: VectorService
    
    def __init__(self,persona: Persona,):
        """
        Args:
            persona: Persona
        """
        self._persona = persona
        self._coord_service = CoordService()
        self._vector_service = VectorService()
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service
    
    @property
    def persona(self) -> Persona:
        return self._persona
    
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
            return self._persona == other.persona
        return False

    
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