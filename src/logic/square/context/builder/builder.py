# src/logic/square/context/builder/builder.py

"""
Module: logic.square.context.builder.builder
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from logic.board import Board, BoardService
from logic.coord import Coord, CoordService
from logic.system import Builder, BuildResult, IdentityService
from logic.square import (
    SquareContextBuildRouteException, SquareState, SquareValidator, ZeroSquareContextFlagsException, SquareContext,
    SquareContextBuildException, ExcessSquareContextFlagsException
)
from logic.token import Token, TokenService


class SquareContextBuilder(Builder[SquareContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
     1.  Produce SquareContext instances whose integrity and reliability are guaranteed.
     2.  Ensure params for SquareContext creation have met the application's safety contract.
     3.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
    None

    # LOCAL METHODS:
        *   build(
                cls,
                id: Optional[int] = None,
                name: Optional[str] = None,
                coord: Optional[Coord] = None,
                board: Optional[Board] = None,
                token: Optional[Token] = None,
                state: Optional[SquareState] = None,
                token_service: TokenService = TokenService(),
                board_service: BoardService = BoardService(),
                coord_service: CoordService = CoordService(),
                identity_service: IdentityService = IdentityService(),
            ) -> BuildResult[SquareContext]:

    # INHERITED METHODS:
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
            state: Optional[SquareState] = None,
            token_service: TokenService = TokenService(),
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> BuildResult[SquareContext]:
        """
        # ACTION:
            1.  If the candidate fails either
                    *   A null check.
                    *   A type check.
                Send an exception chain in the ValidationResult. Else, cast candidate to SquareContext
                instance context.
            2.  Send an exception chain in the BuildResult if either
                    *   One and only one of attributes is not null.
                    *   There is no build route for the enabled option.
                    *   The enabled attribute is not certified as safe by its service.
                are is not certified as safe by their services.
            3.  Build the appropriate context, sed the build success result.
            
        Args:
            id: Optional[int]
            name: Optional[str]
            coord: Optional[Coord]
            board: Optional[Board]
            token: Optional[Token]
            state: Optional[SquareState]
            board_service: BoardService
            coord_service: CoordService
            token_service: TokenService
            identity_service: IdentityService
            
        Returns:
            BuildResult[SquareContext]
            
        Raises:
            SquareContextBuildException
            ZeroSquareContextFlagsException
            ExcessSquareContextFlagsException
            SquareContextBuildRouteException
        """
        method = "SquareContextBuilder.build"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, name, coord, token,board, state,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareContextBuildException(
                    msg=f"{method}: {SquareContextBuildException.MSG}",
                    ex=ZeroSquareContextFlagsException(
                        f"{method}: {ZeroSquareContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareContextBuildException(
                    msg=f"{method}: {SquareContextBuildException.MSG}",
                    ex=ExcessSquareContextFlagsException(
                        f"{method}: {ExcessSquareContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the id SquareContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareContextBuildException(
                        msg=f"{method}: {SquareContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_SquareContext in the BuildResult.
            return BuildResult.success(SquareContext(id=id))
        
        # Build the name SquareContext if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareContextBuildException(
                        msg=f"{method}: {SquareContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_SquareContext in the BuildResult.
            return BuildResult.success(SquareContext(name=name))
        
        # Build the coord SquareContext if its flag is enabled.
        if coord is not None:
            validation = coord_service.validator.validate(coord)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareContextBuildException(
                        msg=f"{method}: {SquareContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a coord_SquareContext in the BuildResult.
            return BuildResult.success(SquareContext(coord=coord))
        
        # Build the board SquareContext if its flag is enabled.
        if board is not None:
            validation = board_service.validator.validate(candidate=board)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareContextBuildException(
                        msg=f"{method}: {SquareContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a board_SquareContext in the BuildResult.
            return BuildResult.success(SquareContext(board=board))
        
        # Build the state SquareContext if its flag is enabled.
        if token is not None:
            validation = square_validator.validate_square_state(candidate=state)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareContextBuildException(
                        msg=f"{method}: {SquareContextBuildException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a state_SquareContext in the BuildResult.
            return BuildResult.success(SquareContext(state=state))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            SquareContextBuildException(
                msg=f"{method}: {SquareContextBuildException.MSG}",
                ex=SquareContextBuildRouteException(f"{method}: {SquareContextBuildRouteException.MSG}")
            )
        )