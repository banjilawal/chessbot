# src/agent/search/context/exception.py

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
    "AgentTeamSearchContextException",
    
# ========================= NULLAGENT_TEAM_SEARCH_CONTEXT EXCEPTIONS =========================#
    "NullAgentTeamSearchContextException",
    
# =========================AGENT_TEAM_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
    "InvalidAgentTeamSearchContextException",
    "NoAgentTeamSearchOptionSelectedException",
    "MoreThanOneAgentTeamSearchOptionPickedException",
    
# =========================AGENT_TEAM_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
    "AgentTeamSearchContextBuildFailedException",
]


class AgentTeamSearchContextException(SearchContextException):
    """
    Super class of exceptions raised by AgentTeamSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "AgentTeamSearchContext raised an exception."


#========================= NULLAGENT_TEAM_SEARCH_CONTEXT EXCEPTIONS =========================#
class NullAgentTeamSearchContextException(AgentTeamSearchContextException, NullException):
    """Raised if an entity, method, or operation requires AgentTeamSearchContext but gets null instead."""
    ERROR_CODE = "NULL_AGENT_TEAM_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "AgentTeamSearchContext cannot be null"


#=========================AGENT_TEAM_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
class InvalidAgentTeamSearchContextException(
    AgentTeamSearchContextException,
    ValidationException
):
    """Catchall Exception for AgentTeamSearchContextValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "AGENT_TEAM_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "AgentTeamSearchContext validation failed."


class NoAgentTeamSearchOptionSelectedException(
    AgentTeamSearchContextException,
    NoBuildOptionSelectedException
):
    """"""
    ERROR_CODE = "NO_AGENT_TEAM_SEARCH_OPTION_SELECTED_ERROR"
    DEFAULT_MESSAGE = "None of the AgentTeamSearchContext options wre selected. An option must be picked."


class MoreThanOneAgentTeamSearchOptionPickedException(
    AgentTeamSearchContextException,
    BuildOptionSelectionTooLargeException
):
    """"""
    ERROR_CODE = "TOO_MANY_AGENT_TEAM_SEARCH_OPTIONS_ERROR"
    DEFAULT_MESSAGE = "Only one AgentTeamSearchContext option can be selected."


#=========================AGENT_TEAM_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
class AgentTeamSearchContextBuildFailedException(AgentTeamSearchContextException, BuildFailedException):
    """
    Catchall Exception for AgentTeamSearchContextBuilder when it encounters an error building
    a AgentTeamSearchContext.
    """
    ERROR_CODE = "AGENT_TEAM_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "AgentTeamSearchContext build failed."