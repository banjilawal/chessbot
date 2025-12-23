# src/chess/system/err/relational/registration.py

"""
Module: chess.system.err.relational.registration
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""



__all__ = [
#======================# NO_REGISTRATION EXCEPTION #======================#
    "NoRegistrationException",
]

from chess.system import NoRelationshipException


# ======================# NO_REGISTRATION EXCEPTION #======================#
class NoRegistrationException(NoRelationshipException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the owning side of a one-to-many is broken. The many side knows its owner from its owner
        attribute. If the owner does not find the many_instance in its collection there item is not registered
        with the owner. Raised when Entity.owner == owner but the Owner does not find the item in its dataset.

    # PARENT:
        *   NoRelationshipException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_REGISTRATION EXCEPTION_ERROR"
    DEFAULT_MESSAGE = "The item is not registered in the owner's dataset."
