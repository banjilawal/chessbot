# src/logic/token/database/core/handler/roster/handler.py

"""
Module: logic.token.database.core.handler.roster.handler
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy

from logic.token import (
    InterruptedRosterDeploymentException, RosterAlreadyDeployedException, Token, TokenStackRosterHandlerException,
    TokenStackService, UnderstrengthRosterDeploymentException,
)
from logic.team import Team, TeamService
from logic.token import Token, TokenContext, TokenNotFoundException
from logic.system import LoggingLevelRouter, SearchResult, UpdateResult

class TokenStackRosterHandler:
    """
    # ROLE: Handler. Utility, Transport, Utilities, Update Management,

    # RESPONSIBILITIES:
    1.  Transfers Team.roster members to their opening tokens.

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
                token_stack: TokenStackService,
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
            token_stack: TokenStackService,
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
            4.  Iterate through the tokens in the stack and search the roster for tokens which open on the
                tokens. If any search fails send the exception chain and the pre-deployment team back.
            5.  For each successful search, handoff the token to the integrity service. If any occupation
                fails send the exception chain and the pre-deployment team back.
            6.  After the loop completes, if some tokens were not deployed, send the exception chain and
                the pre-deployment team back.
            7.  The update was successful send the pre-deployment team and updated teams back to the caller.
        Args:
            team: Team
            team_service: TeamService
            token_stack: TokenStackService
        Returns:
            UpdateResult[Team]
        Raises:
            TokenNotFoundException
            RosterAlreadyDeployedException
            TokenStackRosterHandlerException
            UnderstrengthRosterDeploymentException
            InterruptedRosterDeploymentException
        """
        method = "TokenStackRosterHandler.deploy_roster_on_stack"
        
        # Handle the case that, the team is not certified as safe.
        team_validation = team_service.validator.validate(candidate=team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=TokenStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackRosterHandlerException.MSG,
                    err_code=TokenStackRosterHandlerException.ERR_CODE,
                    ex=team_validation.exception
                )
            )
        # Handle the case that, the team has already been deployed
        if team.roster.is_deployed_on_board:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=team,
                exception=TokenStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackRosterHandlerException.MSG,
                    err_code=TokenStackRosterHandlerException.ERR_CODE,
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
                exception=TokenStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackRosterHandlerException.MSG,
                    err_code=TokenStackRosterHandlerException.ERR_CODE,
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
        for token in token_stack.items:
            token_search_result = cls._get_forming_token(
                team=team,
                token=token
            )
            # Handle the case that the token search is not successful.
            if token_search_result.is_failure:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=team,
                    exception=TokenStackRosterHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenStackRosterHandlerException.MSG,
                        err_code=TokenStackRosterHandlerException.ERR_CODE,
                        ex=token_search_result.exception
                    )
                )
            # --- Transfer the successfully found subject to its opening token. ---#
            team_update_result = cls._transfer_token_to_opening_token(
                team=team,
                opening_token=token,
                token_stack=token_stack,
                token=token_search_result.payload[0],
            )
            # Handle the case that the update is not completed.
            if team_update_result.is_failure:
                # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
                return UpdateResult.update_failure(
                    original=team,
                    exception=TokenStackRosterHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenStackRosterHandlerException.MSG,
                        err_code=TokenStackRosterHandlerException.ERR_CODE,
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
                exception=TokenStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackRosterHandlerException.MSG,
                    err_code=TokenStackRosterHandlerException.ERR_CODE,
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
    def _get_forming_token(cls, team: Team, token: Token,) -> UpdateResult[Token]:
        method = "TokenStackRosterHandler._search_for_opening_token"
        
        pre_deployment_team = deepcopy(team)
        # Find the roster member's opening token.
        token_search_result = team.roster.search(context=TokenContext(opening_token=token.name))
        
        # Handle the case that, the search is not completed.
        if token_search_result.is_failure:
            # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_deployment_team,
                exception=TokenStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackRosterHandlerException.MSG,
                    err_code=TokenStackRosterHandlerException.ERR_CODE,
                    ex=token_search_result.exception
                )
            )
        # Handle the case that, the opening token is not found.
        if token_search_result.is_failure:
            # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_deployment_team,
                exception=TokenStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackRosterHandlerException.MSG,
                    err_code=TokenStackRosterHandlerException.ERR_CODE,
                    ex=TokenNotFoundException(
                        var="opening_token",
                        val=f"{token.name}",
                        msg=f"Token that deploys to token {token.name} not found.",
                        err_code=TokenNotFoundException.ERR_CODE,
                    )
                )
            )
        # --- Send the success result to the caller. ---#
        return SearchResult.success(token_search_result.payload,)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _transfer_token_to_opening_token(
            cls,
            team: Team,
            token: Token,
            opening_token: Token,
            token_stack: TokenStackService,
    ) -> UpdateResult[Token]:
        method = "TokenStackRosterHandler._transfer_token_to_opening_token"
    
        pre_deployment_team = deepcopy(team)
        # --- Handoff the token's occupation to the integrity service. ---#
        token_update_result = token_stack.integrity_service.occupy_stack_token(
            token=token,
            token=opening_token,
        )
        # Handle the case that, the occupation fails.
        if token_update_result.is_failure:
            # Avoid an expensive rollback by sending the pre-deployment team and the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_deployment_team,
                exception=TokenStackRosterHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackRosterHandlerException.MSG,
                    err_code=TokenStackRosterHandlerException.ERR_CODE,
                    ex=token_update_result.exception
                )
            )
        # --- Send the success result to the caller. ---#
        return UpdateResult.update_success(original=pre_deployment_team, updated=team)