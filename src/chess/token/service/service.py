# src/chess/token/service/service.py

"""
Module: chess.token.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import cast

from chess.board import Board, BoardService
from chess.formation import FormationService
from chess.coord import Coord, CoordService, DuplicateCoordPushException, PoppingEmtpyCoordStackException
from chess.system import DeletionResult, EntityService, InsertionResult, LoggingLevelRouter, id_emitter
from chess.token import (
    OverMoveUndoLimitException, Token, TokenFactory, TokenOpeningSquareNullException, TokenServiceException,
    TokenValidator
)

class TokenService(EntityService[Token]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Token microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Token state by providing single entry and exit points to Token
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   formation_service (FormationService)

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "TokenService"
    _formation_service: FormationService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: TokenFactory = TokenFactory(),
            validator: TokenValidator = TokenValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (TokenFactory)
            *   validator (TokenValidator)

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> TokenFactory:
        """get TokenFactory"""
        return cast(TokenFactory, self.entity_builder)
    
    @property
    def validator(self) -> TokenValidator:
        """get TokenValidator"""
        return cast(TokenValidator, self.entity_validator)
    
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
    
    # @LoggingLevelRouter.monitor
    # def form_token_on_board(
    #         self,
    #         token: Token,
    #         board: Board,
    #         board_service: BoardService = BoardService(),
    # ):
    #     token_validation = self.validator.validate(candidate=token)
    #     if token_validation.is_failure:
        
    @LoggingLevelRouter.monitor
    def pop_coord_from_token(self, token) -> DeletionResult[Coord]:
        """
        # ACTION:
            1.  If the token fails validation returns the exception in the DeletionResult.
            2.  If the token has not been activated with an opening square return the exception in the DeletionResult.
            3.  If the token has an empty coord stack return the exception in the DeletionResult.
            4.  If a new coord has not been pushed since the last undo send and exception in the DeletionResult.
                Else, forward the results of token.positions.pop_coord() to the caller.
        # PARAMETERS:
            *   token (Token)
        # RETURN:
            *   DeletionResult[Coord] containing either:
                    - On failure: Exception
                    - On success: Coord in the payload.
        # RAISES:
            *   TokenServiceException
            *   OverMoveUndoLimitException
            *   TokenOpeningSquareNullException
            *   PoppingEmtpyCoordStackException
        """
        method = "TokenService.pop_coord_from_token"
        
        validation = self.validator.validate(token)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=validation.exception
                )
            )
        # Handle the case that the opening square is null which implies there are no moves to undo.
        if token.opening_square is None:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=TokenOpeningSquareNullException(f"{method}: {TokenOpeningSquareNullException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the token has no positions that can be removed.
        if token.positions.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=PoppingEmtpyCoordStackException(
                        f"{method}: {PoppingEmtpyCoordStackException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that an attempt is made to undo more than one turn.
        if token.previous_coord == token.current_address:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=OverMoveUndoLimitException(f"{method}: {OverMoveUndoLimitException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the coord stack pop operation fails.
        pop_result = token.positions.pop_coord()
        if token.previous_coord == token.current_address:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=pop_result.exception
                )
            )
        # Otherwise return the successful pop operation's data to the caller in the DeletionResult.
        return pop_result
    
    @LoggingLevelRouter.monitor
    def push_coord_to_token(
            self,
            token: Token,
            position: Coord,
            coord_service: CoordService = CoordService()
    ) -> InsertionResult[Coord]:
        """
        # ACTION:
            1.  If the token or coord fail their validations return the exception in the InsertionResult.
            2.  If the position is already the current position return the exception in the InsertionResult.
            3.  If the pushing the position to the token's coord stack fails encapsulate the exception then
                send the exception chain in the InsertionResult.'
        # PARAMETERS:
            *   token (Token)
            *   coord (Coord)
            *   coord_service (CoordService)
        # RETURN:
            *   InsertionResult[Coord] containing either:
                    - On failure: Exception
                    - On success: Coord in the payload.
        # RAISES:
            *   TokenServiceException
            *   CoordAlreadyToppingStackException
        """
        method = "TokenService.push_coord_to_token"
        
        # Handle the case that the token is not certified safe.
        token_validation = self.validator.validate(token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=token_validation.exception
                )
            )
        # Handle the case that the position is not certified safe.
        position_validation = coord_service.validate(position)
        if position_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=token_validation.exception
                )
            )
        # Handle the case that the token is already the current position
        if position == token.current_position:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenServiceException.ERROR_CODE}",
                    ex=DuplicateCoordPushException(
                        f"{method}: {DuplicateCoordPushException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that adding the coord to the token's position history fails.
        insertion_result = token.positions.push_coord(coord=position)
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenServiceException.ERROR_CODE}",
                    ex=insertion_result.exception
                )
            )
        # If the coord was successfully pushed onto the token's coord stack forward insertion result.
        return insertion_result
