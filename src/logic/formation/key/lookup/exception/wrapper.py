# src/logic/formation/lookup/exception/validator.py

"""
Module: logic.formation.lookup.exception.work
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from logic.formation import FormationException
from logic.system import LookupException

__all__ = [
    # ======================# FORMATION_LOOKUP_WORK EXCEPTION #======================#
    "FormationLookupFailedException",
]


# ======================# FORMATION_LOOKUP_WORK EXCEPTION #======================#
class FormationLookupFailedException(FormationException, LookupException):
    """
    Role:WorkException, Encapsulation

    Responsibilities:
    1.  If a Formation lookup runs into an error a debug exception is created and encapsulated in a
        FormationLookupFailedException creating an exception chain which is sent to the caller in a
        SearchResult.
    2.  The FormationLookupFailedException chain is useful for tracing a work to its source.

    Super Class:
        *   FormationValidationException
        *   LookupServiceException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "FORMATION_LOOKUP_WORK"
    MSG = "Formation lookup failed."

