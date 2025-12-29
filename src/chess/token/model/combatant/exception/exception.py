# src/chess/token/combatant/exception/exception.py

"""
Module: chess.token.combatant.exception.exception
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""


from chess.token import TokenException
from chess.system import BuildFailedException, NullException,


__all__ = [
    #======================# COMBATANT_TOKEN EXCEPTION #======================#
    "CombatantTokenException",
    
    #======================# COMBATANT_TOKEN VALIDATION EXCEPTION #======================#
    "InvalidCombatantTokenException",
    "NullCombatantException",
    
    #======================# COMBATANT_TOKEN BUILD EXCEPTION #======================#
    "CombatantTokenBuildFailedException",
]


#======================# COMBATANT_TOKEN EXCEPTION #======================#
class CombatantTokenException(TokenException):
    """Super class for CombatantToken exception."""
    ERROR_CODE = "COMBATANT_TOKEN_ERROR"
    DEFAULT_MESSAGE = "CombatantToken raised an exception."


#======================# COMBATANT_TOKEN VALIDATION EXCEPTION #======================#
class InvalidCombatantTokenException(CombatantTokenException, ValidationException):
    """Raised by TokenValidator when a combatant candidate fails a sanity check."""
    ERROR_CODE = "COMBATANT_TOKEN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CombatantToken validation failed."


class NullCombatantException(CombatantTokenException, NullException):
    """Raised if an entity, method, or operation expects a CombatantToken but gets null instead."""
    ERROR_CODE = "NULL_COMBATANT_TOKEN_ERROR"
    DEFAULT_MESSAGE = "CombatantToken cannot be null."


#======================# COMBATANT_TOKEN BUILD EXCEPTION #======================#
class CombatantTokenBuildFailedException(CombatantTokenException, BuildFailedException):
    ERROR_CODE = "COMBATANT_TOKEN_BUILD_FAILED"
    DEFAULT_MESSAGE = "CombatantToken build failed."