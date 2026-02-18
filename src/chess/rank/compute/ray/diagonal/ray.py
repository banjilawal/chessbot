# src/chess/rank/compute/ray/diagonal/ray.py

"""
Module: chess.rank.compute.ray.diagonal.ray
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.board import Board
from chess.graph import Vertex
from chess.square import SquareContext
from chess.token import Token
from chess.coord import Coord, CoordService
from chess.rank import DiagonalRayComputationFailedException
from chess.system import BuildResult, ComputationResult, LoggingLevelRouter
from chess.vector import VectorService


class DiagonalRay:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            token: Token,
            start_x: int,
            end_x: int,
            x_step: int,
            end_y: int,
            slope: int,
            span: [Coord] =  List[Coord],
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[List[Coord]]:
        """
        # Action
            1.  Iterate over the range of start_x to end_x with step x_step.
            2.  For each x find the y value using the slope.
            3.  Build a Coord from the x, y pair.
            4.  If the Coord is not in span, append it.
            5.  End the loop when x >= end_x and y >= end_y.
        PARAMETERS:
            *   start_x (int):          Starting x value. In practice, it will be occupant.current_position.column.
            *   end_x (int):            Ending x value. This will be either 0 or NUMBER_OF_COLUMNS - 1.
            *   x_step (int):           Step size for x. In practice, the magnitude will be 1,
                                        the sign may be negative.
            *   end_y (int):            Ending y value. This will be either 0 or NUMBER_OF_ROWS - 1 depending on the
                                        direction of travel.
            *   slope (int):            Slope of the diagonal. Used to find next y value.
            *   span (List[Coord]):     List to append Coords to if they are not already in the list.
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        RAISES:
            *   DiagonalRayComputationFailedException
        """
        method = "DiagonalRay.compute"
        
        origin = token.coord
        i = origin.column
        j = (2 * slope * i) + slope
        previous_square = None
        while i < end_x and j < end_y:
            # Handle the case that the coord is not built.
            build_result = coord_service.builder.build(row=j, column=i)
            # Return the exception chain on failure.
            if build_result.is_failure:
                return BuildResult.failure(
                    DiagonalRayComputationFailedException(
                        message=f"{method}: {DiagonalRayComputationFailedException.DEFAULT_MESSAGE}",
                        ex=build_result.exception
                    )
                )
            square_search_result = token.team.board.squares.search(context=SquareContext(coord=build_result.payload))
            if square_search_result.is_failure:
                # Return the exception chain on failure.
                if build_result.is_failure:
                    return BuildResult.failure(
                        DiagonalRayComputationFailedException(
                            message=f"{method}: {DiagonalRayComputationFailedException.DEFAULT_MESSAGE}",
                            ex=build_result.exception
                        )
                    )
                
            if build_result.payload not in span:
                span.append(build_result.payload)
            i += x_step
            j = (2 * slope * i) + slope
        return ComputationResult.success(payload=span)
    
    @LoggingLevelRouter.monitor
    def vertex_builder(
            self,
            coord: Coord,
            board: Board,
            vector_service: VectorService = VectorService()
    ) -> BuildResult[Vertex]:
        """
        """
        method = "DiagonalRay.vertex_builder"
        
        square_search_result = board.squares.search(context=SquareContext(coord=coord))
        if square_search_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                DiagonalRayComputationFailedException(
                    message=f"{method}: {DiagonalRayComputationFailedException.DEFAULT_MESSAGE}",
                    ex=square_search_result.exception
                )
            )
        vector_build_result = vector_service.builder.build(square=square_search_result.payload)
        if vector_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                DiagonalRayComputationFailedException(
                    message=f"{method}: {DiagonalRayComputationFailedException.DEFAULT_MESSAGE}",
                    ex=vector_build_result.exception
                )
            )
        return BuildResult.success(payload=vector_build_result.payload)