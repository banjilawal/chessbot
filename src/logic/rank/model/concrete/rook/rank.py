# src/logic/rank/model/concrete/rook/rook.py

"""
Module: logic.rank.model.concrete.rook.rook
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from logic.persona import Persona
from logic.vector import VectorService
from logic.span import RookSpanner, CoordSpan
from logic.rank import RookException, Rank
from logic.coord import Coord, CoordService
from logic.system import ComputationResult, LoggingLevelRouter

class Rook(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Rook's updated position.
    2.  Metadata about the Rook rank useful for optimizing the GameGraph.
    
    # PARENT:
        Rank

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _spanner: RookSpanner

    def __init__(
            self,
            id: int,
            persona: Persona = Persona.ROOK,
            spanner: RookSpanner = RookSpanner(),
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ):
        """
        Args:
            id: int
            persona: Persona
            spanner: RookSpanner
            coord_service: CoordService
            vector_service: VectorService
        """
        super().__init__(
            id=id,
            persona=persona,
            coord_service=coord_service,
            vector_service=vector_service
        )
        self._spanner = spanner
    
    @LoggingLevelRouter.monitor
    def span_dict(self, origin: Coord) -> ComputationResult[Dict[str, CoordSpan]]:
        """
        Produce a dictionary of the coords a Rook can reach from its current position.

        Args:
            origin: Coord
            
        Raises:
            RookException

        Returns:
            ComputationResult[Dict[str, CoordSpan]]
        """
        method = f"{self.__class__.__name__}.span_dict"
        
        span_result = self._spanner.compute(
            origin=origin,
            coord_service=self.coord_service,
        )
        # Handle the case that, the span is not produced.
        if span_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                RookException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    err_code=RookException.ERR_CODE,
                    msg=RookException.MSG,
                    ex=span_result.exception
                )
            )
        # --- Send the success resul to the client. ---#
        return span_result