# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import cast

from chess.square.service.exception.insertion import OccupiedSquareCannotRecieveFormationException
from chess.square.service.exception.occupant.add.full import CannotEnterOccupiedSquareException
from chess.square.state import SquareState
from chess.system import (
    DeletionResult, EntityService, IdFactory, InsertionResult, LoggingLevelRouter, NUMBER_OF_ROWS,
    UpdateResult, ValidationResult, id_emitter
)
from chess.square import (
    AddingFormationToSquareFailedException, AddingSquareOccupantException, DisabledTokenOccupyingSquareException,
    NothingToRemoveFromEmptySquareException, RemovingSquareOccupantException, Square, SquareBuilder,
    SquareServiceException, SquareTokenRelationAnalyzer, SquareValidator, TokenEnteringSquareOnWrongBoardException,
    TokenEnteringWrongOpeningSquareException
)
from chess.team import Team, TeamService
from chess.token import Token, TokenBoardState, TokenContext, TokenDoesNotExistForRemovalException, TokenService


class SquareService(EntityService[Square]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Square microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Square state by providing single entry and exit points to Square
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "SquareService"
    _square_token_relation_analyzer: SquareTokenRelationAnalyzer
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: SquareBuilder = SquareBuilder(),
            validator: SquareValidator = SquareValidator(),
            id: int = IdFactory.next_id(class_name="SquareService"),
            relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (SquareFactory)
            *   validator (SquareValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._square_token_relation_analyzer = relation_analyzer
    
    @property
    def builder(self) -> SquareBuilder:
        """get SquareBuilder"""
        return cast(SquareBuilder, self.entity_builder)
    
    @property
    def validator(self) -> SquareValidator:
        """get SquareValidator"""
        return cast(SquareValidator, self.entity_validator)
    
    @property
    def square_token_relation_analyzer(self) -> SquareTokenRelationAnalyzer:
        return self._square_token_relation_analyzer
    
    @LoggingLevelRouter.monitor
    def remove_occupant(self, square: Square) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  We need the token removed from the square so removing an occupant sends a DeletionResult unlike
                adding an occupant where the caller needs the original square to verify correctness.
            2.  If the square is either unsafe or empty send an exception chain in the DeletionResult.
            3.  Store the store's occupant in a local variable.
            4.  Set the square's occupant to None and its state to empty.
            5.  Send the token back in the DeletionResult.
        # PARAMETERS:
            *   square (Square)
        # RETURN:
            *   DeletionResult[Token]:
                    - On failure: Exception.
                    - On success: Token.
        # RAISES:
            *   SquareServiceException
            *   RemovingSquareOccupantException
            *   NothingToRemoveFromEmptySquareException
        """
        method = "SquareService.remove_occupant"
        
        # Handle the case that the square is not certified as safe.
        validation = self.validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=RemovingSquareOccupantException(
                        message=f"{method}: {RemovingSquareOccupantException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that the square is empty.
        if square.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=RemovingSquareOccupantException(
                        message=f"{method}: {RemovingSquareOccupantException.ERROR_CODE}",
                        ex=NothingToRemoveFromEmptySquareException(
                            f"{method}: {NothingToRemoveFromEmptySquareException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Process the removal logic that maintains integrity and consistency. ---#
        
        # Store the square's occupant.
        token = square.occupant
        # Remove the occupant then update the square's state.
        square.occupant = None
        square.state = SquareState.EMPTY
        
        # --- Send the deletion success result to the caller. ---#
        DeletionResult.success(payload=token)
    
    @LoggingLevelRouter.monitor
    def add_occupant(
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
            *   SquareServiceException
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
                exception=SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
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
                exception=SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
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
                exception=SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
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
                exception=SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
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
                exception=SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
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
                exception=SquareServiceException(
                    message=f"ServiceId: {self.id}, {method}: {SquareServiceException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=validate_token_opening_square_result.exception
                    )
                )
            )
        # --- After integrity and consistency checks are passed, process the occupation. ---#
        
        # Make a deep copy of the square before its occupied then
        original_square  = deepcopy(square)
        # Update state on the square side.
        square.occupant = token
        square.state = SquareState.OCCUPIED
        # Update state ob the token side.
        token.positions.push(square.coord)
        if token.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            token.board_state = TokenBoardState.DEPLOYED_ON_BOARD
            
        # --- Send the update success result to the caller. ---#
        return UpdateResult.update_success(original=original_square, updated=square)
    
    @LoggingLevelRouter.monitor
    def _verify_token_opens_from_square(self, square: Square, token: Token) -> ValidationResult[Square]:
        method = "SquareService._verify_token_forms_on_square"
        
        # Handle the case that the occupant belongs to a different square.
        if square.name.upper() != token.opening_square_name.upper():
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenEnteringWrongOpeningSquareException(f"{method}: {TokenEnteringWrongOpeningSquareException.}")
            )
        return ValidationResult.success(payload=token)