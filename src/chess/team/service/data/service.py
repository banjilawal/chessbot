# src/chess/team/service/data/service.py

"""
Module: chess.team.service.data.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.system import DataService, id_emitter
from chess.team import Team, TeamContext, TeamContextService, TeamInsertionFailedException, TeamService


class TeamDataService(DataService[Team]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Stack data structure for Team objects with no guarantee of uniqueness.
    3.  Implements search, insert, delete, and update operations on Team objects.
    4.  Ensure integrity of team data stack
    5.  Microservice for managing team objects and their lifecycles.

    # PARENT:
        *   DataService

    # PROVIDES:
        *   TeamService
        *   TeamContextService
        *   TeamStack

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    See DataService class for inherited attributes.
    """
    DEFAULT_NAME = "TeamDataService"
    
    def __init__(
            self,
            name: str =DEFAULT_NAME,
            id: int = id_emitter.service_id,
            items: List[Team] = List[Team],
            service: TeamService = TeamService(),
            context_service: TeamContextService = TeamContextService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = DEFAULT_NAME
            *   items (List[Team]): = List[Team]
            *   service (TeamService): = TeamService()
            *   context_service (TeamContextService): = TeamContextService()

        # Returns:
        None

        # Raises:
        None
        """
        method = "TeamDataService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service
        )
    
    @property
    def team_service(self) -> TeamService:
        return cast(TeamService, self.service)
    
    @property
    def team_context_service(self) -> TeamContextService:
        return cast(TeamContextService, self.context_service)
    
    # def push_item(self, item: Team) -> InsertionResult[Team]:
    #     """
    #     # ACTION:
    #     1.  Use TeamDataService.service.validator to certify item.
    #     2.  If certification fails return the exception inside an InsertionResult.
    #     3.  Otherwise, push item onto the stack.
    #     4.  Send the successfully pushed data back in an InsertionResult.
    #
    #     # PARAMETERS:
    #         *   item (Team)
    #
    #     # Returns:
    #     InsertionResult[TTeam] containing either:
    #         - On success: Team in the payload.
    #         - On failure: Exception.
    #
    #     # Raises:
    #         *   TeamInsertionFailedException
    #     """
    #     method = "TeamDataService.push"
    #
    #     try:
    #         # Start the error detection process.
    #         validation = self.data.item_validator.validate(item)
    #         if validation.is_failure():
    #             return InsertionResult.failure(validation.exception)
    #         self.items.append(item)
    #         # After item is pushed onto the stack indicate success by sending it
    #         # back to the caller.
    #         return InsertionResult.success(payload=item)
    #
    #     # Finally, if there is an unhandled exception Wrap a TeamInsertionFailedException around it
    #     # then return exception chain inside an InsertionResult.
    #     except Exception as ex:
    #         return InsertionResult.failure(
    #             TeamInsertionFailedException(
    #                 ex=ex, message=f"{method}: {TeamInsertionFailedException.DEFAULT_MESSAGE}"
    #             )
    #         )
    #
    # @LoggingLevelRouter.monitor
    # def search(self, context: TeamContext) -> SearchResult[List[Team]]:
    #     """
    #     # ACTION:
    #     1.  Pass context argument to self.searcher.
    #     2.  Pass self.items and self.context_service.validator to self.searcher's renaming params.
    #     3.  The Finder object will return any exceptions if it fails, success otherwise.
    #     4.  Because Finder object does all the error using a try-catch is uneccesar
    #
    #     2.  If certification fails return the exception inside an InsertionResult.
    #     3.  Otherwise, push item onto the stack.
    #     4.  Send the successfully pushed data back in an InsertionResult.
    #
    #     # PARAMETERS:
    #         *   item (Team)
    #
    #     # Returns:
    #     SearchResult[List[Team]] containing either:
    #         - On success: List[Team] in the payload.
    #         - On failure: Exception.
    #
    #     # Raises:
    #     None
    #     """
    #     method = "TeamDataService.searcher"
    #
    #     return self.search.find(
    #         data_set=self.items, context=context, context_validator=self.context_service.item_validator
    #     )
