# src/chess/square/service/visitation/handler.py

"""
Module: chess.square.service.visitation.handler
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy

from chess.square import (
    NoVisitForTerminationException, Square, SquareState, SquareValidator, SquareVisitTerminationException,
    SquareVisitorDisabledException, StartingSquareVisitException, TokenVisitHandlerException,
    VisitingOccupiedSquareException, VisitingWrongOpeningSquareException, VisitorFromWrongBoardException
)
from chess.system import DeletionResult, LoggingLevelRouter, UpdateResult, ValidationResult
from chess.token import Token, TokenBoardState, TokenService


class TokenVisitHandler:
    """
    # ROLE: Consistency, Integrity Maintenance, Lifecycle Management

    # RESPONSIBILITIES:
    1.  Ensure integrity and consistency  are maintained in all stages of the square occupation lifecycle.

    # PARENT:
        *   IntegrityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   token-service (TokenService)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   token_service (TokenService)
        Inherited:
        None

    # LOCAL METHODS:
        *   start_visit(token: Token, square: Square, square_validator: SquareValidator) -> UpdateResult[Square]
        *   terminate_visit(square: Square, square_validator: SquareValidator) -> DeletionResult[Token]
        
    # INHERITED METHODS:
    None
    """
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
            square_validator: SquareValidator = SquareValidator(),
    ) -> UpdateResult[Square]:
        """
        # ACTION:
            1.  If the square is either unsafe put the square and exception chain  in the UpdateResult  then
                return the client. Else make a deep copy of the square.
            2.  If th  square is already occupied put the deep_copy and the exception chain  in the UpdateResult
                sent to the client.
            3.  If the token is either
                    *   Disabled.
                    *   Not certified safe.
                    *   Belongs to a different board.
                    *   unformed but want to start from the wrong square.
                put deep_copy and the exception chain in the UpdateResult sent to the client.
            4.  Configure the square side of the square-token binding.
            5.  Configure the token side of the square-token binding.
            6.  Send deep_copy and the current square in the success result.
        # PARAMETERS:
            *   token (Token)
            *   square (Square)
            *   square_validator (SquareValidator)
        # RETURN:
            *   UpdateResult[Square]
        # RAISES:
            *   TokenVisitHandlerException
            *   StartingSquareVisitException
            *   VisitingOccupiedSquareException
            *   VisitorFromWrongBoardException
            *   SquareVisitorDisabledException
        """
        method = "SquareService.add_occupant"
        
        # Handle the case that, the item is not certified safe.
        square_validation = square_validator.validate(candidate=square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=TokenVisitHandlerException(
                    msg=f"{method}: {TokenVisitHandlerException.ERR_CODE}",
                    ex=StartingSquareVisitException(
                        msg=f"{method}: {StartingSquareVisitException.ERR_CODE}",
                        ex=square_validation.exception
                    )
                )
            )
        # --- Make a deep copy of the square for the original field, after its validated. ---#
        pre_update_square = deepcopy(square)
        
        # Handle the case that, the square is already occupied.
        if square.is_occupied:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=TokenVisitHandlerException(
                    msg=f"{method}: {TokenVisitHandlerException.ERR_CODE}",
                    ex=StartingSquareVisitException(
                        msg=f"{method}: {StartingSquareVisitException.ERR_CODE}",
                        ex=VisitingOccupiedSquareException(
                            f"{method}: {VisitingOccupiedSquareException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the token is not certified safe.
        token_validation = self._token_service.validator.validate(candidate=token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=TokenVisitHandlerException(
                    msg=f"{method}: {TokenVisitHandlerException.ERR_CODE}",
                    ex=StartingSquareVisitException(
                        msg=f"{method}: {StartingSquareVisitException.ERR_CODE}",
                        ex=token_validation.exception
                    )
                )
            )
        # Handle the case that, the token belongs to a different board
        if token.team.board != square.board:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=TokenVisitHandlerException(
                    msg=f"{method}: {TokenVisitHandlerException.ERR_CODE}",
                    ex=StartingSquareVisitException(
                        msg=f"{method}: {StartingSquareVisitException.ERR_CODE}",
                        ex=VisitorFromWrongBoardException(
                            f"{method}: {VisitorFromWrongBoardException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the occupant is disabled
        if token.is_disabled:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=TokenVisitHandlerException(
                    msg=f"ServiceId: {self.id}, {method}: {TokenVisitHandlerException.ERR_CODE}",
                    ex=StartingSquareVisitException(
                        msg=f"{method}: {StartingSquareVisitException.ERR_CODE}",
                        ex=SquareVisitorDisabledException(
                            f"{method}: {SquareVisitorDisabledException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, an unformed token is trying to start from the wrong square.
        if token.is_not_deployed:
            validate_token_opening_square_result = self._verify_token_opens_from_square(
                square=square,
                token=token
            )
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=TokenVisitHandlerException(
                    msg=f"{method}: {TokenVisitHandlerException.ERR_CODE}",
                    ex=StartingSquareVisitException(
                        msg=f"{method}: {StartingSquareVisitException.ERR_CODE}",
                        ex=validate_token_opening_square_result.exception
                    )
                )
            )
        # --- Integrity and consistency checks are passed. Start the visit. ---#
        
        # Set the square side of the relationship.
        square.occupant = token
        square.state = SquareState.OCCUPIED
        
        # Set the token side of the relationship.
        token.positions.push(square.coord)
        if token.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            token.board_state = TokenBoardState.DEPLOYED_ON_BOARD
        
        # --- Send the update success result to the client. ---#
        return UpdateResult.update_success(original=pre_update_square, updated=square)
    
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
                    msg=f"{method}: {TokenVisitHandlerException.ERR_CODE}",
                    ex=SquareVisitTerminationException(
                        msg=f"{method}: {SquareVisitTerminationException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that, the square is empty.
        if square.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenVisitHandlerException(
                    msg=f"{method}: {TokenVisitHandlerException.ERR_CODE}",
                    ex=SquareVisitTerminationException(
                        msg=f"{method}: {SquareVisitTerminationException.ERR_CODE}",
                        ex=NoVisitForTerminationException(
                            f"{method}: {NoVisitForTerminationException.MSG}"
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
    def _verify_token_opens_from_square(self, target: Square, visitor: Token) -> ValidationResult[Square]:
        """
        # ACTION:
            1.  If the token's opening name differs from the target's return a ValidationResult with the exception.
                Else return a Validation success result.
        # PARAMETERS:
            *   visitor (Token)
            *   target (Square)
        # RETURN:
            *   ValidationResult[Square]
        # RAISES:
            *   VisitingWrongOpeningSquareException
        """
        method = "TokenVisitHandler._verify_token_forms_on_square"
        
        # Handle the case that, the occupant belongs to a different square.
        if target.name.upper() != visitor.opening_square_name.upper():
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VisitingWrongOpeningSquareException(
                    f"{method}: {VisitingWrongOpeningSquareException.MSG}"
                )
            )
        # --- Send the success result to the caller. ---#
        return ValidationResult.success(payload=target)

