# src/chess/rank/model/concrete/pawn/compute/opening/span.py

"""
Module: chess.rank.model.concrete.pawn.compute.opening.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List

from chess.coord import Coord, CoordService
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import PawnMoveCategory, PawnAttackSpan, PawnOpeningSpanComputationFailedException

class PawnOpeningSpan:
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
    MOVEMENT_CATEGORY = PawnMoveCategory.OPENING_MOVE
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            origin: Coord,
            coord_service: CoordService = CoordService(),
            pawn_attack_span: PawnAttackSpan = PawnAttackSpan(),
    ) -> ComputationResult[List[Coord]]:
        """
        # Action
            1.  If the origin does not pass its validation checks send an exception chain in the CalculationResult.
            2.  Iterate through the vectors in the attack category to compute the targets. If any of th computations
                fail send an exception in the CalculationResult. Else, the computation was successful. Send it
                IN THE ComputationResult's payload.
        # PARAMETERS:
            *   origin (Coord)
            *   attack_category (PawnMoveCategory)
            *   coord_service (CoordService)
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   PawnAttackSpanComputationFailedException
        """
        method = "PawnAttack.compute"
        
        # Handle the case that the coord is not certified safe.
        coord_validation = coord_service.validator.validate(candidate=origin)
        if coord_validation.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PawnOpeningSpanComputationFailedException(
                    message=f"{method}: {PawnOpeningSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=coord_validation.exception
                )
            )
        
        # --- Compute the peaceful destinations ---#
        destinations: List[Coord] = []
        for vector in cls.MOVEMENT_CATEGORY.peaceful_vectors:
            destination_computation = coord_service.add_vector_to_coord(
                coord=origin,
                vector=vector
            )
            # Handle the case that the destination computation does not produce a solution.
            if destination_computation.is_failure:
                # On failure return the exception chain
                return ComputationResult.failure(
                    PawnOpeningSpanComputationFailedException(
                        message=f"{method}: {PawnOpeningSpanComputationFailedException.DEFAULT_MESSAGE}",
                        ex=destination_computation.exception
                    )
                )
            # On success append the solution to the span
            if destination_computation.payload not in destinations:
                destinations.append(destination_computation.payload)
        
        # --- Compute attack targets ---#
        targeting_computation = pawn_attack_span.compute(
            origin=origin,
            coord_service=coord_service,
        )
        # Handle the case that the no solution is produced.
        if targeting_computation.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PawnOpeningSpanComputationFailedException(
                    message=f"{method}: {PawnOpeningSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=targeting_computation.exception
                )
            )
        
        # --- Get the unique points in the destination and attack solutions and send them to the caller. ---#
        span = list(set(destinations + targeting_computation.payload))
        ComputationResult.success(span)