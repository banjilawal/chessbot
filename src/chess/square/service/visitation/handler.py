# src/chess/square/service/visitation/handlerpy

"""
Module: chess.square.service.visitation.__init__
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from chess.square import (
    NoVisitForTerminationException, SquareVisitTerminationException, Square, SquareState, SquareValidator,
    VisitingWrongOpeningSquareException, TokenVisitHandlerException
)
from chess.system import DeletionResult, LoggingLevelRouter, UpdateResult, ValidationResult
from chess.token import Token, TokenBoardState, TokenService


class TokenVisitHandler:
    _token_service: TokenService
    
    def __init__(self, token_service: TokenService):
        self._token_service = token_service
        
    @property
    def token_service(self) -> TokenService:
        return self._token_service
    
    @LoggingLevelRouter.monitor
    def start_visit(
            self,
            token: Token,
            square: Square,
            token_service: TokenService = TokenService(),
    ) -> UpdateResult[Square]:
        """
        # ACTION:
            1.  If the square is either unsafe or occupied send the exception chain and the unmodified square back
                in the UpdatedResult.
            2.  If the token is either
                    *   Disabled.
                    *   Not certified safe.
                    *   Belongs to a different board.
                    *   unformed but want to start from the wrong square.
                Send the exception chain and the unmodified square back in the UpdatedResult.
            3.  Make a deep copy of the square before its occupied.
            4.  Put the token in the square and update the square's occupation state.
            5.  Push the square's coord onto the token's position and update the token's board state if necessary.
            6.  Send the deep copy and the back to the caller in the UpdatedResult.
        # PARAMETERS:
            *   token (Token)
            *   square (Square)
            *   token_service (TokenService)
        # RETURN:
            *   UpdateResult[Square]
        # RAISES:
            *   TokenVisitHandlerException
            *   AddingSquareOccupantException
            *   CannotEnterOccupiedSquareException
            *   TokenEnteringSquareOnWrongBoardException
        """
        method = "SquareService.add_occupant"
        
        # Handle the case that the item is not certified safe.
        square_validation = self.validator.validate(candidate=square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    message=f"ServiceId: {self.id}, {method}: {TokenVisitHandlerException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=square_validation.exception
                    )
                )
            )
        # Handle the case that the square is already occupied.
        if square.is_occupied:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    message=f"ServiceId: {self.id}, {method}: {TokenVisitHandlerException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=CannotEnterOccupiedSquareException(
                            f"{method}: {CannotEnterOccupiedSquareException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the occupant is not certified safe.
        token_validation = token_service.validator.validate(candidate=token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    message=f"ServiceId: {self.id}, {method}: {TokenVisitHandlerException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=token_validation.exception
                    )
                )
            )
        # Handle the case that the occupant belongs to a different board
        if token.team.board != square.board:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    message=f"ServiceId: {self.id}, {method}: {TokenVisitHandlerException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=TokenEnteringSquareOnWrongBoardException(
                            f"{method}: {TokenEnteringSquareOnWrongBoardException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the occupant is disabled
        if token.is_disabled:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    message=f"ServiceId: {self.id}, {method}: {TokenVisitHandlerException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=DisabledTokenOccupyingSquareException(
                            f"{method}: {DisabledTokenOccupyingSquareException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that an unformed token is trying to start from the wrong square.
        if token.is_not_deployed:
            validate_token_opening_square_result = self._verify_token_opens_fromn_square(
                square=square,
                token=token
            )
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    message=f"ServiceId: {self.id}, {method}: {TokenVisitHandlerException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=validate_token_opening_square_result.exception
                    )
                )
            )
        # --- After integrity and consistency checks are passed, process the occupation. ---#
        
        # Make a deep copy of the square before its occupied then
        pre_occupation_square = deepcopy(square)
        # Update state on the square side.
        square.occupant = token
        square.state = SquareState.OCCUPIED
        # Update state ob the token side.
        token.positions.push(square.coord)
        if token.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            token.board_state = TokenBoardState.DEPLOYED_ON_BOARD
        
        # --- Send the update success result to the caller. ---#
        return UpdateResult.update_success(original=pre_occupation_square, updated=square)
    
    @LoggingLevelRouter.monitor
    def terminate_visit(
            self,
            square: Square,
            square_validator: SquareValidator = SquareValidator(),
    ) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the square fails its safety checks send and exception chain in the DeletionResult.
            2.  If the square is empty send an exception chain in the DeletionResult.
            3.  Store the square's occupant in a temp variable.
            4.  Set square.occupant to null and  square.state to empty.
        # PARAMETERS:
            *   square (Square)
        # RETURN:
            *   DeletionResult[Token]
        # RAISES:
            *   TokenVisitHandlerException
            *   SquareVisitTerminationException
            *   NoVisitForTerminationException
        """
        method = "TokenVistHandler.terminate_visit"
        
        # Handle the case that, the square is not certified as safe.
        validation = square_validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenVisitHandlerException(
                    message=f"{method}: {TokenVisitHandlerException.ERROR_CODE}",
                    ex=SquareVisitTerminationException(
                        message=f"{method}: {SquareVisitTerminationException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that, the square is empty.
        if square.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenVisitHandlerException(
                    message=f"{method}: {TokenVisitHandlerException.ERROR_CODE}",
                    ex=SquareVisitTerminationException(
                        message=f"{method}: {SquareVisitTerminationException.ERROR_CODE}",
                        ex=NoVisitForTerminationException(
                            f"{method}: {NoVisitForTerminationException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Process the removal logic that maintains integrity and consistency. ---#
        
        # Store the square's occupant.
        token = square.occupant
        
        # Break the relationship between the square and the token then update the square's state.
        square.occupant = None
        square.state = SquareState.EMPTY
        
        # --- Send the success result to the client. ---#
        DeletionResult.success(payload=token)
    
    @LoggingLevelRouter.monitor
    def _verify_token_opens_from_square(self, square: Square, token: Token) -> ValidationResult[Square]:
        """
        # ACTION:
            1.  If the token and square belong to different boards send an exception in the ValidationResult.
                Else, return the token in the success result.
        # PARAMETERS:
            *   token (Token)
            *   square (Square)
        # RETURN:
            *   UpdateResult[Square]
        # RAISES:
            *   VisitingWrongOpeningSquareException
        """
        method = "SquareService._verify_token_forms_on_square"
        
        # Handle the case that the occupant belongs to a different square.
        if square.name.upper() != token.opening_square_name.upper():
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VisitingWrongOpeningSquareException(
                    f"{method}: {VisitingWrongOpeningSquareException.DEFAULT_MESSAGE}"
                )
            )
        return ValidationResult.success(payload=token)

