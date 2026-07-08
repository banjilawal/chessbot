# src/toolkit/context/square/toolkit.py

"""
Module: toolkit.context.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class SquareContextToolkit(Toolkit[SquareContext]):
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
            state: Optional[SquareState] = None,
            token_service: TokenService = TokenService(),
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> ToolkitResult[SquareContext]:
        """
        # ACTION:
            1.  If the rank fails either
                    *   A null check.
                    *   A type check.
                Send an exception chain in the ValidationResult. Else, cast rank to SquareContext
                instance context.
            2.  Send an exception chain in the ToolkitResult if either
                    *   One and only one of attributes is not null.
                    *   There is no toolkit route for the enabled option.
                    *   The enabled attribute does not pass a validation check. by its service.
                are does not pass a validation check. by their services.
            3.  Toolkit the appropriate context, sed the toolkit success result.
            
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
            ToolkitResult[SquareContext]
            
        Raises:
            SquareContextToolkitException
            ZeroSquareContextFlagsException
            ExcessSquareContextFlagsException
            SquareContextToolkitRouteException
        """
        method = "SquareContextToolkit.toolkit"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [id, name, coord, token,board, state,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                SquareContextToolkitException(
                    msg=f"{method}: {SquareContextToolkitException.MSG}",
                    ex=ZeroSquareContextFlagsException(
                        f"{method}: {ZeroSquareContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                SquareContextToolkitException(
                    msg=f"{method}: {SquareContextToolkitException.MSG}",
                    ex=ExcessSquareContextFlagsException(
                        f"{method}: {ExcessSquareContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/toolkit branch. ---#
        
        # Toolkit the id SquareContext if its flag is enabled.
        if id is not None:
            validation = identity_service.validate_id(candidate=id)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    SquareContextToolkitException(
                        msg=f"{method}: {SquareContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_SquareContext in the ToolkitResult.
            return ToolkitResult.success(SquareContext(id=id))
        
        # Toolkit the schema SquareContext if its flag is enabled.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    SquareContextToolkitException(
                        msg=f"{method}: {SquareContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_SquareContext in the ToolkitResult.
            return ToolkitResult.success(SquareContext(name=name))
        
        # Toolkit the coord SquareContext if its flag is enabled.
        if coord is not None:
            validation = coord_service.run.build(coord)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    SquareContextToolkitException(
                        msg=f"{method}: {SquareContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a coord_SquareContext in the ToolkitResult.
            return ToolkitResult.success(SquareContext(coord=coord))
        
        # Toolkit the board SquareContext if its flag is enabled.
        if board is not None:
            validation = board_service.run.build(candidate=board)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    SquareContextToolkitException(
                        msg=f"{method}: {SquareContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a board_SquareContext in the ToolkitResult.
            return ToolkitResult.success(SquareContext(board=board))
        
        # Toolkit the state SquareContext if its flag is enabled.
        if token is not None:
            validation = square_validator.execute_square_state(candidate=state)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    SquareContextToolkitException(
                        msg=f"{method}: {SquareContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a state_SquareContext in the ToolkitResult.
            return ToolkitResult.success(SquareContext(state=state))
        
        # Return the exception chain if there is no toolkit route for the context.
        return ToolkitResult.failure(
            SquareContextToolkitException(
                msg=f"{method}: {SquareContextToolkitException.MSG}",
                ex=SquareContextToolkitRouteException(f"{method}: {SquareContextToolkitRouteException.MSG}")
            )
        )