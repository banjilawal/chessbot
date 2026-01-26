# src/chess/rank/model/concrete/pawn/compute/attack/span.py

"""
Module: chess.rank.model.concrete.pawn.compute.attack.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List

from chess.vector import Vector
from chess.token import PawnToken
from chess.coord import Coord, CoordService
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import (
    OpeningPawnVectorSet, PawnAttackSpanComputationRouteException, PawnAttackSpanComputationFailedException
)

class PawnAttackSpan:
    """
    # RESPONSIBILITIES:
    1.  Single source of targeting truth for opening and developed pawns.
    2.  If a solution is not provided PawnAttackSpan sends an exception for tracing and solving the
        logic.

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
            1.  If the occupant fails actionable or type tests send an exception chain in the ComputationResult.
            2.  If the pawn is neither opening nor developed send an exception chain in the ComputationResult.
            3.  Give the helper method the pawn's position and vectors it needs to find targets. The helper sends
                result to the caller.
        # PARAMETERS:
            *   occupant (PawnToken):
            *   coord_service (CoordService)
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   PawnAttackSpanComputationFailedException
        """
        method = "PawnAttack.compute"
        
        # If the occupant has not made its first move, call the helper with OPENING_MOVE.targeting_vectors.
        if token.can_open:
            return cls._span_helper(
                origin=token.current_position,
                coord_service=coord_service,
                attack_vectors=cls.OPENING_PAWN_VECTOR_SET.attack_targeting_vectors
            )
        # If the occupant has moved once, call the helper with DEVELOPED_MOVE.targeting vectors.
        if token.is_developed:
            return cls._span_helper(
                origin=token.current_position,
                coord_service=coord_service,
                attack_vectors=cls.DEVELOPED_PAWN_VECTOR_SET.attack_targeting_vectors
            )
        # Return the exception chain if there is no solution route for the any other pawn state,
        return ComputationResult.failure(
            PawnAttackSpanComputationFailedException(
                message=f"{method}: {PawnAttackSpanComputationFailedException.DEFAULT_MESSAGE}",
                ex=PawnAttackSpanComputationRouteException(
                    f"{method}: {PawnAttackSpanComputationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )
    
    @classmethod
    def _span_helper(
            cls,
            origin: Coord,
            attack_vectors: List[Vector],
            coord_service: CoordService
    ) -> ComputationResult[List[Coord]]:
        """
        # Action:
            1.  If the coord is not certified as safe send an exception chain in the ComputationResult.
                Else iterate the through the vectors.
            2.  Add each vector to the origin to get a target coord.
            3.  If the addition fails send an exception chain. Otherwise, add the target coord to the
                targets list if it's not already present.
            4.  After the loop send the target list to the caller in the ComputationResult's payload.'
        """
        method = "PawnAttackSpan._span_helper"
        
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
        # --- Process the vectors ---#
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
            # On computation success add the result to the target list. It should not be present.
            if addition_result.payload not in targets:
                targets.append(addition_result.payload)
                
        # After the loop, put the target inside a ComputationResult and send to the caller.
        return ComputationResult.success(targets)