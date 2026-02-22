# src/chess/rank/model/concrete/bishop/bishop.py

"""
Module: chess.rank.model.concrete.bishop.bishop
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from __future__ import annotations

from typing import List

from chess.graph import Graph
from chess.square import SquareContext
from chess.token import Token
from chess.coord import Coord
from chess.persona import Persona
from chess.geometry import Quadrant
from chess.system import ComputationResult, IdFactory, LoggingLevelRouter
from chess.rank import BishopSpanComputationException, DiagonalSpan, Rank, Bishop

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
        * diagonal_span (DiagonalSpan)

    INHERITED ATTRIBUTES:
        *   See Rank class for inherited attributes
    """
    _diagonal_span: DiagonalSpan
    
    def __init__(
            self,
            id: int,
            name: str = Persona.BISHOP.name,
            ransom: int = Persona.BISHOP.ransom,
            team_quota: int = Persona.BISHOP.quota,
            designation: str = Persona.BISHOP.designation,
            quadrants: List[Quadrant] = List[Persona.BISHOP.quadrants],
            diagonal_span: DiagonalSpan = DiagonalSpan(),
    ):
        super().__init__(
            id=id,
            name=name,
            ransom=ransom,
            team_quota=team_quota,
            designation=designation,
            quadrants=quadrants,
            vectors=None
        )
        self._diagonal_span = diagonal_span
    
    @LoggingLevelRouter.monitor
    def compute_span(self, token: Token,) -> ComputationResult[[Coord]]:
        """
        # Action
            1.  Pass the occupant's updated position to Rook._perpendicular_span to get the set of possible destinations.
            2.  If perpendicular_span fails send the exception chain in the ComputationResult. Else, return
                the span in the ComputationResult's payload.
        # PARAMETERS:
            *   occupant (Token)
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   RookException
            *   RookSpanComputationException
        """
        method = "Bishop.compute_span"
        
        # --- Compute the Bishop's possible destinations. ---#
        computation_result = self._diagonal_span.compute(
            points=[],
            origin=token.current_position,
            coord_service=self.coord_service
        )
        # Handle the case that spanning set computation does not produce a solution.
        if computation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                BishopSpanComputationException(
                    message=f"{method}: {BishopSpanComputationException.DEFAULT_MESSAGE}",
                    ex=computation_result.exception
                )
            )
        # Put the completed Bishop's span into a ComputationResult and send to the caller.
        return computation_result
    
    @LoggingLevelRouter.monitor
    def compute_graph(self, token: Token, id_factory: IdFactory = IdFactory()) -> ComputationResult[Graph]:
        method = "Bishop.compute_graph"
        
        # --- Initialize the graph and compute the spanning set. ---#
        graph = Graph(id=id_factory.next_id(class_name="Graph"))
        span_computation_result = self.compute_span(token=token)
        
        # Handle the case that the spanning set computation does not produce a solution.
        if span_computation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                BishopGraphComputationException(
                    message=f"{method}: {BishopGraphComputationException.DEFAULT_MESSAGE}",
                    ex=span_computation_result.exception
                )
            )
        
        i = 0
        j += 1
        
        while j < len(span_computation_result.payload):
            
            # --- Find square_u. ---#
            square_u_search_result = token.board.squares.search(
                context=SquareContext(coord=span_computation_result.payload[i])
            )
            # Handle the case that the square_u search was not completed.
            if square_u_search_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    BishopGraphComputationException(
                        message=f"{method}: {BishopGraphComputationException.DEFAULT_MESSAGE}",
                        ex=square_u_search_result.exception
                    )
                )
            square_u = square_u_search_result.payload
            
            # --- Find square_v. ---#
            square_v_search_result = token.board.squares.search(
                context=SquareContext(coord=span_computation_result.payload[i])
            )
            # Handle the case that the square_u search was not completed.
            if square_v_search_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    BishopGraphComputationException(
                        message=f"{method}: {BishopGraphComputationException.DEFAULT_MESSAGE}",
                        ex=square_v_search_result.exception
                    )
                )
            square_v = square_u_search_result.payload
            Build
            square_a_search_result = token.board.squares.search(
                context=SquareContext(coord=span_computation_result.payload[i])
            )
            if square_a_search_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    BishopGraphComputationException(
                        message=f"{method}: {BishopGraphComputationException.DEFAULT_MESSAGE}",
                        ex=span_computation_result.exception
                    )
                )
        previous_coord = span_computation_result.payload[0]
        for i in range(len(span_computation_result.payload)):
            j += 1
            
        
        
        
        
        
    