# src/domain/model/outcome/model.py.py

"""
Module: domain.model.outcome.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from microservice import CoordService, VectorService
from domain.model import Model
from domain.schema import Persona


class GameOutcome(Model):
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
        - dict span_dict(self) -> ComputationResult[Dict[str, CoordSpan]]:
        
    Super Class:
        Model
    """
    _game
    
    def __init__(self):