# src/chess/piece/context/builder/builder.py

"""
Module: chess.piece.context.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.piece import (
    NoPieceContextFlagSetException, PieceContext, PieceContextBuildFailedException,
    TooManyPieceContextFlagsSetException
)
from chess.coord import Coord, CoordIntegrityService
from chess.rank import Rank, RankIntegrityService
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter
from chess.team import Team, TeamIntegrityService


class PieceContextBuilder(Builder[PieceContext]):
    """
    # ROLE: Builder

    # RESPONSIBILITIES:
        1. Produce only PieceContext instances that are safe and reliable.
        2. Ensure params for PieceContext have correctness.

    # PROVIDES:
      BuildResult[PieceContext] containing either:
            - On success: PieceContext in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            rank: Optional[Rank] = None,
            ransom: Optional[int] = None,
            coord: Optional[Coord] = None,
            team_service: TeamIntegrityService = TeamIntegrityService(),
            rank_service: RankIntegrityService = RankIntegrityService(),
            coord_service: CoordIntegrityService = CoordIntegrityService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[PieceContext]:
        """
        # Action:
            1. Confirm that only one in the tuple (id, name, coord), is not null.
            2. Certify the not-null attribute is safe using the appropriate service and validator.
            3. If all checks pass build the PieceContext in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   name (Optional[int])
            *   team (Optional[Team])
            *   rank (Optional[Rank])
            *   ransom (Optional[int])
            *   coord (Optional[Coord])
            
        These Parameters must be provided:
            *   team_integrity (TeamIntegrityService)
            *   rank_integrity (RankIntegrityService)
            *   coord_service (CoordIntegrityService)
            *   identity_service (IdentityService)

        # Returns:
          BuildResult[CoordContext] containing either:
                - On success: CoordContext in the payload.
                - On failure: Exception.

        # Raises:
            *   PieceContextBuildFailedException
            *   NoPieceContextFlagSetException
            *   TooManyPieceContextFlagsSetException
        """
        method = "PieceSearchContextBuilder.builder"
        
        try:
            params = [id, name, team, rank, ransom, coord]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoPieceContextFlagSetException(
                        f"{method}: "
                        f"{NoPieceContextFlagSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    TooManyPieceContextFlagsSetException(
                        f"{method}: "
                        f"{TooManyPieceContextFlagsSetException}"
                    )
                )
            
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(PieceContext(id=id))
            
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(PieceContext(name=name))
            
            if coord is not None:
                validation = coord_service.item_validator.validate(coord)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(PieceContext(coord=coord))
            
            if rank is not None:
                validation = rank_service.item_validator.validate(rank)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(PieceContext(rank=rank))
            
            if team is not None:
                validation = team_service.item_validator.validate(team)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(PieceContext(team=team))
            
            if ransom is not None:
                validation = rank_service.item_validator.validate_ransom_in_bounds(ransom)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(PieceContext(ransom=ransom))
        
        except Exception as ex:
            return BuildResult.failure(
                PieceContextBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceContextBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )