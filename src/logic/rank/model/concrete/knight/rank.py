# src/logic/rank/model/concrete/knight/knight.py

"""
Module: logic.rank.model.concrete.knight.knight
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from logic.persona import Persona
from logic.vector import VectorService
from logic.span import KnightSpanner, Span
from logic.rank import KnightException, Rank
from logic.coord import Coord, CoordService
from logic.system import ComputationResult, LoggingLevelRouter

class Knight(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Knight's updated position.
    2.  Metadata about the Knight rank useful for optimizing the GameGraph.
    
    # PARENT:
        Rank

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _spanner: KnightSpanner

    def __init__(
            self,
            id: int,
            persona: Persona = Persona.KNIGHT,
            spanner: KnightSpanner = KnightSpanner(),
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ):
        """
        Args:
            id: int
            persona: Persona
            spanner: KnightSpanner
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
        Produce a dictionary of the coords a Knight can reach from its current position.

        Args:
            origin: Coord

        Raises:
            KnightException

        Returns:
            ComputationResult[Dict[str, Span]]
        """
        method = f"{self.__class__.__name__}.span_dict"
        
        span_result = self._spanner.compute(
            origin=origin,
            vectors=self.persona.vectors,
            coord_service=self.coord_service,
            vector_service=self.vector_service,
        )
        # Handle the case that, the span is not produced.
        if span_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                KnightException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    err_code=KnightException.ERR_CODE,
                    msg=KnightException.MSG,
                    ex=span_result.exception
                )
            )
        # --- Send the success resul to the client. ---#
        return span_result