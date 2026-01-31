# src/chess/team/database/core/stack.py

"""
Module: chess.team.database.core.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, cast

from chess.system import DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, StackService, id_emitter
from chess.system.collection.stack.stack import D
from chess.team import Team,  TeamContextService,  TeamService


class TeamStackService(StackService[Team]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing team objects and their lifecycles.
    3.  Ensure integrity of team data stack
    4.  Stack data structure for Team objects with no guarantee of uniqueness.
    
    # PARENT:
        *   StackService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "TeamStackService"
    
    def __init__(
            self,
            name: str =SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Team] = List[Team],
            service: TeamService = TeamService(),
            context_service: TeamContextService = TeamContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   bag (List[Team])
            *   service (TeamService)
            *   context_service (TeamContextService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "TeamStackService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service
        )
    
    @property
    def team_service(self) -> TeamService:
        return cast(TeamService, self.entity_service)
    
    @property
    def team_context_service(self) -> TeamContextService:
        return cast(TeamContextService, self.context_service)
    
    @property
    def items(self) -> List[Team]:
        return self.items
    
    @LoggingLevelRouter.monitor
    def push_team(self, team: Team) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   item (Team)
        # RETURNS:
            *   InsertionResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        # RAISES:
            *   TeamStackServiceException
        """
        method = "TeamStackService.add_team"
        
        # Handle the case that the team is unsafe.
        validation = self.team_service.validator.validate(candidate=team)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TeamStackServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamStackServiceException.ERROR_CODE}",
                    ex=TeamInsertionFailedException(
                        message=f"{method}: {TeamInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Check if any of the item's attributes are already in use. ---#
        collision_detection = self._attribute_collision_detector(target=item)
        if collision_detection.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TeamStackServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamStackServiceException.ERROR_CODE}",
                    ex=TeamInsertionFailedException(
                        message=f"{method}: {TeamInsertionFailedException.ERROR_CODE}",
                        ex=collision_detection.exception
                    )
                )
            )
        # --- Team order is not required. Direct insertion into the stack is simpler that a push. ---#
        
        # On success return the item in the InsertionResult
        self.items.append(item)
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Team]:
        """
        # ACTION:
            1.  If the id is not certified safe send the exception in the DeletionResult. Else, call
                _delete_Teams_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_Teams_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        # RAISES:
            *   TeamStackServiceException
        """
        method = "TeamStackService.delete_Team_by_id"
        
        # Handle the case that there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TeamStackServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamStackServiceException.ERROR_CODE}",
                    ex=PoppingTeamStackFailedException(
                        message=f"{method}: {PoppingTeamStackFailedException.ERROR_CODE}",
                        ex=PoppingEmptyTeamStackException(
                            f"{method}: {PoppingEmptyTeamStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TeamStackServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamStackServiceException.ERROR_CODE}",
                    ex=PoppingTeamStackFailedException(
                        message=f"{method}: {PoppingTeamStackFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for an item with target id. ---#
        for item in self.items:
            if item.id == id:
                # Handle the case that the match is the wrong type.
                if not isinstance(item, Team):
                    # Return the exception chain on failure.
                    return DeletionResult.failure(
                        TeamStackServiceException(
                            message=f"ServiceId:{self.id}, {method}: {TeamStackServiceException.ERROR_CODE}",
                            ex=PoppingTeamStackFailedException(
                                message=f"{method}: {PoppingTeamStackFailedException.ERROR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Team, got {type(item).__name__} "
                                    f"instead of a Team."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted item in the DeletionResult. ---#
                Team = cast(Team, item)
                self.items.remove(Team)
                return DeletionResult.success(payload=Team)
        
        # If none of the items had that id return an empty DeletionResult.
        return DeletionResult.nothing_to_delete()
