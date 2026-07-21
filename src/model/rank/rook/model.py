# src/model/rank/rook/model.py

"""
Module: model.rank.rook.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Dict

from schema import Persona
from err import RookException
from geometry import CoordSpan, RookSpanner
from model import Coord, Rank
from result import ComputationResult


class Rook(Rank):
    """
    Role:Computation, Metadata

    Responsibilities:
    1.  Produces a list of Coords reachable from a Rook's updated position.
    2.  Metadata about the Rook rank useful for optimizing the GameGraph.
    
    Super Class:
        Rank

    Provides:

    
    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _spanner: RookSpanner

    def __init__(
            self,
            persona: Persona | None = Persona.ROOK,
            spanner: RookSpanner | None = RookSpanner(),
    ):
        """
        Args:
            persona: Persona
            spanner: RookSpanner
            coord_service: CoordService
            vector_service: VectorService
        """
        super().__init__(
            id=id,
            persona=persona,
        )
        self._spanner = spanner
    
    @LoggingLevelRouter.monitor
    def span_dict(self, origin: Coord) -> ComputationResult:
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
            # Send the exception chain on failure.
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