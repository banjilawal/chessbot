# src/chess/rank/model/concrete/pawn/compute/peacek/span.py

"""
Module: chess.rank.model.concrete.pawn.compute.peace.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List

from chess.coord import Coord, CoordService
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import PawnMoveCategory, PawnPeacefulSpanComputationFailedException



class PawnPeacefulSpan:
    """
    # RESPONSIBILITIES:
    1.  Compute the spanning subset in the horizontal and vertical plane with no duplicates.
    2.  If the computation fails send an exception chain to the caller for error tracing.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            origin: Coord,
            pawn_move_category: PawnMoveCategory,
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[List[Coord]]:
        """
        # Action
            1.  If the origin does not pass its validation checks send an exception chain in the CalculationResult.
            2.  Iterate through the vectors in the peaceful category to compute the destinations. If any of th computations
                fail send an exception in the CalculationResult. Else, the computation was successful. Send it
                IN THE ComputationResult's payload.
        # PARAMETERS:
            *   origin (Coord)
            *   peaceful_category (PawnMoveCategory)
            *   coord_service (CoordService)
            *   span (List[Coord])
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   PawnPeacefulSpanComputationFailedException
        """
        method = "PawnPeaceful.compute"
        
        # Handle the case that the coord is not certified safe.
        coord_validation = coord_service.validator.validate(candidate=origin)
        if coord_validation.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PawnPeacefulSpanComputationFailedException(
                    message=f"{method}: {PawnPeacefulSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=coord_validation.exception
                )
            )
        # Iterate through the vectors, adding each one to the origin to get the King's spanning set.
        destinations: List[Coord] = []
        for vector in pawn_move_category.peaceful_vectors:
            addition_result = coord_service.add_vector_to_coord(coord=origin, vector=vector)
            
            # Handle the case that vector addition does not produce a result.
            if addition_result.is_failure:
                # On failure return the exception chain
                return ComputationResult.failure(
                    PawnPeacefulSpanComputationFailedException(
                        message=f"{method}: {PawnPeacefulSpanComputationFailedException.DEFAULT_MESSAGE}",
                        ex=addition_result.exception
                    )
                )
            # Otherwise add the coord to the destinations.
            if addition_result.payload not in destinations:
                destinations.append(addition_result.payload)
        
        # --- The destinations have been successfully computed. Return in the ComputationResult's payload. ---#
        return ComputationResult.success(destinations)