# src/chess/rank/model/concrete/pawn/compute/attack/span.py

"""
Module: chess.rank.model.concrete.pawn.compute.attack.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List

from chess.coord import Coord, CoordService
from chess.rank import (
    OpeningPawnVectorSet, PawnAttackSpanComputationRouteException, PawnAttackSpanComputationFailedException
)
from chess.system import ComputationResult, LoggingLevelRouter
from chess.token import PawnToken
from chess.vector import Vector


class PawnAttackSpan:
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
    OPENING_PAWN_VECTOR_SET = OpeningPawnVectorSet()
    DEVELOPED_PAWN_VECTOR_SET = OpeningPawnVectorSet()
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            token: PawnToken,
            coord_service: CoordService = CoordService(),
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
            *   span (List[Coord])
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   PawnAttackSpanComputationFailedException
        """
        method = "PawnAttack.compute"
        
        if token.can_open:
            return cls._span(
                origin=token.current_position,
                coord_service=coord_service,
                attack_vectors=cls.OPENING_PAWN_VECTOR_SET.attack_targeting_vectors
            )
        if token.is_developed:
            return cls._span(
                origin=token.current_position,
                coord_service=coord_service,
                attack_vectors=cls.DEVELOPED_PAWN_VECTOR_SET.attack_targeting_vectors
            )
        
        # On failure return the exception chain
        return ComputationResult.failure(
            PawnAttackSpanComputationFailedException(
                message=f"{method}: {PawnAttackSpanComputationFailedException.DEFAULT_MESSAGE}",
                ex=PawnAttackSpanComputationRouteException(
                    f"{method}: {PawnAttackSpanComputationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )
        
    
    @classmethod
    def _span(
            cls,
            origin: Coord,
            attack_vectors: List[Vector],
            coord_service: CoordService
    ) -> ComputationResult[List[Coord]]:
        method = "PawnAttackSpan._opening_targets"
        
        # Handle the case that the coord is not certified safe.
        coord_validation = coord_service.validator.validate(candidate=origin)
        if coord_validation.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PawnAttackSpanComputationFailedException(
                    message=f"{method}: {PawnAttackSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=coord_validation.exception
                )
            )
        
        targets: List[Coord] = []
        for vector in attack_vectors:
            addition_result = coord_service.add_vector_to_coord(coord=origin, vector=vector)
            
            # Handle the case that vector addition does not produce a result.
            if addition_result.is_failure:
                # On failure return the exception chain
                return ComputationResult.failure(
                    PawnAttackSpanComputationFailedException(
                        message=f"{method}: {PawnAttackSpanComputationFailedException.DEFAULT_MESSAGE}",
                        ex=addition_result.exception
                    )
                )
            # Otherwise add the coord to the targets.
            if addition_result.payload not in targets:
                targets.append(addition_result.payload)
        # --- The targets have been successfully computed. Return in the ComputationResult's payload. ---#
        return ComputationResult.success(targets)