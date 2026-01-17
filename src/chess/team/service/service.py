# src/chess/team/service.py

"""
Module: chess.team.service
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.schema import SchemaService
from chess.rank import Rank, RankService
from chess.system import (
    CalculationResult, EntityService, IdentityService, InsertionResult, LoggingLevelRouter,
    SearchResult, id_emitter
)
from chess.team import (
    AddingRosterMemberFailedException, EnemyCannotJoinRosterException, HostageRelationAnalyzer, RosterRelationAnalyzer,
    Team, TeamBuilder,
    TeamRankQuotaFullException, TeamSearchFailedException, TeamServiceException, TeamValidator, TokenLocation,
    ZeroTeamContextFlagsException
)
from chess.token import (
    AddingDuplicateTokenException, CombatantToken, Token, TokenContext, TokenService,
    TokenServiceCapacityException
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
        self._schema_service = schema_service
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
    def search_team_roster(
            self,
            team: Team,
            id: Optional[int] = None,
            designation: Optional[str] = None,
            identity_service: IdentityService = IdentityService(),
    ) -> SearchResult[List[Token]]:
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
                    ex=TeamSearchFailedException(
                        message=f"{method}: {TeamSearchFailedException.DEFAULT_MESSAGE}",
                        ex=team_validation.exception
                    )
                )
            )
        # --- Run the search on the roster. ---#
        search_result = team.roster.search(id=id, designation=designation, identity_service=identity_service)
        
        # Handle the case that the search did not complete.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=TeamSearchFailedException(
                        message=f"{method}: {TeamSearchFailedException.DEFAULT_MESSAGE}",
                        ex=search_result.exception
                    )
                )
            )
        
    
    def add_roster_member(self, team: Team, piece: Token) -> InsertionResult[Token]:
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
            *   InsertionResult[token] containing either:
                    - On failure: Exception
                    - On success: Token
        # RAISES:
            *   TeamServiceException
        """
        method = "TeamService.add_roster_team_member"
        
        # --- The relation analyzer validates its candidates. This has to be done before running further tests. ---#
        relation_analysis = self._roster_relation_analyzer.analyze(
            candidate_primary=team,
            candidadate_satellite=piece
        )
        
        # Handle the case that the relation_analysis was not completed.
        if relation_analysis.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=relation_analysis.exception
                    )
                )
            )
        # Handle the case that the piece belongs to a different team.
        if relation_analysis.does_not_exist:
            # Return exception chain on failure.
            return InsertionResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=AddingRosterMemberFailedException(
                        message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                        ex=EnemyCannotJoinRosterException(
                            f"{method}: {EnemyCannotJoinRosterException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the piece is already registered with the team.
        if relation_analysis.fully_exists:
            # Return exception chain on failure.
            return InsertionResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=AddingRosterMemberFailedException(
                        message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                        ex=AddingDuplicateTokenException(
                            f"{method}: {AddingDuplicateTokenException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Would have liked to check roster capacity first, but that requires validating the team. ---#
        if team.roster.members.is_full:
            # Return exception chain on failure.
            return InsertionResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=AddingRosterMemberFailedException(
                        message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                        ex=TokenServiceCapacityException(
                            f"{method}: {TokenServiceCapacityException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Find out if there is an openin for the token's rank on the roster. ---#
        boolean_result = team.roster.members.rank_has_openings(piece.rank)
        
        # Handle the case that the rank_has_openings failed test failed.
        if boolean_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=AddingRosterMemberFailedException(
                        message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                        ex=boolean_result.exception
                    )
                )
            )
        # Handle the case that the roster has no openings for the rank.
        if not cast(bool, boolean_result.payload):
            # Return exception chain on failure.
            return InsertionResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=AddingRosterMemberFailedException(
                        message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                        ex=TeamRankQuotaFullException(f"{method}: {TeamRankQuotaFullException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # --- Run the insertion operation on the DataService. ---#
        insertion_result = team.roster.members.add_unique_token(piece)
        
        # Handle the case that the insertion was not completed.
        if insertion_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                TeamServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TeamServiceException.ERROR_CODE}",
                    ex=AddingRosterMemberFailedException(
                        message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # On success, directly forward result to the caller.
        return insertion_result
    
    def calculate_remaining_rank_quota(
            self,
            team: Team,
            rank: Rank,
            rank_service: RankService = RankService()
    ) -> CalculationResult[int]:
        """
        # ACTION:
            1.  If either the team or rank are not certified send the exception in the CalculationResult.
                Else, search the roster by the rank.
            2.  If the search did not complete send the exception in the CalculationResult.
            3.  Calculate rank.team_quota - len(matches) and send in the CalculationResult.
        # PARAMETERS:
            *   team (Team)
            *   rank (Rank)
            *   rank_service (RankService)
        # RETURN:
            *   CalculationReport[Rank, int] containing either:
                - On failure: Exception
                - On success: (Rank, int) tuple
        # RAISES:
            *   TeamServiceException
        """
        method = "TeamService.calculate_remaining_rank_quota"
        
        # Handle the case that the team is not certified safe.
        team_validation = self.validator.validate(team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return CalculationResult.failure(
                TeamServiceException(
                    message=f"{method}: {TeamServiceException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        # Handle the case that the rank is not certified safe
        rank_validation = rank_service.validator.validate(rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return CalculationResult.failure(
                TeamServiceException(
                    message=f"{method}: {TeamServiceException.ERROR_CODE}",
                    ex=rank_validation.exception
                )
            )
        # --- Search the team's roster for tokens that share the persona's rank. ---#
        search_result = team.roster.search(context=TokenContext(rank=rank))
        
        # Handle the case that the search did not succeed
        if search_result.is_failure:
            # Return the exception chain on failure.
            return CalculationResult.failure(
                TeamServiceException(
                    message=f"{method}: {TeamServiceException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # Calculate how many slots are available for the rank and send in the CalculationResult.
        open_slots = rank.team_quota - len(search_result.payload)
        return CalculationResult(open_slots)

        
