# src/chess/prisoner/exception.py

"""
Module: chess.prisoner.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# HOSTAGE_MANIFEST EXCEPTION #======================#
    "HostageManifestException",
]

# ======================# HOSTAGE_MANIFEST EXCEPTION #======================#
class HostageManifestException(ChessException):
    """
    # ROLE: Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Catchall for Hostage exceptions.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    None
  
    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_ERROR"
    DEFAULT_MESSAGE = "HostageManifest raised an exception."