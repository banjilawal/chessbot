# src/logic/rank/model/concrete/bishop/bishop.py

"""
Module: logic.rank.model.concrete.bishop.bishop
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict, List

from logic.persona import Persona
from logic.span import BishopSpanner, Span
from logic.coord import Coord, CoordService
from logic.rank import BishopException, Rank
from logic.system import ComputationResult, LoggingLevelRouter
from logic.vector import VectorService


class Bishop(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Bishop's updated position.
    2.  Metadata about the Bishop rank useful for optimizing the GameGraph.

    # PARENT:
        Rank

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        * diagonal_span (DiagonalSpanComputer)

    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _spanner: BishopSpanner
    
    def __init__(
            self,
            id: int,
            persona: Persona = Persona.BISHOP,
            spanner: BishopSpanner = BishopSpanner(),
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ):
        """
        Args:
            id: int
            persona: Persona
            spanner: BishopSpanner
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
    def span_dict(self, origin: Coord) -> ComputationResult[Dict[str, Span]]:
        """
        Produce a dictionary of the coords a Bishop can reach from its current position.
        
        Args:
            origin: Coord
            
        Raises:
            BishopException
            
        Returns:
            ComputationResult[Dict[str, Span]]
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
        
        
        
        
        
    