# src/model/rank/pawn/__init__.py

"""
Module: model.rank.pawn.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Dict

from schema import Persona
from err import PawnException
from geometry import CoordSpan, PawnSpanner
from model import PawnToken, Rank
from result import ComputationResult
from util import LoggingLevelRouter


class Pawn(Rank):
    """
    Role:Computation, Metadata

    Responsibilities:
    1.  Produces a list of Coords reachable from a Pawn's updated position.
    2.  Metadata about the Pawn rank useful for optimizing the GameGraph.
    
    Super Class:
        Rank

    Provides:

    
    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _spanner: PawnSpanner

    def __init__(
            self,
            id: int,
            persona: Persona | None = Persona.PAWN,
            spanner: PawnSpanner | None = PawnSpanner(),
    ):
        """
        Args:
            id: int
            persona: Persona
            spanner: PawnSpanner
        """
        super().__init__(id=id, persona=persona,)
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
            # Send the exception chain on failure.
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