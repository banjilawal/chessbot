# src/chess/rank/model/concrete/pawn/pawn.py

"""
Module: chess.rank.model.concrete.pawn.pawn
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.token import MoveCategory, PawnToken, TokenService
from chess.vector import Vector
from chess.persona import Persona
from chess.geometry import Quadrant
from chess.coord import Coord, CoordService
from chess.system import ComputationResult, LoggingLevelRouter
from chess.rank import (
    PawnAttackSpan, PawnException, PawnMoveCategory, PeacefulPawnSpan, PawnSpanComputationFailedException, Rank,
    Pawn
)


class Pawn(Rank):
    """
    # ROLE: Computation, Metadata

    # RESPONSIBILITIES:
    1.  Produces a list of Coords reachable from a Pawn's current position.
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
    _attack_span: PawnAttackSpan
    _peaceful_span: PeacefulPawnSpan
    
    def __init__(
            self,
            id: int,
            name: str = Persona.PAWN.name,
            ransom: int = Persona.PAWN.ransom,
            team_quota: int = Persona.PAWN.quota,
            designation: str = Persona.PAWN.designation,
            quadrants: List[Quadrant] = List[Persona.PAWN.quadrants],
            vectors: Optional[List[Vector]] = None,
    ):
        super().__init__(
            id=id,
            name=name,
            ransom=ransom,
            team_quota=team_quota,
            designation=designation,
            quadrants=quadrants,
            vectors=vectors,
        )
        
    
    @LoggingLevelRouter.monitor
    def spanning_set_dictionary(
            self,
            token: PawnToken,
            token_service: TokenService = TokenService(),
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[dict[str, List[Coord]]]:
        """
        
        """
        method = "Pawn.spanning_set_dictionary"
        #
        # # Handle the case that the token is either neither safe nor actionable.
        # actionable_token_verification_result = token_service.verify_token_is_actionable(token=token)
        # if actionable_token_verification_result.is_failure:
        #     # Return the exception chain on failure.
        #     return ComputationResult.failure(
        #         PawnSpanComputationFailedException(
        #             message=f"{method}: {PawnSpanComputationFailedException.DEFAULT_MESSAGE}",
        #             ex=actionable_token_verification_result.exception
        #         )
        #     )
        # Handle the case that the token is not a Pawn
        if not isinstance(token, PawnToken):
            return ComputationResult.failure(
                PawnSpanComputationFailedException(
                    message=f"{method}: {PawnSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(
                        f"{method}: Expected PawnToken, got {type(token).__name__} instead. Cannot "
                        f"compute pawn spanning dictionary for non-Pawn tokens."
                    )
                )
            )
        solution_set: dict[str, List[Coord]] = {}
        # Get the peaceful destinations
        destination_result = self._compute_peaceful_span(token=token)
        
        # Handle the case that the computation does not produce a solution.
        if destination_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PawnException(
                    message=f"{method}: {PawnException.DEFAULT_MESSAGE}",
                    ex=destination_result.exception
                )
            )
        targeting_result = self._compute_attack_span(token=token)
        # Handle the case that the computation does not produce a solution.
        if targeting_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PawnException(
                    message=f"{method}: {PawnException.DEFAULT_MESSAGE}",
                    ex=targeting_result.exception
                )
            )
        
        
        
        
    
    
    @LoggingLevelRouter.monitor
    def _compute_peaceful_span(self, token: PawnToken,) -> ComputationResult[[Coord]]:
        
        if token.can_open:
            return self._peaceful_span.compute(
                origin=token.current_position,
                coord_service=self.coord_service,
                pawn_move_category=PawnMoveCategory.OPENING_MOVE
            )
        return self._peaceful_span.compute(
            origin=token.current_position,
            coord_service=self.coord_service,
            pawn_move_category=PawnMoveCategory.DEVELOPED_MOVE
        )
    
    @LoggingLevelRouter.monitor
    def _compute_attack_span(self, token: PawnToken) -> ComputationResult[[Coord]]:
        if token.can_open:
            return self._attack_span.compute(
                origin=token.current_position,
                coord_service=CoordService(),
                pawn_move_category=PawnMoveCategory.OPENING_MOVE
            )
        return self._attack_span.compute(
            origin=token.current_position,
            coord_service=CoordService(),
            pawn_move_category=PawnMoveCategory.DEVELOPED_MOVE
        )
    
    @LoggingLevelRouter.monitor
    def compute_span(
            self,
            token: PawnToken,
            token_service: TokenService = TokenService(),
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[[Coord]]:
        """
        # Action
            1.  If the origin is not certified safe send an exception chain in the ComputationResult.
            2.  Add origin to each vector in Pawn.vectors to get the spanning set. If any of the
                additions fails send an exception chain in the ComputationResult.
            3.  Send the set of points to the caller in the ComputationReslt's payload.
        # PARAMETERS:
            *   origin (Coord)
            *   coord_service (CoordService)

        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   PawnSpanComputationFailedException
        """
        method = "Pawn.compute_span"
        
        destinations = []
        if token.can_open:
            destination_computation = self._peaceful_span.compute(
                origin=token.current_position,
                coord_service=coord_service,
                pawn_move_category=PawnMoveCategory.OPENING_MOVE
            )
            if destination_computation.is_failure:
                return ComputationResult.failure(
                    PawnSpanComputationFailedException(
                        message=f"{method}: {PawnSpanComputationFailedException.DEFAULT_MESSAGE}",
                        ex=destination_computation.exception
                    )
                )
            targeting_computation =self._attack_span.compute(
                origin=token.current_position,
                coord_service=coord_service,
                pawn_move_category=PawnMoveCategory.OPENING_MOVE
            )
            if destination_computation.is_failure:
                return ComputationResult.failure(
                    PawnSpanComputationFailedException(
                        message=f"{method}: {PawnSpanComputationFailedException.DEFAULT_MESSAGE}",
                        ex=destination_computation.exception
                    )
                )
            span = cast(List, list(set(destination_computation.payload + targeting_computation.payload)))
            ComputationResult.success(span)
            
            
        
        
        # Handle the case that the coord is not certified safe.
        coord_validation = coord_service.validator.validate(candidate=token.current_position)
        if coord_validation.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PawnSpanComputationFailedException(
                    message=f"{method}: {PawnSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=coord_validation.exception
                )
            )
        
        # Iterate through the vectors, adding each one to the origin to get the Pawn's spanning set.
        span: List[Coord] = []
        for vector in self.vectors:
            # Handle the case that the computation does not produce a solution.
            result = coord_service.add_vector_to_coord(coord=origin, vector=vector)
            # Return the exception chain on failure.
            if result.is_failure:
                return ComputationResult.failure(result.exception)
            # Otherwise add the coord to the span.
            if result.payload not in span:
                span.append(result.payload)
        
        # --- The Pawn's span has been successfully computed. Return in the ComputationResult's payload. ---#
        return ComputationResult.success(span)
    
    @LoggingLevelRouter.monitor
    def compute_span(self, piece: PawnPiece) -> [Coord]:
        """
        # Action
        1.  If piece.positions.size() == 1, then we are in an opening move. Call _opening_span.
            Otherwise, call _developed_span.
        2.  Return the list.
    
        # PARAMETERS:
            *   piece (Token): Single-source-of-truth for the basis of the span.
    
        # RETURNS:
        List[Coord]
    
        RAISES:
        None
        """
        method = "Pawn.compute_span"
        
        origin = token.current_position
        if piece.positions.size() == 1:
            return self._opening_span(origin)
        return self._developed_span(origin)
    
@LoggingLevelRouter.monitor
def _compute_developed_span(self, origin: Coord) -> [Coord]:
    """
    # BACKGROUND:
    Any opening moves develop by
        *   Advancing one square_name forward.
        *   Attacking one square_name forward then one diagonal square_name.

    # Action
    1.  Call  by adding a vector of (0,1) to the origin.
    2.  Get the set attackable positions by adding (-1,1), (1,1) to the origin.
    3.  Return the 3 points to the span.

    # PARAMETERS:
        *   origin (Coord):

    # RETURNS:
    List[Coord]

    RAISES:
    None
    """
    method = "Pawn._compute_developed_span"
    return [
        # Forward position
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=0, y=1)),
        # Queen-side attacking position
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=-1, y=1)),
        # King-side attacking position
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=1, y=1))
    ]

@LoggingLevelRouter
def _compute_opening_span(self, origin: Coord) -> [Coord]:
    """
    # BACKGROUND:
    Any opening moves develop by
        *   Advancing either one or two squares forward.
        *   Attacking either one or two squares forward then one diagonal square_name.

    # Action
    1.  Get the opening forward position by adding a vector of (0,2) to the origin.
    2.  Get the set opening attackable positions by adding (-1,2), (1,2) to the origin.
    3.  Call _developed_span to get the remaining opening destinations.
    4.  Return the 6 points to the span.

    # PARAMETERS:
        *   origin (Coord):

    # RETURNS:
    List[Coord]

    RAISES:
    None
    """
    method = "Pawn._compute_opening_span"
    return [
        # Get destination of 2 step advance.
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=0, y=2)),
        # Get 2 step queen-side attack destination.
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=-1, y=2)),
        # Get 2 step king-side attack destination.
        self.coord_service.add_vector_to_coord(coord=origin, vector=Vector(x=1, y=2)),
        # Add points in developed move.
        self._compute_developed_span(origin),
    ]
