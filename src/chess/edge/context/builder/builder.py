# src/chess/edge/context/builder/builder.py

"""
Module: chess.edge.context.builder.builder
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from chess.board import Board, BoardService
from chess.coord import Coord, CoordService
from chess.edge.state import EdgeState
from chess.system import Builder, BuildResult, IdentityService
from chess.edge import (
    EdgeContextBuildRouteException, ZeroEdgeContextFlagsException, EdgeContext, EdgeContextBuildException,
    ExcessiveEdgeContextFlagsException
)
from chess.token import Token, TokenService


class EdgeContextBuilder(Builder[EdgeContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce EdgeContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of EdgeContext instances that can be used safely by the client.
    3.  Ensure params for EdgeContext creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            coord: Optional[Coord] = None,
            board: Optional[Board] = None,
            token: Optional[Token] = None,
            state: Optional[EdgeState] = None,
            token_service: TokenService = TokenService(),
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[EdgeContext]:
        """
        # ACTION:
            1.  If one-and-only-one context attribute is not null send an exception chain in the BuildResult.
            2.  If there is no build route for the not-null context attribute send an exception chain in the BuildResult.
            3.  If the build route exists and the context attribute is not verified send an exception chain in the
                BuildResult. Else build the context and send it in the BuildResult's payload.
        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   name Optional[(str)]
                *   cord Optional[(Coord)]
                *   board Optional[(Board)]
                *   state Optional[EdgeState]
            These Parameters must be provided:
                *   board_service (BoardService)
                *   coord_service (CoordService)
                *   token_service (TokenService)
                *   identity_service (IdentityService)
            # RETURNS:
                *   BuildResult[EdgeContext] containing either:
                        - On failure: Exception.
                        - On success: EdgeContext in the payload.
            # RAISES:
                *   ZeroEdgeContextFlagsException
                *   EdgeContextBuildException
                *   ExcessiveEdgeContextFlagsException
                *   EdgeContextBuildRouteException
            """
        method = "EdgeContextBuilder.build"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, name, coord, token,board, state,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                EdgeContextBuildException(
                    message=f"{method}: {EdgeContextBuildException.DEFAULT_MESSAGE}",
                    ex=ZeroEdgeContextFlagsException(
                        f"{method}: {ZeroEdgeContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                EdgeContextBuildException(
                    message=f"{method}: {EdgeContextBuildException.DEFAULT_MESSAGE}",
                    ex=ExcessiveEdgeContextFlagsException(
                        f"{method}: {ExcessiveEdgeContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the id EdgeContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextBuildException(
                        message=f"{method}: {EdgeContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_EdgeContext in the BuildResult.
            return BuildResult.success(EdgeContext(id=id))
        
        # Build the name EdgeContext if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextBuildException(
                        message=f"{method}: {EdgeContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_EdgeContext in the BuildResult.
            return BuildResult.success(EdgeContext(name=name))
        
        # Build the coord EdgeContext if its flag is enabled.
        if coord is not None:
            validation = coord_service.validator.validate(coord)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextBuildException(
                        message=f"{method}: {EdgeContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a coord_EdgeContext in the BuildResult.
            return BuildResult.success(EdgeContext(coord=coord))
        
        # Build the board EdgeContext if its flag is enabled.
        if board is not None:
            validation = board_service.validator.validate(candidate=board)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextBuildException(
                        message=f"{method}: {EdgeContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a board_EdgeContext in the BuildResult.
            return BuildResult.success(EdgeContext(board=board))
        
        # Build the occupant EdgeContext if its flag is enabled.
        if token is not None:
            validation = token_service.validator.validate(candidate=token)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextBuildException(
                        message=f"{method}: {EdgeContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a token_EdgeContext in the BuildResult.
            return BuildResult.success(EdgeContext(occupant=token))
        
        # Build the state EdgeContext if its flag is enabled.
        if state is not None:
            if not isinstance(state, EdgeState):
                # Return the exception chain on failure.
                return BuildResult.failure(
                    EdgeContextBuildException(
                        message=f"{method}: {EdgeContextBuildException.DEFAULT_MESSAGE}",
                        ex=TypeError(
                            f"{method}: Was expecting a EdgeState, got {type(state).__name__} instead."
                        )
                    )
                )
            # On validation success return a token_EdgeContext in the BuildResult.
            return BuildResult.success(EdgeContext(state=state))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            EdgeContextBuildException(
                message=f"{method}: {EdgeContextBuildException.DEFAULT_MESSAGE}",
                ex=EdgeContextBuildRouteException(f"{method}: {EdgeContextBuildRouteException.DEFAULT_MESSAGE}")
            )
        )