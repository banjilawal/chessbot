# src/logic/square/service/operation/build/build.py

"""
Module: logic.square.service.operation.build.build
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""

from __future__ import annotations

from logic.board import Board, BoardService
from logic.coord import Coord, CoordService
from logic.square import Square, SquareBuildException, SquareCollisionAnalysis
from logic.system import (
    Builder, IdFactory, IdentityService, BuildResult, InvariantBreachException, LoggingLevelRouter
)

class SquareBuilder(Builder[Square]):
    """
     Role:
        -   Worker,
        -   Integrity Management

     Responsibilities:
         1.  Produce Square instances whose integrity is guaranteed at creation.
         2.  Ensure params for Square creation have met the application's safety contract.
         3.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    Attributes:

    Provides:
        -   def execute(
                schema: str,
                board: Board,
                coord: Coord,
                id: int = IdFactory,
                board_service: BoardService,
                coord_service: CoordService,
                identity_service: IdentityService,
                square_collision_analyzer: SquareCollisionAnalysis),
            ) -> BuildResult[Square]

     Super Class:
         Builder
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            name: str,
            board: Board,
            coord: Coord,
            id: int = IdFactory.next_id(class_name="Square"),
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            square_collision_analyzer: SquareCollisionAnalysis = SquareCollisionAnalysis(),
    ) -> BuildResult[Square]:
        """
        Action:
            1.  Send an exception chain in the BuildResult if
                    -   Any build param fails does not pass a validation check.
                    -   The square's attributes have already been used on the board.
            2.  Build the Square instance with the params.
            3.  Send an exception chain in the BuildResult if
                    * The square requires insertion into the board but the insertion fails.
            4.  Return the Square instance in the BuildResult.
        Args:
            id: int
            name: str
            coord: Coord
            board: Board
            coord_service: CoordService
            board_service: BoardService
            identity_service: IdentityService
        Returns:
            BuildResult[Square]
            
        Raises:
            SquareBuildException
        """
        method = f"{cls.__class__.__name__}.build"
        
        # Handle the case that, a build param fails does not pass a validation check.
        build_param_validation_result = cls._run_build_param_checks(
            id=id,
            name=name,
            coord=coord,
            board=board,
            board_service=board_service,
            coord_service=coord_service,
            identity_service=identity_service,
            collision_analyzer=square_collision_analyzer,
        )
        if build_param_validation_result.is_failure:
            return build_param_validation_result
        # --- Forward the result of binding the square to the client. ---#
        return cls._bind_square_board(
            board=board,
            board_service=board_service,
            square=Square(id=id, name=name, coord=coord, board=board),
        )
    
    @classmethod
    def _run_build_param_checks(
            cls,
            id: int,
            name: str,
            coord: Coord,
            board: Board,
            board_service: BoardService,
            coord_service: CoordService,
            identity_service: IdentityService,
            collision_analyzer: SquareCollisionAnalysis,
    ) -> BuildResult[Square]:
        """
        Verify that, the square's build params are safe. A BuildResult is returned
        instead of a Validation to avoid visual clutter and let the param_check runner
        handle the result.
        
       Action:
            1.  Send an exception chain in the BuildResult if either:
                    -   id
                    -   schema
                    -   coord
                    -   board
                fails its validation checks.
            2.  Otherwise, send the success result of a null square.
        Args:
            id: int
            name: str
            coord: Coord
            board: Board
            board_service: BoardService
            coord_service: CoordService
            identity_service: IdentityService
            collision_analyzer: SquareCollisionAnalysis
        Returns:
            BuildResult[Square]
        Raises:
            SquareBuildException
        """
        method = f"{cls.__name__}_run_build_param_checks"
        
        # Handle the case that, either id or schema are not certified safe.
        identity_validation = identity_service.validate_identity(
            id_candidate=id,
            name_candidate=name
        )
        if identity_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=SquareBuildException.OP,
                    msg=SquareBuildException.MSG,
                    err_code=SquareBuildException.ERR_CODE,
                    rslt_type=SquareBuildException.RSLT_TYPE,
                    ex=identity_validation.exception,
                )
            )
        # Handle the case that, the coordis not safe.
        coord_validation = coord_service.validator.validate(coord)
        if coord_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=SquareBuildException.OP,
                    msg=SquareBuildException.MSG,
                    err_code=SquareBuildException.ERR_CODE,
                    rslt_type=SquareBuildException.RSLT_TYPE,
                    ex=coord_validation.exception,
                )
            )
        # Handle the case that, the boardis not safe.
        board_validation = board_service.validator.validate(board)
        if board_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=SquareBuildException.OP,
                    msg=SquareBuildException.MSG,
                    err_code=SquareBuildException.ERR_CODE,
                    rslt_type=SquareBuildException.RSLT_TYPE,
                    ex=board_validation.exception,
                )
            )
        # Handle the case that, the square's attributes have already been used.
        collision_detection_result = collision_analyzer.execute(
            id=id,
            name=name,
            coord=coord,
            board=board
        )
        if collision_detection_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=SquareBuildException.OP,
                    msg=SquareBuildException.MSG,
                    err_code=SquareBuildException.ERR_CODE,
                    rslt_type=SquareBuildException.RSLT_TYPE,
                    ex=collision_detection_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(None)
    
    @classmethod
    def _bind_square_board(
            cls,
            board: Board,
            square: Square,
            board_service: BoardService,
    ) -> BuildResult[Square]:
        """
        Establish the bidirectional relationship between the square and its board
        to finalize the build.
        
        Action:
            1.  Send an exception chain in the BuildResult if either:
                    -   The analysis is not completed.
                    -   TThe square and board are not related.
                    -   The board has a stale link to the square.
            2.  If the square has not been registered with the board insert in the board's
                squares.
            3.  Send the success result.
        Args:
            board: Board
            square: Square
            board_service: BoardService
        Returns:
            BuildResult[Square]
        Raises:
            SquareBuildException
        """
        method = f"{cls.__name__}.bind_square_board"
        
        relation_analysis = board_service.square_relation_analyzer.search(
            candidate_primary=board,
            candidate_satellite=square
        )
        # Handle the case that, the relation analysis was not completed.
        if relation_analysis.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=SquareBuildException.OP,
                    msg=SquareBuildException.MSG,
                    err_code=SquareBuildException.ERR_CODE,
                    rslt_type=SquareBuildException.RSLT_TYPE,
                    ex=relation_analysis.exception,
                )
            )
        # Handle the case that, the board and item are not related.
        if relation_analysis.not_related or relation_analysis.stale_link_exists:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=SquareBuildException.OP,
                    msg=SquareBuildException.MSG,
                    err_code=SquareBuildException.ERR_CODE,
                    rslt_type=SquareBuildException.RSLT_TYPE,
                    ex=InvariantBreachException(
                        msg=InvariantBreachException.MSG,
                        err_code=InvariantBreachException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the square has not registered with the board.
        if relation_analysis.not_registered:
            insertion_result = board.squares.insert_square(square=square)
            if insertion_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=SquareBuildException.OP,
                        msg=SquareBuildException.MSG,
                        err_code=SquareBuildException.ERR_CODE,
                        rslt_type=SquareBuildException.RSLT_TYPE,
                        ex=insertion_result.exception,
                    )
                )
        # --- Forward the work product to the client. ---#
        return BuildResult.success(square)