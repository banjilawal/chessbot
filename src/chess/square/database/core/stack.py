# src/chess/square/database/core/stack.py

"""
Module: chess.square.database.core.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""
from copy import deepcopy
from typing import List, Optional, cast

from chess.system import (
    ComputationResult, NUMBER_OF_COLUMNS, StackService, DeletionResult, IdentityService, InsertionResult,
    LoggingLevelRouter, NUMBER_OF_ROWS, SearchResult, UpdateResult, id_emitter
)
from chess.square import (
    SquareContext, SquareNameAlreadyInUseException, SquareCoordAlreadyInUseException, SquareIdAlreadyInUseException,
    PoppingEmptySquareStackException, Square, SquareStackException, SquareService, SquareContextService,
    PoppingSquareException, PushingSquareException, FullSquareStackException
)
from chess.team import Team, TeamService
from chess.token import Token, TokenContext


class SquareStack(StackService[Square]):
    """
    # ROLE: Data Stack, AbstractSearcher EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Square objects and their lifecycles.
    3.  Ensure integrity of Square data stack
    4.  Stack data structure for Square objects with no guarantee of uniqueness.

    # PARENT:
        *   StackService[Square]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "SquareStack"
    
    _capacity: int
    _stack: List[Square]
    _service: SquareService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Square] = List[Square],
            service: SquareService = SquareService(),
            capacity: int = NUMBER_OF_ROWS * NUMBER_OF_COLUMNS,
            context_service: SquareContextService = SquareContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   items (List[Team])
            *   service (TeamService)
            *   context_service (TeamContextService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "SquareService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
        self._stack = items
        self._capacity = capacity
        self._service = service
    
    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
        
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def is_full(self) -> bool:
        return self.size == self._capacity
    
    @property
    def remaining_slots(self) -> int:
        return self.capacity - self.size
    
    @property
    def current_square(self) -> Optional[Square]:
        return self._stack[-1] if self._stack else None
    
    @property
    def integrity_service(self) -> SquareService:
        return self._service
    
    @property
    def context_service(self) -> SquareContextService:
        return cast(SquareContextService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def push(self, item: Square) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   item (Square)
        # RETURNS:
            *   InsertionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
            *   SquareStackException
        """
        method = "SquareStack.add_square"
        
        # Handle the case that the list is full
        if self.is_full:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=PushingSquareException(
                        message=f"{method}: {PushingSquareException.ERROR_CODE}",
                        ex=FullSquareStackException(f"{method}: {FullSquareStackException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # Handle the case that the item is unsafe.
        validation = self.integrity_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=PushingSquareException(
                        message=f"{method}: {PushingSquareException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Check if any of the item's attributes are already in use. ---#
        collision_detection = self._find_colliding_squares(target=item)
        if collision_detection.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=PushingSquareException(
                        message=f"{method}: {PushingSquareException.ERROR_CODE}",
                        ex=collision_detection.exception
                    )
                )
            )
        # --- Append the square and send the successful InsertionResult. ---#
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Square]:
        """
        # ACTION:
            1.  If the stack is empty send an exception in the DeletionResult. Else remove the
                square at the top of the stack and send in the DeletionResult
        # PARAMETERS:
                    *   None
        # RETURNS:
            *   DeletionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Token in the payload.
        # RAISES:
            *   SquareStackException
            *   PoppingEmptySquareStackException
        """
        method = "SquareStack.pop"
        
        # Handle the case that there are no tokens in the stack.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=PoppingSquareException(
                        message=f"{method}: {PoppingSquareException.ERROR_CODE}",
                        ex=PoppingEmptySquareStackException(
                            f"{method}: {PoppingEmptySquareStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Pop the updated square of the non-empty stack and return in the DeletionResult. ---#
        square = self._stack.pop(-1)
        DeletionResult.success(square)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Square]:
        """
        # ACTION:
            1.  If the id is not certified safe send the exception in the DeletionResult. Else, call
                _delete_squares_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_squares_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
            *   SquareStackException
        """
        method = "SquareStack.delete_square_by_id"
        
        # Handle the case that there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=PoppingSquareException(
                        message=f"{method}: {PoppingSquareException.ERROR_CODE}",
                        ex=PoppingEmptySquareStackException(
                            f"{method}: {PoppingEmptySquareStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=PoppingSquareException(
                        message=f"{method}: {PoppingSquareException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for an item with target id. ---#
        target = None
        for square in self._stack:
            if square.id == id:
                target = square
                self._stack.remove(square)
        if target is not None:
            return DeletionResult.success(payload=target)
        return DeletionResult.nothing_to_delete()
    
    def number_of_occupied_squares(self) -> ComputationResult[int]:
        """
        # ACTION:
            1.  Iterate through the squares. If a square is occupied increment the counter.
            2.  After the loop send total in the ComputationResult.
        # PARAMETERS:
            None
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: An int in the payload.
        # RAISES:
            None
        """
        method = "SquareStack.number_of_occupied_squares"
        
        number_of_occupied_squares = 0
        # Loop through the squares to get tally of occupied squares.
        for square in self._stack:
            if square.is_occupied:
                number_of_occupied_squares += 1
        # Send the total in the ComputationResult.
        return ComputationResult.success(number_of_occupied_squares)
    
    def _find_colliding_squares(self, target) -> SearchResult[Square]:
        """
        # ACTION:
            1.  If any stack members share either an id, coord or name with the target send and
                exception in the SearchResult. Those three properties must be unique within the game.
            2.  If no matches are found send an empty SearchResult indicating there were no collisions.
        # PARAMETERS:
                    *   target (Square)
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On failure: Exception or non-empty list.
                    - On success: Empty search result.
        # RAISES:
            *   TokenIdAlreadyInUseException
            *   TokenDesignationAlreadyInUseException
            *   TokenOpeningSquareAlreadyInUseException
        """
        method = "SquareStack.find_colliding_squares"
        
        # --- Loop through the stack to find matches. ---#
        for square in self._stack:
            
            # Return an exception in the SearchResult if a stack member shares the target's id.
            if square.id == target.id:
                return SearchResult.failure(
                    SquareIdAlreadyInUseException(
                        f"{method}: {SquareIdAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
            # Return an exception in the SearchResult if a stack member shares the target's coord.
            if square.coord == target.coord:
                return SearchResult.failure(
                    SquareCoordAlreadyInUseException(
                        f"{method}: {SquareCoordAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
            # Return an exception in the SearchResult if a stack member shares the target's name.
            if square.name.upper() == target.name.upper():
                return SearchResult.failure(
                    SquareNameAlreadyInUseException(
                        f"{method}: {SquareNameAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
        # --- At the happy path return an empty search result indication there are no collisions. ---#
        return SearchResult.empty()
    
    @LoggingLevelRouter.monitor
    def accept_roster_members_from_team(
            self,
            team: Team,
            team_service: TeamService = TeamService()
    ) -> UpdateResult[Team]:
        method = "SquareService.accept_roster_members_from_team"
        
        # Handle the case that the occupant is not certified safe.
        team_validation = team_service.validator.validate(candidate=team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=DeployingTeamRosterExcetion(
                        message=f"{method}: {DeployingTeamRosterExcetion.ERROR_CODE}",
                        ex=team_validation.exception
                    )
                )
            )
        pre_deployment_team = deepcopy(team)
        
        for square in self._stack:
            # Find the roster member's opening square.
            token_search_result = team.roster.search(context=TokenContext(opening_square=square))
            
            # Handle the case that the search is not completed.
            if token_search_result.is_failure:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=pre_deployment_team,
                    exception=SquareStackException(
                        message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                        ex=DeployingTeamRosterExcetion(
                            message=f"{method}: {DeployingTEamRosterExcetion.ERROR_CODE}",
                            ex=token_search_result.exception
                        )
                    )
                )
            # Handle the case that the no token which opens from the square is found.
            if token_search_result.is_empty:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=pre_deployment_team,
                    exception=SquareStackException(
                        message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                        ex=DeployingTeamRosterExcetion(
                            message=f"{method}: {DeployingTEamRosterExcetion.ERROR_CODE}",
                            ex=TokenDoesNotExistException(
                                f"{method}: {TokenDoesNotExistException.DEFAULT_MESSAGE}"
                            )
                        )
                    )
                )
            # --- Handoff the square's occupation to the integrity service. ---#
            square_update_result = self._service.add_occupant(square=square, token=token_search_result.payload[0])
            
            # Handle the case that the occupation fails.
            if square_update_result.is_failure:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=pre_deployment_team,
                    exception=SquareStackException(
                        message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                        ex=DeployingTeamRosterExcetion(
                            message=f"{method}: {DeployingTEamRosterExcetion.ERROR_CODE}",
                            ex=square_update_result.exception
                        )
                    )
                )
            # --- When the loop finishes send the success result to the caller. ---#
            return UpdateResult.update_success(original=pre_deployment_team, updated=team)