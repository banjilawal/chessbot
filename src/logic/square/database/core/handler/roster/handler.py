# src/logic/square/database/core/handler/roster/handler.py

"""
Module: logic.square.database.core.handler.roster.handler
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy

from logic.square import (
    InterruptedRosterDeploymentException, RosterAlreadyDeployedException, Square, SquareStackRosterHandlerException,
    SquareStackService, UnderstrengthRosterDeploymentException,
)
from logic.team import Team, TeamService
from logic.token import Token, TokenContext, TokenNotFoundException
from logic.system import LoggingLevelRouter, SearchResult, UpdateResult

class SquareStackRosterHandler:
    """
    # ROLE: Handler. Utility, Transport, Utilities, Update Management,

    # RESPONSIBILITIES:
    1.  Transfers Team.roster members to their opening squares.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        Local:
        None

        Inherited:
        None

    # LOCAL METHODS:
        *   form_team(
                team: Team,
                square_stack: SquareStackService,
                team_service: TeamService = TeamService()
            ) -> UpdateResult[Team]

    # INHERITED METHODS:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def deploy_roster_on_stack(
            cls,
            team: Team,
            team_service: TeamService,
            square_stack: SquareStackService,
    ) -> UpdateResult[Team]:
        """
        # ACTION:
            The stack is also updated but team is not tied to the stack. Its easier to verify and not
            used anymore.
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
        Args:
            team: Team
            team_service: TeamService
            square_stack: SquareStackService
        Returns:
            UpdateResult[Team]
        Raises:
            TokenNotFoundException
            RosterAlreadyDeployedException
            SquareStackRosterHandlerException
            UnderstrengthRosterDeploymentException
            InterruptedRosterDeploymentException
        """
        method = "SquareStackRosterHandler.deploy_roster_on_stack"
        
        # Handle the case that, the team is not certified as safe.
        team_validation = team_service.validator.validate(candidate=team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackRosterHandlerException.MSG,
                    err_code=SquareStackRosterHandlerException.ERR_CODE,
                    ex=team_validation.exception
                )
            )
        # Handle the case that, the team has already been deployed
        if team.roster.is_deployed_on_board:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackRosterHandlerException.MSG,
                    err_code=SquareStackRosterHandlerException.ERR_CODE,
                    ex=RosterAlreadyDeployedException(
                        var="team.roster",
                        msg=RosterAlreadyDeployedException.MSG,
                        err_code=RosterAlreadyDeployedException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the team is not at full strength.
        if  0 < team.roster.size < Team.MAX_ROSTER_SIZE:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackRosterHandlerException.MSG,
                    err_code=SquareStackRosterHandlerException.ERR_CODE,
                    ex=UnderstrengthRosterDeploymentException(
                        var="team.roster",
                        msg=UnderstrengthRosterDeploymentException.MSG,
                        err_code=UnderstrengthRosterDeploymentException.ERR_CODE,
                    )
                )
            )
        # --- The validation checks were passed, make a deep copy of the team and run deployment steps ---#
        pre_deployment_team = deepcopy(team)
        
        deployment_count = 0
        for square in square_stack.items:
            token_search_result = cls._get_forming_token(
                team=team,
                square=square
            )
            # Handle the case that the token search is not successful.
            if token_search_result.is_failure:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=team,
                    exception=SquareStackRosterHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareStackRosterHandlerException.MSG,
                        err_code=SquareStackRosterHandlerException.ERR_CODE,
                        ex=token_search_result.exception
                    )
                )
            # --- Transfer the successfully found subject to its opening square. ---#
            team_update_result = cls._transfer_token_to_opening_square(
                team=team,
                opening_square=square,
                square_stack=square_stack,
                token=token_search_result.payload[0],
            )
            # Handle the case that the update is not completed.
            if team_update_result.is_failure:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=team,
                    exception=SquareStackRosterHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareStackRosterHandlerException.MSG,
                        err_code=SquareStackRosterHandlerException.ERR_CODE,
                        ex=team_update_result.exception
                    )
                )
            # --- Increment the deployment count. ---#
            deployment_count += 1
            
        # Handle the case that some roster members were not deployed.
        if deployment_count != Team.MAX_ROSTER_SIZE or not team.roster.is_empty:
            # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=SquareStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackRosterHandlerException.MSG,
                    err_code=SquareStackRosterHandlerException.ERR_CODE,
                    ex=InterruptedRosterDeploymentException(
                        var="team.roster",
                        msg=InterruptedRosterDeploymentException.MSG,
                        err_code=InterruptedRosterDeploymentException.ERR_CODE,
                    )
                )
            )
        # --- Send the success result to the caller. ---#
        return UpdateResult.update_success(original=pre_deployment_team, updated=team)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _get_forming_token(cls, team: Team, square: Square,) -> UpdateResult[Token]:
        method = "SquareStackRosterHandler._search_for_opening_square"
        
        pre_deployment_team = deepcopy(team)
        # Find the roster member's opening square.
        token_search_result = team.roster.search(context=TokenContext(opening_square=square.name))
        
        # Handle the case that, the search is not completed.
        if token_search_result.is_failure:
            # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_deployment_team,
                exception=SquareStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackRosterHandlerException.MSG,
                    err_code=SquareStackRosterHandlerException.ERR_CODE,
                    ex=token_search_result.exception
                )
            )
        # Handle the case that, the opening square is not found.
        if token_search_result.is_failure:
            # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_deployment_team,
                exception=SquareStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackRosterHandlerException.MSG,
                    err_code=SquareStackRosterHandlerException.ERR_CODE,
                    ex=TokenNotFoundException(
                        var="opening_square",
                        val=f"{square.name}",
                        msg=f"Token that deploys to square {square.name} not found.",
                        err_code=TokenNotFoundException.ERR_CODE,
                    )
                )
            )
        # --- Send the success result to the caller. ---#
        return SearchResult.success(token_search_result.payload,)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _transfer_token_to_opening_square(
            cls,
            team: Team,
            token: Token,
            opening_square: Square,
            square_stack: SquareStackService,
    ) -> UpdateResult[Square]:
        method = "SquareStackRosterHandler._transfer_token_to_opening_square"
    
        pre_deployment_team = deepcopy(team)
        # --- Handoff the square's occupation to the integrity service. ---#
        square_update_result = square_stack.integrity_service.occupy_stack_square(
            token=token,
            square=opening_square,
        )
        # Handle the case that, the occupation fails.
        if square_update_result.is_failure:
            # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_deployment_team,
                exception=SquareStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackRosterHandlerException.MSG,
                    err_code=SquareStackRosterHandlerException.ERR_CODE,
                    ex=square_update_result.exception
                )
            )
        # --- Send the success result to the caller. ---#
        return UpdateResult.update_success(original=pre_deployment_team, updated=team)