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


class TokenService(IntegrityService[Token]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer, Computation, Transformer,.

    # LOCAL RESPONSIBILITIES:
    
    # INHERITED RESPONSIBILITIES:
        *   See IntegrityService class for inherited responsibilities.

    # PARENT:
        *   IntegrityService

    # PROVIDES:
    None

    Attributes:
        SERVICE_NAME: str
        collision_detector: TokenCollisionDetector
        handler: TokenHandler

    # INHERITED ATTRIBUTES:
        *   See IntegrityService class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   id (int)
        *   name (str)
        *   builder (TokenBuilder) = TokenBuilder()
        *   validator (TokenValidator) = TokenValidator()
        *   collision_detector: TokenCollisionDetector = TokenCollisionDetector(),
        *   handler: TokenHandler = TokenHandler(),

    Methods:
        push_coord_to_token(token: Token, position: Coord, coord_service: CoordService) -> InsertionResult:
            
        *   promote_pawn(
                    self,
                    pawn: PawnToken,
                    new_rank: Rank,
                    rank_service: RankService = RankService()
            ) -> UpdateResult[PawnToken]:
            
        *   deploy_on_board(self,token: Token) -> InsertionResult[bool]:
        *   pop_coord_from_token(self, token) -> DeletionResult[Coord]:

    # INHERITED METHODS:
        *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "TokenService"
    _handler: TokenHandler
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            handler: TokenHandler = TokenHandler(),
            builder: TokenFactory = TokenFactory(),
            validator: TokenValidator = TokenValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._handler = handler
    
    @property
    def builder(self) -> TokenFactory:
        """get TokenFactory"""
        return cast(TokenFactory, self.entity_builder)
    
    @property
    def validator(self) -> TokenValidator:
        """get TokenValidator"""
        return cast(TokenValidator, self.entity_validator)
    
    @property
    def handler(self) -> TokenHandler:
        return self._handler
    
    @LoggingLevelRouter.monitor
    def pop_coord_from_token(self, token) -> DeletionResult[Coord]:
        """
        # ACTION:
            1.  If the token fails validation returns the exception in the DeletionResult.
            2.  If the token has not been activated with an opening item return the exception in the DeletionResult.
            3.  If the token has an empty coord stack return the exception in the DeletionResult.
            4.  If a new coord has not been pushed since the last undo send and exception in the DeletionResult.
                Else, forward the results of token.positions.pop_coord() to the caller.
                
        Args:
            token: Token
            
        Returns:
            DeletionResult[Coord]
            
        Raises:
            TokenServiceException
            OverMoveUndoLimitException
            TokenOpeningSquareNotFoundException
            PoppingEmtpyCoordStackException
        """
        method = f"{self.__class__.__name__}.pop_coord_from_token"
        
        popping_coord_result = self._handler.coord.undo_current_token_positon(
            token=token,
            token_validator=self.validator,
        )
        # Handle the case that, the pop was not completed.
        if popping_coord_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceException.MSG,
                    err_code=TokenServiceException.ERR_CODE,
                    ex=popping_coord_result.exception,
                )
            )
        return popping_coord_result
    
    @LoggingLevelRouter.monitor
    def push_coord_to_token(
            self,
            token: Token,
            coord: Coord,
            coord_service: CoordService = CoordService()
    ) -> InsertionResult:
        """
        Action:
            1.  If the token or coord fail their validations return the exception in the InsertionResult.
            2.  If the position is already the updated position return the exception in the InsertionResult.
            3.  If the pushing the position to the token's coord stack fails encapsulate the exception then
                send the exception chain in the InsertionResult.'
        Args:
            token: Token
            coord: Coord
            coord_service: CoordService

        Returns:
            InsertionResult[bool]
            
        Raises:
            TokenServiceException
        """
        method = f"{self.__class__.__name__}.push_coord_to_token"
        
        insertion_result = self._handler.coord.push_coord(
            token=token,
            coord=coord,
            coord_service=coord_service,
            token_validator=self.validator,
        )
        # Handle the case that, the insertion is not successful.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
            # Return the exception chain on failure.
                TokenServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenServiceException.MSG,
                    err_code=TokenServiceException.ERR_CODE,
                    ex=insertion_result.exception,
                )
            )
        # If the coord was successfully pushed onto the token's coord stack forward insertion result.
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def promote_pawn(
            self,
            rank: Rank,
            pawn: PawnToken,
            rank_service: RankService = RankService(),
            schema_service: SchemaService = SchemaService(),
    ) -> UpdateResult[PawnToken]:
        """
        # ACTION:
            1.  If the token is not a free pawn or it has been promoted send an exception chain to the
                InsertionResult.
            2.  If the rank fails validation send an exception chain to the InsertionResult.
            3.  Update the pawn's rank and promotion state then send the success InsertionResult.
            
        Args:
            rank:
            pawn: PawnToken
            rank_service: RankService
            schema_service: SchemaService
            
        Returns:
            UpdateResult[PawnToken]
            
        Raises:
            TokenServiceException
        """
        method = f"{self.__class__.__name__}.promote_pawn"
        
        promotion_result = self._handler.pawn_promoter.promote(
            rank=rank,
            pawn=pawn,
            rank_service=rank_service,
            schema_service=schema_service,
            token_validator=self.validator,
        )
        # Handle the case that, the promotion is not successful.
        if promotion_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=(
                    TokenServiceException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenServiceException.MSG,
                        err_code=TokenServiceException.ERR_CODE,
                        ex=promotion_result.exception
                    )
                )
            )
        return promotion_result
    
    @LoggingLevelRouter.monitor
    def deploy_on_board(self,token: Token,) -> InsertionResult[bool]:
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
