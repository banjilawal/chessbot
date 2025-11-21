# src/agent/search/context/collision.py

"""
Module: chess.agent.search.context.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from chess.system import (
     NullException, BuildFailedException, SearchContextException, ValidationException,
     NoBuildOptionSelectedException, BuildOptionSelectionTooLargeException,
)

__all__ = [
    "TeamSearchContextException",
    
# ========================= AGENT_TEAM_SEARCH_CONTEXT EXCEPTIONS =========================#
    "NullTeamSearchContextException",
    
# ========================= TEAM_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
    "InvalidTeamSearchContextException",
    "NoTeamSearchOptionSelectedException",
    "MoreThanOneTeamSearchOptionPickedException",
    
# ========================= TEAM_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
    "TeamSearchContextBuildFailedException",
]


class TeamSearchContextException(SearchContextException):
    """
    Super class of exceptions raised by TeamSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "TEAM_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext raised an exception."


#========================= NULL_TEAM_SEARCH_CONTEXT EXCEPTIONS =========================#
class NullTeamSearchContextException(TeamSearchContextException, NullException):
    """Raised if an entity, method, or operation requires TeamSearchContext but gets null instead."""
    ERROR_CODE = "NULL_TEAM_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext cannot be null"


#========================= TEAM_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
class InvalidTeamSearchContextException(
    TeamSearchContextException,
    ValidationException
):
    """Catchall Exception for TeamSearchContext when a validation candidate fails a sanity check."""
    ERROR_CODE = " TEAM_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext validation failed."


class NoTeamSearchOptionSelectedException(
    TeamSearchContextException,
    NoBuildOptionSelectedException
):
    """"""
    ERROR_CODE = "NO_TEAM_SEARCH_OPTION_SELECTED_ERROR"
    DEFAULT_MESSAGE = "None of the TeamSearchContext options wre selected. An option must be picked."


class MoreThanOneTeamSearchOptionPickedException(
    TeamSearchContextException,
    BuildOptionSelectionTooLargeException
):
    """"""
    ERROR_CODE = "TOO_MANY_TEAM_SEARCH_OPTIONS_ERROR"
    DEFAULT_MESSAGE = "Only one TeamSearchContext option can be selected."


#=========================AGENT_TEAM_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
class TeamSearchContextBuildFailedException(TeamSearchContextException, BuildFailedException):
    """
    Catchall Exception for TeamSearchContextBuilder when it encounters an error building
    a TeamSearchContext.
    """
    ERROR_CODE = "EAM_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext build failed."