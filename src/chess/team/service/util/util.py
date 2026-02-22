# src/chess/team/service/util/util.py

"""
Module: chess.team.service.util.util
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy

from chess.formation import FormationKey, FormationService
from chess.rank import RankService
from chess.system import IdFactory, IdentityService, UpdateResult
from chess.team import FillingTeamRosterException, RosterRelationAnalyzer, Team, TeamValidator


class TeamRosterUtil:
    
    _rank_service: RankService
    _identity_service: IdentityService
    _formation_service: FormationService
    _roster_relation_analyzer: RosterRelationAnalyzer
    
    def __init__(
            self,
            rank_service: RankService = RankService(),
            identity_service: IdentityService = IdentityService(),
            formation_service: FormationService = FormationService(),
            roster_relation_analyzer: RosterRelationAnalyzer = RosterRelationAnalyzer(),
    ):
        self._rank_service = rank_service
        self._identity_service = identity_service
        self._formation_service = formation_service
        self._roster_relation_analyzer = roster_relation_analyzer
        
    @property
    def rank_service(self) -> RankService:
        return self._rank_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
        
    @property
    def roster_relation_analyzer(self) -> RosterRelationAnalyzer:
        return self._roster_relation_analyzer
       
    def fill(
            self,
            team: Team,
            team_validator: TeamValidator = TeamValidator(),
    ) -> UpdateResult[Team]:
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
        
        pre_update_team = deepcopy(team)
        # Handle the case that the team is not certified safe.
        team_validation = team_validator.validate(candidate=team)
        if team_validation.is_failure:
            # Return exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_team,
                exception=FillingTeamRosterException(
                    message=f"{method}: {FillingTeamRosterException.ERROR_CODE}",
                    ex=team_validation.exception
                )
            )
        # --- Get the formations for the team by its color. ---#
        formation_lookup_result = self._formation_service.lookup_formation(
            super_key=FormationKey(color=team.schema.color)
        )
        
        # Handle the case that the formation lookup was not completed.
        if formation_lookup_result.is_failure:
            # Return exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_team,
                exception=FillingTeamRosterException(
                    message=f"{method}: {FillingTeamRosterException.ERROR_CODE}",
                    ex=formation_lookup_result.exception
                )
            )

        # --- Iterate through each formation to get each occupant's build params. ---#
        for formation in formation_lookup_result.payload:
            
            # Build the token.
            token_build_result = team.roster.integrity_service.builder.build(
                owner=team,
                id=IdFactory.next_id(class_name="Token"),
                formation=formation,
                team_validator=team_validator,
                rank_service=self._rank_service,
                identity_service=self._identity_service,
                formation_service=self._formation_service,
            )
            # Handle the case that the occupant does not get built.
            if token_build_result.is_failure:
                # Return exception chain on failure.
                return UpdateResult.update_failure(
                    original=pre_update_team,
                    exception=FillingTeamRosterException(
                        message=f"{method}: {FillingTeamRosterException.ERROR_CODE}",
                        ex=token_build_result.exception
                    )
                )
            # --- The factory returns only instances of concrete tokens so don't cast during the insert.---#
            insertion_result = team.roster.insert(token=token_build_result.payload)
            
            # Handle the case that the insertion was not completed.
            if insertion_result.is_failure:
                # Return exception chain on failure.
                return UpdateResult.update_failure(
                    original=pre_update_team,
                    exception=FillingTeamRosterException(
                        message=f"{method}: {FillingTeamRosterException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
        # --- Return the success result when the look finishes. ---#
        return UpdateResult.update_success(original=pre_update_team, updated=team)



