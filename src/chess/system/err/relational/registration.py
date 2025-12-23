# src/chess/system/err/registration.py

"""
Module: chess.system.err.registration
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import BiDirectionalException



__all__ = [
#======================# REGISTRATION EXCEPTION #======================#
    "RegistrationException",
]


#======================# REGISTRATION EXCEPTION #======================#
class RegistrationException(BiDirectionalException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an item has its owner set correctly but the item does not exist in the Owner's collection.
    2.  Indicate a bidirectional relationship is broken on the owning side
    3.  Raised when Entity.owner == owner but the Owner does not find the item in its dataset.

    # PARENT:
        *   NoBidirectionalRelationshipException

    # PROVIDES:
    RegistrationException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_DATASET_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "The item is not found in its owner's dataset."
