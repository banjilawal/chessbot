# src/chess/system/err/registration.py

"""
Module: chess.system.err.registration
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system.err import ChessException


__all__ = [
# ======================# REGISTRATION EXCEPTION SUPER CLASS #======================#
    "RegistrationException",
]


# ======================# REGISTRATION EXCEPTION SUPER CLASS #======================#
class RegistrationException(ChessException):
    """Raised when Entity.owner == owner but the Owner does not find the item in its dataset."""
    ERROR_CODE = "NO_DATA_SET_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "The item is not found in its owner's dataset."
