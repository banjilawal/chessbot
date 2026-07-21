# src/assembler/itinerary/py

"""
Module: assembler.itinerary.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import ItineraryBlueprint
from result import BuildResult
from assembler import Assembler
from util import  LoggingLevelRouter
from model import Itinerary

class ItineraryAssembler(Assembler[Itinerary]):
    NAME = "itinerary_assembler"
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ItineraryBlueprint,) -> BuildResult[Itinerary]:
        """
        Assemble the appropriate Itinerary.

        Args:
            blueprint: ItineraryBlueprint
        Returns:
            BuildResult[Itinerary]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(
            Itinerary(
                id=blueprint.id,
                source=blueprint.source,
                token=blueprint.token,
                destination=blueprint.destination,
            )
        )
    
    
    

        
        
