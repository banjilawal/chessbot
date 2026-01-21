# src/chess/owner/finder/finder.py

"""
Module: chess.owner.cntext.finder.finder
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from typing import List

from chess.player.service.data.exception.null import AgentNullDatasetException
from chess.system import LoggingLevelRouter, SearchResult
from chess.agent import (
    PlayerAgent, AgentContext, AgentContextValidator, AgentVariety
)
from chess.system.data.operation import DataFinder
from chess.team import Team, TeamContext


class AgentFinder(DataFinder[PlayerAgent]):
    """
    # ROLE: AbstractSearcher

    # RESPONSIBILITIES:
    1.  Search Player collections for items which match the attribute target specified in the AgentContext parameter.
    2.  Safely forward any errors encountered during a search to the caller.

    # PARENT:
        *   AbstractSearcher

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See AbstractSearcher class for inherited attributes.
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            context: AgentContext,
            dataset: List[PlayerAgent],
            context_validator: AgentContextValidator = AgentContextValidator(),
    ) -> SearchResult[List[PlayerAgent]]:
        """
        # ACTION:
        1.  Verify the dataset is not null and contains only Player objects,
        2.  Use context_validator to certify the provided map.
        3.  Route to the appropriate finder-helper based on the attribute-value tuple which is enabled.
        4.  The finder-helper sends the SearchResult to the caller.

        # PARAMETERS:
            *   map: AgentContext
            *   dataset (List[Player])
            *   context_validator: AgentContextValidator

        # RETURNS:
        SearchResult[List[Player]] containing either:
            - On finding a match: List[Player] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # RAISES:
            *   TypeError
            *   AgentNullDatasetException
            *   AgentFinderException
        """
        method = "AgentFinder.find"
        try:
            # Don't want to run a search if the dataset is null.
            if dataset is None:
                return SearchResult.failure(
                    AgentNullDatasetException(f"{method}: {AgentNullDatasetException.DEFAULT_MESSAGE}")
                )
            # certify the map is safe.
            validation_result = context_validator.validate(context)
            if validation_result.is_failure:
                return SearchResult.failure(validation_result.exception)
            
            # After map is verified select the search method based on the which flag is enabled.
            
            # Entry point into searching by owner.id.
            if context.id is not None:
                return cls._find_by_id(dataset, context.id)
            # Entry point into searching by owner.designation.
            if context.name is not None:
                return cls._find_by_name(dataset, context.name)
            # Entry point into searching by owner's team.
            if context.team is not None:
                return cls._find_by_team(dataset, context.team)
            # Entry point into searching by AgentVariety (Human or Machine)
            if context.variety is not None:
                return cls._find_by_variety(dataset, context.variety)
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            SearchResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, dataset: [PlayerAgent], id: int) -> SearchResult[List[PlayerAgent]]:
        """
        # ACTION:
        1.  Get the PlayerAgents with the matching id.
        2.  If no hits are found an empty SearchResult is returned. For one or more unique hits a success
            SearchResult is returned. Otherwise, a SearchResult failure containing an exception is sent.
        3.  There really should only be one or none hits on a unique id but, the multiple hits error condition is
            relaxed for testing.

        # PARAMETERS:
            *   id (int)
            *   dataset (List[Player])

        # RETURNS:
        SearchResult[List[Player]] containing either:
            - On finding a match: List[Player] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # RAISES:
            *   AgentFinderException
        """
        method = "AgentFinder._find_by_id"
        try:
            # Get the list of agents with the same id.
            matches = [agent for agent in dataset if player.id == id]
            
            # An empty array means nothing was found.
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, dataset: [PlayerAgent], name: str) -> SearchResult[List[PlayerAgent]]:
        """
        # ACTION:
        1.  Get the PlayerAgents with the matching upper class name.
        2.  If no hits are found an empty SearchResult is returned. For one or more unique hits a success
            SearchResult is returned. Otherwise, a SearchResult failure containing an exception is sent.
        3.  There really should only be one or none hits on a unique id but, the multiple hits error condition is
            relaxed for testing.

        # PARAMETERS:
            *   name (str)
            *   dataset (List[Player])

        # RETURNS:
        SearchResult[List[Player]] containing either:
            - On finding a match: List[Player] in the payload.
            - On error: Exception , payload null
            - On no matches found: Exception null, payload null

        # RAISES:
            *   AgentFinderException
        """
        method = "AgentFinder._find_by_name"
        try:
            # Get the list of agents with the same name in upper case..
            matches = [agent for agent in dataset if player.name.upper() == name.upper()]
            
            # An empty array means nothing was found.
            if len(matches) == 0:
                return SearchResult.empty()
            # Relaxing the 0 <= match_count < 2 requirement for convenience. Will handle the
            # inconsistency later.
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_team(cls, dataset: [PlayerAgent], team: Team) -> SearchResult[List[PlayerAgent]]:
        """
        # ACTION:
        1.  Get the Player with the matching team.
        2.  If no match is found return an exception.
        3.  A team search should produce either no hits or one hit only.
        4.  Multiple unique agents in the result indicate that  a problem.

        # PARAMETERS:
            *   team (Team)
            *   dataset (List[Player])

        # RETURNS:
        SearchResult[List[Player]] containing either:
            - On success: List[owner] in the payload.
            - On failure: Exception.

        # RAISES:
            *   AgentFinderException
        """
        method = "AgentFinder._find_by_team"
        try:
            # Loop through the set and return the first owner who ran the team.
            # If more than one Player is returned there might be a problem.
            for agent in dataset:
                team_search = player.teams.search(context=TeamContext(id=team.id))
                if team_search.is_failure:
                    return SearchResult.failure(team_search.exception)
                # Put the first owner that matches inside a List then send the array inside a SearchResult.
                # The exhaustive search is just to make sure there are no duplicates.
                if team_search.is_success:
                    return SearchResult.success(payload=List[team_search.payload])
            return SearchResult.empty()
            
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_variety(cls, dataset: [PlayerAgent], variety) -> SearchResult[[PlayerAgent]]:
        """
        # ACTION:
        1.  Get the Agents whose subclass matches the AgentVariety
        2.  If no match is found return an exception.
        3.  A team search should produce either no hits or one hit only.
        4.  Multiple unique agents in the result indicate that  a problem.

        # PARAMETERS:
            *   team (Team)
            *   dataset (List[Player])

        # RETURNS:
        SearchResult[List[Player]] containing either:
            - On success: List[owner] in the payload.
            - On failure: Exception.

        # RAISES:
            *   AgentFinderException
        """
        method = "AgentFinder._find_by_name"
        try:
            matches = []
            # Use the variety to pick which concrete Player type needs to be found.
            matches = [agent for agent in dataset if isinstance(agent, AgentVariety.subclass_from_variety(variety))]
            if len(matches) == 0:
                return SearchResult.empty()
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
                
            # Finally, if some exception is not handled by the checks wrap it inside an SearchFailedException
            # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                SearchFailedException(ex=ex, message=f"{method}: {SearchFailedException.DEFAULT_MESSAGE}")
            )