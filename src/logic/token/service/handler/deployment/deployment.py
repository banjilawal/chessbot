# src/logic/token/service/handler/deployment/deployer.py

"""
Module: logic.token.service.handler.deployment.deployer
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from copy import deepcopy

from logic.edge import UpdatingEdgeWeightException
from logic.schema import SchemaService
from logic.rank import King, Pawn, Rank, RankService
from logic.system import LoggingLevelRouter, UpdateResult, ValidationResult
from logic.token import (
    PawnDeploymentRowException, PromoteInactivePawnException, PromoteToPawnException, DeploymentState,
    DeploymentToKingException, PawnAlreadyPromotedException, PawnPromoterException, DeploymentException,
    PawnToken, TokenAlreadyDeployedException, TokenValidator,
)

from __future__ import annotations
from typing import cast

from logic.rank import King, Knight, Queen, Rank, RankService, Rook
from logic.rank.model.concrete.bishop import Bishop
from logic.schema import SchemaService
from logic.square import SquareContext
from logic.system import DeletionResult, IntegrityService, InsertionResult, LoggingLevelRouter, UpdateResult, id_emitter
from logic.coord import Coord, CoordService, PushingDuplicateCoordException, PoppingEmtpyCoordStackException, coord
from logic.token import (
    PromotionToKingException, NewRankSameAsCurrentRankException, OverMoveUndoLimitException,
    PawnAlreadyPromotedException,
    PromotionException, PawnToken,
    PromotionState, Token, TokenBoardState,
    TokenValidator,
    TokenDeploymentException, TokenFactory, TokenHandler, TokenOpeningSquareNotFoundException,
    TokenServiceException,
)


class TokenDeployment:
    """
    # ROLE: Update Handler, Consistency, Integrity Maintenance, Lifecycle Management

    # RESPONSIBILITIES:
    1.  Ensure integrity and consistency are maintained during the pawn's deployment lifecycle.

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
    def execute(
            cls,
            token: Token,
            token_validator: TokenValidator,
    ) -> UpdateResult[Token]:
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
        method = f"{cls.__class__.__name__}.deploy_on_board"
        
        # Handle the case that, the token is not certified safe.
        token_validation = token_validator.validate(token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=token_validation.exception,
                )
            )
        # Handle the case that, the token has already been deployed.
        if token.is_deployed:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=TokenAlreadyDeployedException(
                        msg=TokenDeploymentException.MSG,
                        err_code=TokenDeploymentException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the token has already been deployed.
        if token.is_deployed:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=TokenAlreadyDeployedException(
                        msg=TokenDeploymentException.MSG,
                        err_code=TokenDeploymentException.ERR_CODE,
                    ),
                )
            )
        board = token.team.board
        opening_square_search_result = board.squares.search(
            context=SquareContext(name=token.opening_square_name)
        )
        # Handle the case that, the search fails.
        if opening_square_search_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=opening_square_search_result.exception,
                )
            )
        # Handle the case that, the token's square is not found.
        if opening_square_search_result.is_empty:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenDeploymentException(
                    mthd=method,
                    op=TokenDeploymentException.OP,
                    msg=TokenDeploymentException.MSG,
                    err_code=TokenDeploymentException.ERR_CODE,
                    rslt_type=TokenDeploymentException.RSLT_TYPE,
                    ex=opening_square_search_result.exception,
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