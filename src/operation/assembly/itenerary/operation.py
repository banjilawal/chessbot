# src/operation/assembly/itinerary/operation.py

"""
Module: operation.assembly.itinerary.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import ItineraryBlueprint
from result import BuildResult
from operation import Assembler
from util import  LoggingLevelRouter
from model import Itinerary

class ItineraryAssembler(Assembler[Itinerary]):
    NAME = "itinerary_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: ItineraryBlueprint,) -> BuildResult[Itinerary]:
        """
        Assemble the appropriate Itinerary.

        Args:
            blueprint: ItineraryBlueprint
        Returns:
            BuildResult[Itinerary]
        Raises:
        """
        method = f"{cls.__name__}.execute"
        return BuildResult.success(
            Itinerary(
                id=blueprint.id,
                source=blueprint.source,
                token=blueprint.token,
                destination=blueprint.destination,
            )
        )
    
    
    

        
        
