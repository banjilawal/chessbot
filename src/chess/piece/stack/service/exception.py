# src/chess/piece/stack/service/collision.py

"""
Module: chess.piece.stack.service.exception
Author: Banji Lawal
Created: 2025-11-18
version: 1.0.0
"""


from chess.system import ServiceException, ValidationException, NullException


__all__ = [
    "CoordStackServiceException",
    
    # ======================# NULL COORD_STACK_SERVICE EXCEPTIONS #======================#
    "NullCoordStackServiceException",
    
    # ======================# COORD_STACK_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidCoordStackServiceException",
    "CannotRunServiceWithoutCoordStackException",
    
    # ======================# COORD_STACK_SERVICE DATA OPERATIONS EXCEPTIONS #======================#
    "PoppingEmptyCoordStackException",
    "DoubleCoordPushException",
    "PushingNullException",
    "CannotUndoPreviousTurnException",
]


class CoordStackServiceException(ServiceException):
    """
    Super class for exceptions raised by CoordStackService objects. DO NOT USE DIRECTLY. Subclasses
    give more useful debugging messages.
    """
    ERROR_CODE = "COORD_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordStackService raised an exception."


# ======================# NULL COORD_STACK_SERVICE EXCEPTIONS #======================#
class NullCoordStackServiceException(CoordStackServiceException, NullException):
    """Raised if an entity, method, or operation requires CoordStackService but gets validation instead."""
    ERROR_CODE = "NULL_COORD_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordStackService cannot be validation."


# ======================# COORD_STACK_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidCoordStackServiceException(CoordStackServiceException, ValidationException):
    """Catchall Exception for CoordStackServiceValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "COORD_STACK_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CoordStackService validation failed."


class CannotRunServiceWithoutCoordStackException(CoordStackServiceException):
    """Raised if the service does not have a CoordStack."""
    ERROR_CODE = "NO_COORD_STACK_FOR_SERVICE_ERROR"
    DEFAULT_MESSAGE = (
        "The service does not have a CoordStack to manage. CoordStackService"
        " requires a CoordStack."
    )


# ======================# COORD_STACK_SERVICE DATA OPERATION EXCEPTIONS #======================#
class PoppingEmptyCoordStackException(CoordStackServiceException):
    """Raised when trying to pop from an empty CoordStackService."""
    ERROR_CODE = "POPPING_EMPTY_STACK_ERROR"
    DEFAULT_MESSAGE = "Cannot pop from an empty CoordStackService."


class DoubleCoordPushException(CoordStackServiceException):
    """Raised when trying to push the current_position onto the stack again."""
    ERROR_CODE = "DOUBLY_PSUHING_CURRENT_POSITION_ERROR"
    DEFAULT_MESSAGE = "The Coord is already at the top of the stack. It cannot be pushed twice."


class PushingNullException(CoordStackServiceException):
    """Raised when trying to push validation item to stack."""
    ERROR_CODE = "PUSHING_NULL_ERROR"
    DEFAULT_MESSAGE = "Cannot push validation item onto a CoordStackService."


class CannotUndoPreviousTurnException(CoordStackServiceException):
    """Only the current move can be undone."""
    ERROR_CODE = "UNDOING_PREVIOUS_TURN_ERROR"
    DEFAULT_MESSAGE = "Cannot undo a previous turn once it has been committed.."

