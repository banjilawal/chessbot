# src/chess/team/service.py

"""
Module: chess.team.service
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""

from typing import List, cast

from chess.schema import SchemaService
from chess.token import Token, TokenContext, TokenService
from chess.system import EntityService, LoggingLevelRouter, SearchResult, id_emitter
from chess.team import (
    HostageRelationAnalyzer, RosterRelationAnalyzer, Team, TeamBuilder, TeamServiceException, TeamValidator,
    TokenLocation
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
    _hostage_relation_analyzer: HostageRelationAnalyzer
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: TeamBuilder = TeamBuilder(),
            validator: TeamValidator = TeamValidator(),
            schema_service: SchemaService = SchemaService(),
            roster_relation_analyzer: RosterRelationAnalyzer = RosterRelationAnalyzer(),
            hostage_relation_analyzer: HostageRelationAnalyzer = HostageRelationAnalyzer(),
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
        self._roster_relation_analyzer = roster_relation_analyzer
        self._hostage_relation_analyzer = hostage_relation_analyzer
    
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
    def hostage_relation_analyzer(self) -> HostageRelationAnalyzer:
        return self._hostage_relation_analyzer
    
    @property
    def schema_service(self) -> SchemaService:
        return self._schema_service
    
    @LoggingLevelRouter.monitor
    def search_team_for_token(
            self,
            team: Team,
            piece: Token,
            piece_service: TokenService = TokenService(),
    ) -> SearchResult[List[(Token, TokenLocation)]]:
        """
        This is only going to be used in Arenas where it might be necessary to check if a captured piece has
        been properly registered with the enemy. I probably won't need it.
        """
        method = "TeamService.search_team_for_token"
        
        # Validate the team and handle the failure case.
        team_validation = self.validator.validate(candidate=team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        # Validate the piece and handle the failure case.
        piece_validation = piece_service.validator.validate(piece)
        if piece_validation.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=piece_validation.exception
                )
            )
        # create the container for storing all the search hits.
        matches: List[(Token, TokenLocation)]
        
        # Process tokens on the roster first.
        roster_search = team.roster.search(context=TokenContext(id=piece.id))
        if roster_search.is_failure:
            # If roster_search fails send the exception chain.
            return SearchResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=roster_search.exception
                )
            )
        # Go through the roster hits, tag their locations and append to matches.
        if roster_search.is_success:
            for token in roster_search.payload:
                matches.append((token, TokenLocation.ROSTER))
                
        # Process the hostages
        hostage_search = team.hostages.search(context=TokenContext(id=piece.id))
        if hostage_search.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=hostage_search.exception
                )
            )
        # Tag and append hits from the hostages list.
        if hostage_search.is_success:
            for token in hostage_search.payload:
                matches.append((token, TokenLocation.HOSTAGES))
        # Send the tagged matches.
        return SearchResult.success(matches)
        
            
        

    

        
