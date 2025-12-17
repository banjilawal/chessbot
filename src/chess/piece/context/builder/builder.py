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
from chess.coord import Coord, CoordService
from chess.rank import Rank, RankCertifier
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter
from chess.team import Team, TeamCertifier


class PieceContextBuilder(Builder[PieceContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce PieceContext instances whose integrity is always guaranteed.
     2.  Manage construction of PieceContext instances that can be used safely by the client.
     3.  Ensure params for PieceContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
         *  build: -> BuildResult[PieceContext]

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
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
            team_service: TeamCertifier = TeamCertifier(),
            rank_service: RankCertifier = RankCertifier(),
            coord_service: CoordService = CoordService(),
            idservice: IdentityService = IdentityService(),
    ) -> BuildResult[PieceContext]:
        """
        # Action:
            1. Confirm that only one in the tuple (id, designation, coord), is not null.
            2. Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3. If all checks pass build the PieceContext in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   designation (Optional[int])
            *   team (Optional[Team])
            *   rank (Optional[Rank])
            *   ransom (Optional[int])
            *   coord (Optional[Coord])
            
        These Parameters must be provided:
            *   team_certifier (TeamCertifier)
            *   rank_certifier (RankCertifier)
            *   coord_service (CoordService)
            *   identity_service (IdentityService)

        # Returns:
          BuildResult[PieceContext] containing either:
                - On success: PieceContext in the payload.
                - On failure: Exception.

        # Raises:
            *   PieceContextBuildFailedException
            *   NoPieceContextFlagSetException
            *   TooManyPieceContextFlagsSetException
        """
        method = "PieceContextBuilder.builder"
        
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
                validation = idservice.validate_id(id)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(PieceContext(id=id))
            
            if name is not None:
                validation = idservice.validate_name(name)
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