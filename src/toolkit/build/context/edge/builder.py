# src/toolkit/context/edge/toolkit.py

"""
Module: toolkit.context.edge.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from logic.board import Board, BoardService
from logic.coord import Coord, CoordService
from microservice.edge import EdgeState
from system import Toolkit, ToolkitResult, IdentityService
from microservice.edge import (
    EdgeContextToolkitRouteException, ZeroEdgeContextFlagsException, EdgeContext, EdgeContextToolkitException,
    ArenaEdgeContextFlagsException
)
from model.state.token import Token, TokenService


class EdgeContextToolkit(Toolkit[EdgeContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Toolkit Process Owner

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
            ) -> ToolkitResult[Token]

     Super Class:
         Toolkit
     """
    @classmethod
    def __init__(
            self,
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
    ) -> ToolkitResult[EdgeContext]:
        """
        # ACTION:
            1.  If one-and-only-one context attribute is not null send an exception chain in the ToolkitResult.
            2.  If there is no toolkit route for the not-null context attribute send an exception chain in the ToolkitResult.
            3.  If the toolkit route exists and the context attribute is not verified send an exception chain in the
                ToolkitResult. Else toolkit the context and send it in the ToolkitResult's payload.
        # PARAMETERS:
            Only one these must be provided:
                *   id Optional[(int)]
                *   schema Optional[(str)]
                *   cord Optional[(Coord)]
                *   board Optional[(Board)]
                *   state Optional[EdgeState]
            These Parameters must be provided:
                *   board_service (BoardService)
                *   coord_service (CoordService)
                *   token_service (TokenService)
                *   identity_service (IdentityService)
            # RETURNS:
                *   ToolkitResult[EdgeContext] containing either:
                        - On failure: Exception.
                        - On success: EdgeContext in the payload.
            Raises:
                *   ZeroEdgeContextFlagsException
                *   EdgeContextToolkitException
                *   ArenaEdgeContextFlagsException
                *   EdgeContextToolkitRouteException
            """
        method = "EdgeContextToolkit.toolkit"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, name, coord, token,board, state,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                EdgeContextToolkitException(
                    msg=f"{method}: {EdgeContextToolkitException.MSG}",
                    ex=ZeroEdgeContextFlagsException(
                        f"{method}: {ZeroEdgeContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                EdgeContextToolkitException(
                    msg=f"{method}: {EdgeContextToolkitException.MSG}",
                    ex=ArenaEdgeContextFlagsException(
                        f"{method}: {ArenaEdgeContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/toolkit branch. ---#
        
        # Toolkit the id EdgeContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    EdgeContextToolkitException(
                        msg=f"{method}: {EdgeContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_EdgeContext in the ToolkitResult.
            return ToolkitResult.success(EdgeContext(id=id))
        
        # Toolkit the schema EdgeContext if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    EdgeContextToolkitException(
                        msg=f"{method}: {EdgeContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_EdgeContext in the ToolkitResult.
            return ToolkitResult.success(EdgeContext(name=name))
        
        # Toolkit the coord EdgeContext if its flag is enabled.
        if coord is not None:
            validation = coord_service.run.build(coord)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    EdgeContextToolkitException(
                        msg=f"{method}: {EdgeContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a coord_EdgeContext in the ToolkitResult.
            return ToolkitResult.success(EdgeContext(coord=coord))
        
        # Toolkit the board EdgeContext if its flag is enabled.
        if board is not None:
            validation = board_service.run.build(candidate=board)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    EdgeContextToolkitException(
                        msg=f"{method}: {EdgeContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a board_EdgeContext in the ToolkitResult.
            return ToolkitResult.success(EdgeContext(board=board))
        
        # Toolkit the occupant EdgeContext if its flag is enabled.
        if token is not None:
            validation = token_service.run.search_service(candidate=token)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    EdgeContextToolkitException(
                        msg=f"{method}: {EdgeContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a token_EdgeContext in the ToolkitResult.
            return ToolkitResult.success(EdgeContext(occupant=token))
        
        # Toolkit the state EdgeContext if its flag is enabled.
        if state is not None:
            if not isinstance(state, EdgeState):
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    EdgeContextToolkitException(
                        msg=f"{method}: {EdgeContextToolkitException.MSG}",
                        ex=TypeError(
                            f"{method}: Was expecting a EdgeState, got {type(state).__name__} instead."
                        )
                    )
                )
            # On validation success return a token_EdgeContext in the ToolkitResult.
            return ToolkitResult.success(EdgeContext(state=state))
        
        # Return the exception chain if there is no toolkit route for the context.
        return ToolkitResult.failure(
            EdgeContextToolkitException(
                msg=f"{method}: {EdgeContextToolkitException.MSG}",
                ex=EdgeContextToolkitRouteException(f"{method}: {EdgeContextToolkitRouteException.MSG}")
            )
        )