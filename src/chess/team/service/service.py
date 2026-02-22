# src/chess/team/service.py

"""
Module: chess.team.service
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""

from __future__ import annotations
from typing import List, cast

from chess.rank import RankService
from chess.schema import SchemaService
from chess.formation import FormationKey, FormationService
from chess.system import (
    DeletionResult, EntityService, IdentityService, InsertionResult, LoggingLevelRouter, SearchResult, id_emitter
)
from chess.team import (
    FillingTeamRosterFailedException, HostageRelationAnalyzer, RosterRelationAnalyzer, Team, TeamBuilder,
    TeamContext, TeamDatabaseException, TeamServiceException, TeamValidator
)


class TeamService(EntityService[Team]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Team microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Team state by providing single entry and exit points to Team
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   roster_relation_analyzer (RosterRelationAnalyzer)
        *   hostage_relation_analyzer (HostageRelationAnalyzer)

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "TeamService"
    
    _schema_service: SchemaService
    _roster_relation_analyzer: RosterRelationAnalyzer
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: TeamBuilder = TeamBuilder(),
            validator: TeamValidator = TeamValidator(),
            schema_service: SchemaService = SchemaService(),
            roster_relation_analyzer: RosterRelationAnalyzer = RosterRelationAnalyzer(),
    ):
        """
        # ACTION:
             Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (TeamBuilder)
            *   validator (TeamValidator)
            *   roster_relation_analyzer (RosterRelationAnalyzer)
            *   hostage_relation_analyzer (HostageRelationAnalyzer)
        # RETURNS:
                None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._schema_service = schema_service
        self._roster_relation_analyzer = roster_relation_analyzer
    
    @property
    def builder(self) -> TeamBuilder:
        """get TeamBuilder."""
        return cast(TeamBuilder, self.entity_builder)
    
    @property
    def validator(self) -> TeamValidator:
        """get TeamValidator."""
        return cast(TeamValidator, self.entity_validator)
    
    @property
    def roster_relation_analyzer(self) -> RosterRelationAnalyzer:
        return self._roster_relation_analyzer
    
    @property
    def schema_service(self) -> SchemaService:
        return self._schema_service
    
    def fill_team_roster(
            self,
            team: Team,
            rank_service: RankService = RankService(),
            identity_service: IdentityService = IdentityService(),
            formation_service: FormationService = FormationService(),
    ) -> InsertionResult:
        """
        # ACTION:
            1.  If a successful relation analysis does not show that the team and piece are partially related send an
                exception. Also, send the exception if the relation analysis fails.
            2.  If the rank's quota is full, send the exception in InsertionResult. Else get the result of the
                super().push_item.
            3.  If the super class raises an exception, wrap and forward it. Else, forward the super class success
                directly to the caller.
        # PARAMETERS:
            *   team (Team)
            *   piece (Piece)
        # RETURN:
            *   InsertionResult[occupant] containing either:
                    - On failure: Exception
                    - On success: Token
        # RAISES:
            *   TeamServiceException
        """
        method = "TeamService.fill_team_roster"
        
        # Handle the case that the team is not certified safe.
        team_validation = self.validator.validate(candidate=team)
        if team_validation.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=FillingTeamRosterFailedException(
                        message=f"{method}: {FillingTeamRosterFailedException.ERROR_CODE}",
                        ex=team_validation.exception
                    )
                )
            )
        # --- Get the formations for the team by its color. ---#
        formation_lookup_result = formation_service.lookup_formation(super_key=FormationKey(color=team.schema.color))
        
        # Handle the case that the formation lookup was not completed.
        if formation_lookup_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=FillingTeamRosterFailedException(
                        message=f"{method}: {FillingTeamRosterFailedException.ERROR_CODE}",
                        ex=formation_lookup_result.exception
                    )
                )
            )
        # --- Iterate through each formation to get each occupant's build params. ---#
        for formation in formation_lookup_result.payload:

            # Build the token.
            token_build_result = team.roster.integrity_service.builder.build(
                    owner=team,
                    id=id_emitter.token_id,
                    formation=formation,
                    team_service=self,
                    rank_service=rank_service,
                    identity_service=identity_service,
                    formation_service=formation_service,
            )
            # Handle the case that the occupant does not get built.
            if token_build_result.is_failure:
                # Return exception chain on failure.
                return InsertionResult.failure(
                    TeamServiceException(
                        message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                        ex=FillingTeamRosterFailedException(
                            message=f"{method}: {FillingTeamRosterFailedException.ERROR_CODE}",
                            ex=token_build_result.exception
                        )
                    )
                )
            # --- The factory returns only instances of concrete tokens so don't cast during the insert.---#
            insertion_result = team.roster.insert(token=token_build_result.payload)
            
            # Handle the case that the insertion was not completed.
            if insertion_result.is_failure:
                # Return exception chain on failure.
                return InsertionResult.failure(
                    TeamServiceException(
                        message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                        ex=FillingTeamRosterFailedException(
                            message=f"{method}: {FillingTeamRosterFailedException.ERROR_CODE}",
                            ex=insertion_result.exception
                        )
                    )
                )
        # --- Return the success result when the look finishes. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def delete_by_id(self, id: int, identity_service: IdentityService = IdentityService()) -> DeletionResult[Team]:
        """
        # ACTION:
            1.  Get the result of calling _token_database_core.delete_token_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   TeamDatabaseException
        """
        method = "TeamDatabase.remove_token"
        
        # --- Handoff the deletion responsibility to _token_database_core. ---#
        deletion_result = self._team_stack.delete_by_id(id=id, identity_service=identity_service)
        
        # Handle the case that the deletion was not completed.
        if deletion_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TeamDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {TeamDatabaseException.ERROR_CODE}",
                    ex=deletion_result.exception
                )
            )
        # --- For either a successful or null deletion result directly forward to the caller. ---#
        return deletion_result
    
    @LoggingLevelRouter.monitor
    def insert(self, team: Team) -> InsertionResult:
        """
        # ACTION:
            1.  If the item fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the item either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _token_database_core.insert_token fails send the wrapped exception in the
                InsertionResult. Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   team (Team)
        # RETURN:
            *   InsertionResult containing either:
                    - On failure: An exception.
                    - On success: bool in payload.
        # RAISES:
            *   TeamDatabaseException
        """
        method = "TeamDatabase.insert"
        
        # --- Use _token_database_core.insert_token because order does not matter for the occupant access. ---#
        insertion_result = self._team_stack.push(item=team)
        
        # Handle the case that the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TeamDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {TeamDatabaseException.ERROR_CODE}",
                    ex=insertion_result.exception
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: TeamContext) -> SearchResult[List[Team]]:
        """
        # ACTION:
            1.  Get the result of calling _token_database_core.delete_token_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   TeamDatabaseException
        """
        method = "TokenDatabase.search"
        
        # --- Handoff the search responsibility to _token_database_core. ---#
        search_result = self._team_stack.context_service.finder.find(context=context)
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TeamDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {TeamDatabaseException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
    
    

        
