# src/model/rank/bishop/model.py

"""
Module: model.rank.bishop.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from schema import Persona
from err import BishopException
from geometry import BishopSpanner
from model import Rank
from result import ComputationResult
from util import LoggingLevelRouter


class Bishop(Rank):
    """
    Role:Computation, Metadata

    Responsibilities:
    1.  Produces a list of Coords reachable from a Bishop's updated position.
    2.  Metadata about the Bishop rank useful for optimizing the GameGraph.

    Super Class:
        Rank

    Provides:

    # LOCAL ATTRIBUTES:
        * diagonal_span (DiagonalSpanComputer)

    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _spanner: BishopSpanner
    
    def __init__(
            self,
            persona: Persona | None = Persona.BISHOP,
            spanner: BishopSpanner | None = BishopSpanner(),
    ):
        """
        Args:
                        persona: Persona
            spanner: BishopSpanner
        """
        super().__init__(
            id=id,
            persona=persona,
        )
        self._spanner = spanner
        
    @LoggingLevelRouter.monitor
    def span_dict(self, origin: Coord) -> ComputationResult:
        """
        Produce a dictionary of the coords a Bishop can reach from its current position.
        
        Args:
            origin: Coord
            
        Raises:
            BishopException
            
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
                BishopException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    err_code=BishopException.ERR_CODE,
                    msg=BishopException.MSG,
                    ex=span_result.exception
                )
            )
        # --- Send the success resul to the client. ---#
        return span_result
        
        
        
        
        
    