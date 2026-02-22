# src/chess/square/database/core/util/occupation/roster/deployer.py

"""
Module: chess.square.database.core.util.occupation.roster.deployer
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy

from chess.token import TokenContext
from chess.team import Team, TeamService
from chess.system import LoggingLevelRouter, UpdateResult
from chess.square import (
    CannotDeployUnderStrengthTeamException, DeployingTeamRosterException, SquareStackService, SquareStackException,
    TeamAlreadyDeployedException, TeamPartiallyDeployedException
)

class RosterFormationCoordinator:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def form_team(
            cls,
            team: Team,
            sqsckuare_stack: SquareStackService,
            team_service: TeamService = TeamService(),
    ) -> UpdateResult[Team]:
        """
        # ACTION:
            1.  If the team fails its validation checks send the exception chain and team back in the
                UpdatedResult.
            2.  Iff the team has already been deployed or is at partial strength send the exception chain
                and team in the UpdatedResult.
            3.  Make a deep copy of the pre-deployment team.
                    *   The deep copy can be sent back instead of doing an expensive rollback.
                    *   If the update succeeds the client can use the pre-deployment copy for
                        verifying correctness.
            4.  Iterate through the squares in the stack and search the roster for tokens which open on the
                squares. If any search fails send the exception chain and the pre-deployment team back.
            5.  For each successful search, handoff the token to the integrity service. If any occupation
                fails send the exception chain and the pre-deployment team back.
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
                    message=f"{method}: {SquareStackException.ERROR_CODE}",
                    ex=DeployingTeamRosterException(
                        message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                        ex=team_validation.exception
                    )
                )
            )
        # Handle the case that the team has already been deployed
        if team.roster.is_deployed_on_board:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackException(
                    message=f"{method}: {SquareStackException.ERROR_CODE}",
                    ex=DeployingTeamRosterException(
                        message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                        ex=TeamAlreadyDeployedException(
                            f"{method}: {TeamAlreadyDeployedException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the team is not at full strength.
        if team.roster.size < Team.MAX_ROSTER_SIZE:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackException(
                    message=f"{method}: {SquareStackException.ERROR_CODE}",
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
        for square in square_stack.items:
            # Find the roster member's opening square.
            token_search_result = team.roster.search(context=TokenContext(opening_square=square))
            
            # Handle the case that the search is not completed.
            if token_search_result.is_failure:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=pre_deployment_team,
                    exception=SquareStackException(
                        message=f"{method}: {SquareStackException.ERROR_CODE}",
                        ex=DeployingTeamRosterException(
                            message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                            ex=token_search_result.exception
                        )
                    )
                )
            # --- Handoff the square's occupation to the integrity service. ---#
            square_update_result = square_stack.integrity_service.add_occupant(
                square=square,
                token=token_search_result.payload[0]
            )
            
            # Handle the case that the occupation fails.
            if square_update_result.is_failure:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=pre_deployment_team,
                    exception=SquareStackException(
                        message=f"{method}: {SquareStackException.ERROR_CODE}",
                        ex=DeployingTeamRosterException(
                            message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                            ex=square_update_result.exception
                        )
                    )
                )
        # --- After the deployment loop has finished perform clean up tasks.---#
        
        # Handle the case that at least one token was not deployed.
        if not team.roster.is_empty:
            # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_deployment_team,
                exception=SquareStackException(
                    message=f"{method}: {SquareStackException.ERROR_CODE}",
                    ex=DeployingTeamRosterException(
                        message=f"{method}: {DeployingTeamRosterException.ERROR_CODE}",
                        ex=TeamPartiallyDeployedException(
                            f"{method}: {TeamPartiallyDeployedException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        
        # --- Send the success result to the caller. ---#
        return UpdateResult.update_success(original=pre_deployment_team, updated=team)
