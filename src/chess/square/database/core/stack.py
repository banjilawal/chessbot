# src/chess/square/database/core/stack.py

"""
Module: chess.square.database.core.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""
from copy import deepcopy
from typing import List, Optional, cast

from chess.token import TokenContext
from chess.team import Team, TeamService
from chess.system import (
    ComputationResult, IdFactory, NUMBER_OF_COLUMNS, StackService, DeletionResult, IdentityService, InsertionResult,
    LoggingLevelRouter, NUMBER_OF_ROWS, SearchResult, UpdateResult, id_emitter
)
from chess.square import (
    CannotDeployUnderStrengthTeamException, DeployingTeamRosterException, SquareContext, TeamPartiallyDeployedException,
    SquareNameAlreadyInUseException, SquareCoordAlreadyInUseException, SquareIdAlreadyInUseException,
    PoppingEmptySquareStackException, Square, SquareStackException, SquareService, SquareContextService,
    PoppingSquareException, PushingSquareException, FullSquareStackException, TeamAlreadyDeployedException
)


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
    _context_service: SquareContextService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            service: SquareService = SquareService(),
            capacity: int = NUMBER_OF_ROWS * NUMBER_OF_COLUMNS,
            id: int = IdFactory.next_id(class_name="SquareStack"),
            context_service: SquareContextService = SquareContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   service (SquareService)
            *   context_service (SquareContextService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "SquareService.__init__"
        super().__init__(id=id,name=name,)
        self._stack = []
        self._capacity = capacity
        self._service = service
        self._context_service = context_service
    
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
    def current_item(self) -> Optional[Square]:
        return self._stack[-1] if self._stack else None
    
    @property
    def integrity_service(self) -> SquareService:
        return self._service
    
    @property
    def context_service(self) -> SquareContextService:
        return self._context_service
    
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
        # --- Handoff validation, id, designation or opening_square collision detection. ---#
        collision_report = self.integrity_service.collision_detector.detect(
            target=item,
            dataset=self._stack,
        )
        # Handle the case that, the collision analysis is not completed.
        if collision_report.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=PushingSquareException(
                        message=f"{method}: {PushingSquareException.ERROR_CODE}",
                        ex=collision_report.exception
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
        # --- Pop the non-empty token stack. ---#
        square = self._stack.pop(-1)
        # --- Send the success result to the caller. ---#
        DeletionResult.success(square)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Square]:
        """
        # ACTION:
            1.  If the id is not certified safe send an exception in the DeletionResult.
            2.  Create a temp variable for storing a square before it's deleted.
            3.  Iterate through the squares.
                    *   If a square's id matches the target record the square in a temp variable before deleting
                        it from the list.
            4.  After the loop is finishes, if the temp variable is not None send it in the deletion success result.
                Else, send the nothing to delete result instead.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   DeletionResult[Square]
        # RAISES:
            *   SquareStackException
            *   PoppingSquareException
            *   PoppingEmptySquareStackException
        """
        method = "SquareStack.delete_by_id"
        
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
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for square in self._stack:
            if square.id == id:
                # Record a hit before pulling it from the stack.
                target = square
                self._stack.remove(square)
        # --- After the purging loop finishes handle the possible return cases. ---#
        
        # At least one edge was removed.
        if target is not None:
            return DeletionResult.success(payload=target)
        # Default case: no edges were removed.
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
                    - On success: int.
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
    
    @LoggingLevelRouter.monitor
    def accept_roster_members_from_team(
            self,
            team: Team,
            team_service: TeamService = TeamService()
    ) -> UpdateResult[Team]:
        """
        # ACTION:
            1.  If the team fails its validation checks send the exception chain and team back in the UpdatedResult.
            2.  Iff the team has already been deployed or is at partial strength send the exception chain and team
                in the UpdatedResult.
            3.  Make a deep copy of the pre-deployment team.
                    *   The deep copy can be sent back instead of doing an expensive rollback.
                    *   If the update succeeds the client can use the pre-deployment copy for verifying correctness.
            4.  Iterate through the squares in the stack and search the roster for tokens which open on the squares.
                If any search fails send the exception chain and the pre-deployment team back.
            5.  For each successful search, handoff the token to the integrity service. If any occupation fails send
                the exception chain and the pre-deployment team back.
            6.  After the loop completes, if some tokens were not deployed, send the exception chain and
                the pre-deployment team back.
            7.  The update was successful send the pre-deployment team and updated teams back to the caller.
        # PARAMETERS:
            *   team (Team)
            *   team_service (TeamService)
        # RETURN:
            *   UpdateResult[Team]
        # RAISES:
            *   SquareStackException
            *   DeployingTeamRosterException
            *   TeamAlreadyDeployedException
            *   TeamPartiallyDeployedException
            *   CannotDeployUnderStrengthTeamException
        """
        method = "SquareService.accept_roster_members_from_team"
        
        # Handle the case that the occupant is not certified safe.
        team_validation = team_service.validator.validate(candidate=team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=DeployingTeamRosterException(
                        message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                        ex=team_validation.exception
                    )
                )
            )
        # Handle the case that the team has already been deployed
        if team.roster.is_empty:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=DeployingTeamRosterException(
                        message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                        ex=TeamAlreadyDeployedException(f"{method}: {TeamAlreadyDeployedException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # Handle the case that the team is not at full strength.
        if team.roster.is_empty:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                    ex=DeployingTeamRosterException(
                        message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                        ex=CannotDeployUnderStrengthTeamException(
                            f"{method}: {CannotDeployUnderStrengthTeamException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- The validation checks were passed, make a deep copy of the team and run deployment steps ---#
        pre_deployment_team = deepcopy(team)
        
        total_occupations = 0
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
                        ex=DeployingTeamRosterException(
                            message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                            ex=token_search_result.exception
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
                        ex=DeployingTeamRosterException(
                            message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                            ex=square_update_result.exception
                        )
                    )
                )
            # Increment the number of occupations.
            total_occupations += 1
            
            # Handle the case that at least one token was not deployed.
            if total_occupations != team.roster.size:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=pre_deployment_team,
                    exception=SquareStackException(
                        message=f"ServiceId:{self.id}, {method}: {SquareStackException.ERROR_CODE}",
                        ex=DeployingTeamRosterException(
                            message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                            ex=TeamPartiallyDeployedException(
                                f"{method}: {TeamPartiallyDeployedException.DEFAULT_MESSAGE}"
                            )
                        )
                    )
                )
            # --- When the loop finishes send the success result to the caller. ---#
            return UpdateResult.update_success(original=pre_deployment_team, updated=team)
      
    @LoggingLevelRouter.monitor
    def query(self, context: SquareContext) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a SquareStackException 
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (SquareContext)
        # RETURN:
            *   SearchResult[List[Square] containing either:
                    - On failure: An exception.
                    - On success: List[Square] in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   SquareStackException
        """
        method = "SquareStack.query"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareStackException(
                    message=f"ServiceID:{self.id} {method}: {SquareStackException.ERROR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result