# src/model/rank/king/model.py

"""
Module: model.rank.king.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from schema import Persona
from err import KingException
from geometry import KingSpanner
from model import Coord, Rank
from result import ComputationResult
from util import LoggingLevelRouter


class King(Rank):
    """
    Role:Computation, Metadata

    Responsibilities:
    1.  Produces a list of Coords reachable from a King's updated position.
    2.  Metadata about the King rank useful for optimizing the GameGraph.
    
    Super Class:
        Rank

    Provides:

    
    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _spanner: KingSpanner

    def __init__(
            self,
            persona: Persona | None = Persona.KING,
            spanner: KingSpanner | None = KingSpanner(),
    ):
        """
        Args:
                        persona: Persona
            spanner: KingSpanner
        """
        super().__init__(
            id=id,
            persona=persona,
        )
        self._spanner = spanner
    
    @LoggingLevelRouter.monitor
    def span_dict(self, origin: Coord) -> ComputationResult:
        """
        Produce a dictionary of the coords a King can reach from its current position.

        Args:
            origin: Coord

        Raises:
            KingException

        Returns:
            ComputationResult[Dict[str, CoordSpan]]
        """
        method = f"{self.__class__.__name__}.span_dict"
        
        span_result = self._spanner.compute(
            origin=origin,
            vectors=self.persona.vectors,
            coord_service=self.coord_service,
            vector_service=self._vector_service,
        )
        # Handle the case that, the span is not produced.
        if span_result.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                KingException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    err_code=KingException.ERR_CODE,
                    msg=KingException.MSG,
                    ex=span_result.exception
                )
            )
        # --- Send the success resul to the client. ---#
        return span_result