# src/integrity/build/context/linegeo/builder.py

"""
Module: integrity.build.context.linegeo.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from integrity import Builder
from model import LinGeoContext


class LinGeoContextBuilder(Builder[LinGeoContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Token]

     Super Class:
         Builder
     """
    @classmethod
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            coord: Optional[Coord] = None,
            board: Optional[Board] = None,
            token: Optional[Token] = None,
            state: Optional[LinegeoState] = None,
            token_service: TokenService = TokenService(),
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[LinGeoContext]:
        """
        # ACTION:
            1.  If one-and-only-one context attribute is not null send an exception chain in the BuildResult.
            2.  If there is no build route for the not-null context attribute send an exception chain in the BuildResult.
            3.  If the build route exists and the context attribute is not verified send an exception chain in the
                BuildResult. Else build the context and send it in the BuildResult's payload.
        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   schema Optional[(str)]
                *   cord Optional[(Coord)]
                *   board Optional[(Board)]
                *   state Optional[LinegeoState]
            These Parameters must be provided:
                *   board_service (BoardService)
                *   coord_service (CoordService)
                *   token_service (TokenService)
                *   identity_service (IdentityService)
            # RETURNS:
                *   BuildResult[LinGeoContext] containing either:
                        - On failure: Exception.
                        - On success: LinGeoContext in the payload.
            Raises:
                *   ZeroLinGeoContextFlagsException
                *   LinGeoContextBuildException
                *   ArenaLinGeoContextFlagsException
                *   LinGeoContextBuildRouteException
            """
        method = "LinGeoContextBuilder.build"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, name, coord, token,board, state,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                LinGeoContextBuildException(
                    msg=f"{method}: {LinGeoContextBuildException.MSG}",
                    ex=ZeroLinGeoContextFlagsException(
                        f"{method}: {ZeroLinGeoContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                LinGeoContextBuildException(
                    msg=f"{method}: {LinGeoContextBuildException.MSG}",
                    ex=ArenaLinGeoContextFlagsException(
                        f"{method}: {ArenaLinGeoContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the id LinGeoContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    LinGeoContextBuildException(
                        msg=f"{method}: {LinGeoContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_LinGeoContext in the BuildResult.
            return BuildResult.success(LinGeoContext(id=id))
        
        # Build the schema LinGeoContext if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    LinGeoContextBuildException(
                        msg=f"{method}: {LinGeoContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_LinGeoContext in the BuildResult.
            return BuildResult.success(LinGeoContext(name=name))
        
        # Build the coord LinGeoContext if its flag is enabled.
        if coord is not None:
            validation = coord_service.validator.validate(coord)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    LinGeoContextBuildException(
                        msg=f"{method}: {LinGeoContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a coord_LinGeoContext in the BuildResult.
            return BuildResult.success(LinGeoContext(coord=coord))
        
        # Build the board LinGeoContext if its flag is enabled.
        if board is not None:
            validation = board_service.validator.validate(candidate=board)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    LinGeoContextBuildException(
                        msg=f"{method}: {LinGeoContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a board_LinGeoContext in the BuildResult.
            return BuildResult.success(LinGeoContext(board=board))
        
        # Build the occupant LinGeoContext if its flag is enabled.
        if token is not None:
            validation = token_service.validator.search_service(candidate=token)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    LinGeoContextBuildException(
                        msg=f"{method}: {LinGeoContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a token_LinGeoContext in the BuildResult.
            return BuildResult.success(LinGeoContext(occupant=token))
        
        # Build the state LinGeoContext if its flag is enabled.
        if state is not None:
            if not isinstance(state, LinegeoState):
                # Return the exception chain on failure.
                return BuildResult.failure(
                    LinGeoContextBuildException(
                        msg=f"{method}: {LinGeoContextBuildException.MSG}",
                        ex=TypeError(
                            f"{method}: Was expecting a LinegeoState, got {type(state).__name__} instead."
                        )
                    )
                )
            # On validation success return a token_LinGeoContext in the BuildResult.
            return BuildResult.success(LinGeoContext(state=state))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            LinGeoContextBuildException(
                msg=f"{method}: {LinGeoContextBuildException.MSG}",
                ex=LinGeoContextBuildRouteException(f"{method}: {LinGeoContextBuildRouteException.MSG}")
            )
        )