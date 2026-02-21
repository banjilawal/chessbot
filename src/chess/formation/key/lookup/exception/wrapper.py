# src/chess/formation/lookup/exception/wrapper.py

"""
Module: chess.formation.lookup.exception.wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import FormationException
from chess.system import LookupFailedException

__all__ = [
    # ======================# FORMATION_LOOKUP_WRAPPER EXCEPTION #======================#
    "FormationLookupFailedException",
]


# ======================# FORMATION_LOOKUP_WRAPPER EXCEPTION #======================#
class FormationLookupFailedException(FormationException, LookupFailedException):
    """
    # ROLE: WrapperException, Encapsulation

    # RESPONSIBILITIES:
    1.  If a Formation lookup runs into an error a debug exception is created and encapsulated in a
        FormationLookupFailedException creating an exception chain which is sent to the caller in a
        SearchResult.
    2.  The FormationLookupFailedException chain is useful for tracing a wrapper to its source.

    # PARENT:
        *   FormationValidationException
        *   LookupServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_LOOKUP_WRAPPER"
    DEFAULT_MESSAGE = "Formation lookup failed."

