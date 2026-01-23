# src/chess/rank/model/concrete/pawn/compute/opening/span.py

"""
Module: chess.rank.model.concrete.pawn.compute.opening.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List

from chess.vector import Vector
from chess.coord import Coord, CoordService
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import AttackCategory, PawnAttackSpan, PawnOpeningSpanComputationFailedException

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
    ATTACK_CATEGORY = AttackCategory.OPENING
    FORWARD_VECTORS = [Vector(x=0, y=1), Vector(0, y=2)]
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            origin: Coord,
            coord_service: CoordService = CoordService(),
            pawn_attacking_span: PawnAttackSpan = PawnAttackSpan(),
    ) -> ComputationResult[List[Coord]]:
        """
        # Action
            1.  If the origin does not pass its validation checks send an exception chain in the CalculationResult.
            2.  Iterate through the vectors in the attack category to compute the targets. If any of th computations
                fail send an exception in the CalculationResult. Else, the computation was successful. Send it
                IN THE ComputationResult's payload.
        # PARAMETERS:
            *   origin (Coord)
            *   attack_category (AttackCategory)
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
        
        # Get the possible opening destinations.
        destination_computation_result = cls._compute_destinations(
            origin=origin,
            coord_service=coord_service,
        )
        # Handle the case that the destination_computation does not produce a result.
        if destination_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PawnOpeningSpanComputationFailedException(
                    message=f"{method}: {PawnOpeningSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=destination_computation_result.exception
                )
            )
        span = []
        # Compute the attack targets for the two possible destinations.
        for destination in destination_computation_result.payload:
            targeting_computation_result = cls._compute_targets(
                span=span,
                origin=destination,
                pawn_attack_span=pawn_attacking_span,
            )
            if targeting_computation_result.is_failure:
                # On failure return the exception chain
                return ComputationResult.failure(
                    PawnOpeningSpanComputationFailedException(
                        message=f"{method}: {PawnOpeningSpanComputationFailedException.DEFAULT_MESSAGE}",
                        ex=targeting_computation_result.exception
                    )
                )
            span = targeting_computation_result.payload
 
        # --- The targets have been successfully computed. Return in the ComputationResult's payload. ---#
        return ComputationResult.success(span)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _compute_targets(
            cls,
            origin: Coord,
            span:List[Coord],
            pawn_attack_span: PawnAttackSpan = PawnAttackSpan(),
    ) -> ComputationResult[List[Coord]]:
        method = "PawnOpeningSpan._compute_targets"
        
        targeting_computation_result = pawn_attack_span.compute(
            span=span,
            origin=origin,
            coord_service=CoordService(),
        )
        # Handle the case that the computation does not produce a solution.
        if targeting_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PawnOpeningSpanComputationFailedException(
                    message=f"{method}: {PawnOpeningSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=targeting_computation_result.exception
                )
            )
        # --- Return the targets to the caller. ---#
        return targeting_computation_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _compute_destinations(
            cls,
            origin: Coord,
            coord_service: CoordService = CoordService()
    ) -> ComputationResult[List[Coord]]:
        method = "PawnOpeningSpan._compute_destinations"
        
        destinations: List[Coord] = []
        for vector in cls.FORWARD_VECTORS:
            addition_result = coord_service.add_vector_to_coord(coord=origin, vector=vector)
            
            # Handle the case that the computation does not produce a solution.
            if addition_result.is_failure:
                # On failure return the exception chain
                return ComputationResult.failure(
                    PawnOpeningSpanComputationFailedException(
                        message=f"{method}: {PawnOpeningSpanComputationFailedException.DEFAULT_MESSAGE}",
                        ex=addition_result.exception
                    )
                )
            # Otherwise add the coord to the targets.
            if addition_result.payload not in destinations:
                destinations.append(addition_result.payload)
        # --- Return the destinations to the caller. ---#
        return ComputationResult.success(destinations)