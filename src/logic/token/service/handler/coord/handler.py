# src/logic/token/service/handler/coord/handler.py

"""
Module: logic.token.service.handler.coord.handler
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""
from logic.token.service.handler.coord.exception.anchor import TokenCoordHandlerException

# src/logic/token/service/service.py

"""
Module: logic.token.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.rank import King, Knight, Queen, Rank, RankService, Rook
from logic.rank.model.concrete.bishop import Bishop
from logic.schema import SchemaService
from logic.square import SquareContext
from logic.system import DeletionResult, IntegrityService, InsertionResult, LoggingLevelRouter, UpdateResult, id_emitter
from logic.coord import Coord, CoordService, DuplicateCoordPushException, PoppingEmtpyCoordStackException
from logic.token import (
    PromotionToKingException, NewRankSameAsCurrentRankException, OverMoveUndoLimitException,
    PawnAlreadyPromotedException,
    PromotionException, PawnToken,
    PromotionState, Token, TokenBoardState,
    TokenService, TokenValidator,
    TokenDeploymentException, TokenFactory, TokenHandler, TokenOpeningSquareNotFoundException,
    TokenServiceException,
)

class TokenCoordHandler:
    """
    # ROLE: Update Handler, Consistency, Integrity Maintenance, Lifecycle Management

    # RESPONSIBILITIES:
    1.  Ensure integrity and consistency are maintained during the pawn's promotion lifecycle.

    # PARENT:
    None

    # PROVIDES:
    None

    Attributes:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
    None

    # LOCAL METHODS:

    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def undo_last_coord_push(
            cls,
            token: Token,
            token_validator: TokenValidator = TokenValidator(),
    ) -> DeletionResult[Coord]:
        """
        # ACTION:
            1.  If the token fails validation returns the exception in the DeletionResult.
            2.  If the token has not been activated with an opening item return the exception in the DeletionResult.
            3.  If the token has an empty coord stack return the exception in the DeletionResult.
            4.  If a new coord has not been pushed since the last undo send and exception in the DeletionResult.
                Else, forward the results of token.positions.pop_coord() to the caller.

        Args:
            token: Token
            token_validator: TokenValidator

        Returns:
            DeletionResult[Coord]

        Raises:
            TokenServiceException
            OverMoveUndoLimitException
            TokenOpeningSquareNotFoundException
            PoppingEmtpyCoordStackException
        """
        method = f"{cls.__class__.__name__}undo_last_coord_push"
        
        # Handle the case that, the token is not certified as safe.
        validation_result = token_validator.validate(token)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenCoordHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=TokenCoordHandlerException.MSG,
                    err_code=TokenCoordHandlerException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, token is not active
        if not token.is_active:
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return DeletionResult.failure(
                    TokenCoordHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=TokenCoordHandlerException.MSG,
                        err_code=TokenCoordHandlerException.ERR_CODE,
                        ex=CoordS
                    )
                )
        
        if token.opening_square_name is None:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERR_CODE}",
                    ex=TokenOpeningSquareNotFoundException(
                        f"{method}: {TokenOpeningSquareNotFoundException.MSG}"
                    )
                )
            )
        # Handle the case that, the token has no positions that can be removed.
        if token.positions.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERR_CODE}",
                    ex=PoppingEmtpyCoordStackException(
                        f"{method}: {PoppingEmtpyCoordStackException.MSG}"
                    )
                )
            )
        # Handle the case that, an attempt is made to undo more than one turn.
        if token.previous_coord == token.current_address:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERR_CODE}",
                    ex=OverMoveUndoLimitException(f"{method}: {OverMoveUndoLimitException.MSG}")
                )
            )
        # Handle the case that, the coord stack pop operation fails.
        pop_result = token.positions.pop()
        if token.previous_coord == token.current_address:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERR_CODE}",
                    ex=pop_result.exception
                )
            )
        # Otherwise return the successful pop operation's data to the caller in the DeletionResult.
        return pop_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def push_coord(
            cls,
            token: Token,
            coord: Coord,
            coord_service: CoordService = CoordService(),
            token_validator: TokenValidator = TokenValidator(),

    ) -> InsertionResult:
        """
        Action:
            1.  If the token or coord fail their validations return the exception in the InsertionResult.
            2.  If the position is already the updated position return the exception in the InsertionResult.
            3.  If the pushing the position to the token's coord stack fails encapsulate the exception then
                send the exception chain in the InsertionResult.'

        Args:
            coord: Coord
            token: Token
            coord_service: CoordService
            token_validator: TokenValidator

        Returns:
            DeletionResult[Coord]

        Raises:
            TokenServiceException
            OverMoveUndoLimitException
            TokenOpeningSquareNotFoundException
            PoppingEmtpyCoordStackException
        """
        method = "TokenService.push_coord_to_token"
        
        # Handle the case that, the token is not certified safe.
        token_validation = self.validator.validate(token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenService.ERR_CODE}",
                    ex=token_validation.exception
                )
            )
        # Handle the case that, the position is not certified safe.
        position_validation = coord_service.validate(position)
        if position_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenService.ERR_CODE}",
                    ex=token_validation.exception
                )
            )
        # Handle the case that, the token is already the updated position
        if position == token.current_position:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenServiceException.ERR_CODE}",
                    ex=DuplicateCoordPushException(
                        f"{method}: {DuplicateCoordPushException.MSG}"
                    )
                )
            )
        # Handle the case that, adding the coord to the token's position history fails.
        insertion_result = token.positions.push(item=position)
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenServiceException.ERR_CODE}",
                    ex=insertion_result.exception
                )
            )
        # If the coord was successfully pushed onto the token's coord stack forward insertion result.
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def deploy_on_board(self, token: Token, ) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the token or coord fail their validations return the exception in the InsertionResult.
            2.  If the position is already the updated position return the exception in the InsertionResult.
            3.  If the pushing the position to the token's coord stack fails encapsulate the exception then
                send the exception chain in the InsertionResult's payload.

        # Args:
            token: Token

        Returns:
            InsertionResult

        Raises:
            TokenServiceException
            CoordAlreadyToppingStackException
        """
        method = "TokenService.deploy_on_board"
        
        # Handle the case that, the token is not certified safe.
        token_validation = self.validator.validate(token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenService.ERR_CODE}",
                    ex=TokenDeploymentException(
                        msg=f"{method}: {TokenDeploymentException.ERR_CODE}",
                        ex=token_validation.exception
                    )
                )
            )
        # Handle the case that, the token has already been placed on the board.
        if token.board_state != TokenBoardState.NEVER_BEEN_PLACED:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenService.ERR_CODE}",
                    ex=TokenDeploymentException(
                        msg=f"{method}: {TokenDeploymentException.ERR_CODE}",
                        ex=TokenAlreadyDeployedOnBoardException(f"{method}:")
                    )
                )
            )
        # Find the square where the token gets formed.
        square_search_result = token.team.board.squares.search(
            context=SquareContext(token.opening_square_name)
        )
        # Handle the case that, the search is not completed.
        if square_search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenService.ERR_CODE}",
                    ex=TokenDeploymentException(
                        msg=f"{method}: {TokenDeploymentException.ERR_CODE}",
                        ex=square_search_result.exception
                    )
                )
            )
        # Handle the case the square is not found.
        if square_search_result.is_empty:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenService.ERR_CODE}",
                    ex=TokenDeploymentException(
                        msg=f"{method}: {TokenDeploymentException.ERR_CODE}",
                        ex=TokenOpeningSquareNotFoundException(
                            f"{method}: {TokenOpeningSquareNotFoundException.MSG}"
                        )
                    )
                )
            )
        # --- Run the occupation process on the opening square. ---#
        occupation_result = token.team.board.squares.add_occupant_to_square(
            token=token,
            square=square_search_result.payload[0],
        )
        # Handle the case that, occupying the opening square fails.
        if occupation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenService.ERR_CODE}",
                    ex=TokenDeploymentException(
                        msg=f"{method}: {TokenDeploymentException.ERR_CODE}",
                        ex=occupation_result.exception
                    )
                )
            )
        # --- Assure that token.board_state has been updated. ---#
        if token.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            token.board_state = TokenBoardState.DEPLOYED_ON_BOARD
        
        # Send the success result to the caller.
        return InsertionResult.success()