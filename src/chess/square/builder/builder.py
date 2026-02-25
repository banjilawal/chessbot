# src/chess/square/builder/builder.py

"""
Module: chess.square.builder.builder
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.board import Board, BoardService
from chess.coord import Coord, CoordService
from chess.square import (
    AddingDuplicateSquareException, Square, SquareBuildException, SquareCollisionDetector, SquareContext,
    SquareCoordCollisionException,
    SquareIdCollisionException, SquareNameCollisionException
)
from chess.system import (
    Builder, BuildResult, IdFactory, IdentityService, InsertionResult, InvariantBreachException, LoggingLevelRouter,
    ValidationResult,
)

class SquareBuilder(Builder[Square]):
    """
     # ROLE: Builder, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce Square instances whose integrity and reliability are guaranteed.
     2.  Ensure params for Square creation have met the application's safety contract.
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
                name: str,
                board: Board,
                coord: Coord,
                id: int = IdFactory.next_id(Square.__name__),
                board_service: BoardService = BoardService(),
                coord_service: CoordService = CoordService(),
                identity_service: IdentityService = IdentityService(),
            ) -> BuildResult[Square]

    # INHERITED METHODS:
    None
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
            square_collision_detector: SquareCollisionDetector = SquareCollisionDetector(),
    ) -> BuildResult[Square]:
        """
        # ACTION:
            1.  Send an exception chain in the BuildResult if
                    * Any build param fails is not certified as safe.
                    * The square's attributes have already been used on the board.
            2.  Build the Square instance with the params.
            3.  Send an exception chain in the BuildResult if
                    * The square requires insertion into the board but the insertion fails.
            4.  Return the Square instance in the BuildResult.
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   cord (Coord)
            *   board (Board)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
            *   SquareBuildException
        """
        method = "SquareBuilder.builder"
        
        # Handle the case that, a build param fails is not certified as safe.
        build_params_validation_result = cls._validate_build_params(
            id=id,
            name=name,
            coord=coord,
            board=board,
            board_service=board_service,
            coord_service=coord_service,
            identity_service=identity_service,
        )
        if build_params_validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildException(
                    msg=f"{method}: {SquareBuildException.MSG}",
                    ex=build_params_validation_result.exception
                )
            )
        # Handle the case that, the square's attributes have already been used.
        collision_detection_result = square_collision_detector.detect_attribute_collisions(
            id=id,
            name=name,
            coord=coord,
            board=board
        )
        if collision_detection_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildException(
                    msg=f"{method}: {SquareBuildException.MSG}",
                    ex=collision_detection_result.exception
                )
            )
        # --- Create the Square. ---#
        square = Square(id=id, name=name, coord=coord, board=board)
        
        # Ensure the square and board have a bidirectional relationship by handling insertion.
        insertion_result = cls._build_square_board_relationship(
            square=square,
            board=board,
            board_service=board_service
        )
        # Handle the case that, the insertion was not successful.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildException(
                    msg=f"{method}: {SquareBuildException.MSG}",
                    ex=insertion_result.exception
                )
            )
        # --- Send the success result to the client. ---#
        return BuildResult.success(square)
    
    @classmethod
    def _validate_build_params(
            cls,
            id: int,
            name: str,
            coord: Coord,
            board: Board,
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[int]:
        """
        # ACTION:
            1.  If either the id, name, coord, or board are is not certified as safe by their validators, return the
                validation exception to the caller. Otherwise, return the number of attributes in the success result.
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   cord (Coord)
            *   board (Board)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[int] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
        None
        """
        method = "SquareBuilder._validate_build_params"
        
        # Handle the case that, either id or name are not certified safe.
        identity_validation = identity_service.validate_identity(
            id_candidate=id,
            name_candidate=name
        )
        if identity_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(identity_validation.exception)
        
        # Handle the case that, the coord is not certified safe.
        coord_validation = coord_service.validator.validate(coord)
        if coord_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(coord_validation.exception)
        
        # Handle the case that, the board is not certified safe.
        board_validation = board_service.validator.validate(board)
        if board_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(board_validation.exception)
    
        # --- Send the success result indicating no attribute conditions. ---#
        return ValidationResult.success(3)
    
    @classmethod
    def _build_square_board_relationship(
            cls,
            square: Square,
            board: Board,
            board_service: BoardService,
    ) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  Conduct an analysis to find out if the square and board have a bidirectional relationship with
                each other. If the relation_analyzer aborts return the exception in the InsertionResult.
            2.  If the analysis reveals:
                    *   There is no relation between them, send the failure result.
                    *   They have a bidirectional relation, send the success result.
                    *   The square has not registered with the board use board_service for a square insertion.
                        return the service operation's result.
       # PARAMETERS:
            *   square (Square)
            *   board (Board)
            *   board_service (BoardService)
        # RETURNS:
            *   InsertionResult[bool] containing either:
                    - On failure: Exception.
                    - On success: bool.
        # RAISES:
        None
        """
        method = "SquareBuilder._build_square_board_relationship"
        
        # If the item does not have  a fully bidirectional relationship with the board process the registration.
        relation_analysis = board_service.square_relation_analyzer.analyze(
            candidate_primary=board,
            candidate_satellite=square
        )
        # Handle the case that, the relation analysis was not completed.
        if relation_analysis.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(relation_analysis.exception)
        
        # Handle the case that, the board and item are not related.
        if relation_analysis.not_related:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                InvariantBreachException(msg=f"{method}:{InvariantBreachException.MSG}", )
            )
        
        # Handle the case that, the board and item are have a fully bidirectional relationship.
        if relation_analysis.is_bidirectional:
            # Return the exception chain on failure.
            return InsertionResult.success()
        
        # --- Last relationship state is a partial binding. This is the only case for registering the Square ---#
        
        # Handle the case that, the insertion fails.
        insertion_result = board.squares.insert_square(square=square)
        if insertion_result.is_failure:
            # On failure return the exception.
            return InsertionResult.failure(insertion_result.exception)
        
        # --- On insertion success extract the insertion payload and send in the BuildResult. ---#
        return BuildResult.success(cast(Square, insertion_result.payload))