# src/logic/rank/model/concrete/pawn/pawn.py

"""
Module: logic.rank.model.concrete.pawn.pawn
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from logic.persona import Persona
from logic.token import PawnToken
from logic.coord import CoordService
from logic.vector import VectorService
from logic.span import PawnSpanner, CoordSpan
from logic.rank import PawnException, Rank
from logic.system import ComputationResult, LoggingLevelRouter

class Pawn(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Pawn's updated position.
    2.  Metadata about the Pawn rank useful for optimizing the GameGraph.
    
    # PARENT:
        Rank

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _spanner: PawnSpanner

    def __init__(
            self,
            id: int,
            persona: Persona = Persona.PAWN,
            spanner: PawnSpanner = PawnSpanner(),
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ):
        """
        Args:
            id: int
            persona: Persona
            spanner: PawnSpanner
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
    def span_dict(self, pawn_token: PawnToken) -> ComputationResult[Dict[str, CoordSpan]]:
        """
        Produce a dictionary of the coords a Pawn can reach from its current position.

        Args:
            pawn_token: PawnToken

        Raises:
            PawnException

        Returns:
            ComputationResult[Dict[str, CoordSpan]]
        """
        method = f"{self.__class__.__name__}.span_dict"
        
        span_result = self._spanner.compute(
            pawn_token=pawn_token,
            coord_service=self.coord_service,
            vector_service=self.vector_service,
        )
        # Handle the case that, the span is not produced.
        if span_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                PawnException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    err_code=PawnException.ERR_CODE,
                    msg=PawnException.MSG,
                    ex=span_result.exception
                )
            )
        # --- Send the success resul to the client. ---#
        return span_result