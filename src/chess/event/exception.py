"""
Module: chess.event.exception
Author: Banji Lawal
Created: 2025-10-01

# Purpose
Higher level exceptions raised by `Event` object and the `Transaction` classes managing `event` lifecycles.
Each Event and Transaction subclass has a corresponding Exception subclass, making debugging and maintenance
easier.

Contents:
    - `EventException:` Super class of all exceptions an event object raises.
    - `NullEventException:` Raised by methods, entities, and models that require an event but receive a null.
    - `InvalidEventException:` Super class of exceptions raised EventValidators raise if a client fails sanity checking.
    - `EventBuilderException:` Super class of exceptions raised when An EventBuilder runs into problems creating an event.
    - `TransactionException:` Super class of all exceptions a Transaction instances raise..

Notes:
    DO NOT USE THESE EXCEPTIONS DIRECTLY. Limited use in the finally statement of a try-except block.
"""

from chess.exception import ChessException, ValidationException, NullException, BuilderException

__all__ = [
    #=== AN EVENT EXCEPTIONS ===
    'EventException',
    'NullEventException',
    'InvalidEventException',
    'EventBuilderException',
    
    #=== TRANSACTION EXCEPTIONS ===
    'TransactionException'
]

#=== AN EVENT EXCEPTIONS ===
class EventException(ChessException):
    """
    Super class of all exceptions an event object raises. DO NOT USE DIRECTLY. Subclasses provide better
    debugging and maintenance support.

    Notes:
        Only use in the finally statement of a try-except block.
    """
    ERROR_CODE = "EVENT_ERROR"
    DEFAULT_MESSAGE = "Event raised an error."

class NullEventException(EventException, NullException):
    """
    Raised by methods, entities, and models that require an event but receive a null.
    """
    ERROR_CODE = "NULL_EVENT_ERROR"
    DEFAULT_MESSAGE = "Event cannot be null."

class InvalidEventException(EventException, ValidationException):
    """
    Super class of exceptions raised EventValidators raise if a client fails sanity checking. Each EventValidator
    subclass has a corresponding InvalidEventException subclass, making debugging and maintenance easier.

    Notes:
        Only use in the finally statement of a try-except block.
    """
    ERROR_CODE = "INVALID_EVENT_ERROR"
    DEFAULT_MESSAGE = "Event validation failed."

class EventBuilderException(EventException, BuilderException):
    """
    Super class of exceptions raised when An EventBuilder runs into problems creating an event. Each EventBuilder
    subclass has a corresponding InvalidEventException subclass, making debugging and maintenance easier.

    Notes:
        Only use in the finally statement of a try-except block.
    """
    ERROR_CODE = "EVENT_BUILDER_ERROR"
    DEFAULT_MESSAGE = "EventBuilder validation failed."


 #=== TRANSACTION EXCEPTIONS ===

class TransactionException(ChessException):
    """
    Super class of all exceptions a Transaction instances raise. Do not use directly. Subclasses
    give details useful for debugging. Class exists primarily for catching all transaction exceptions.
    """
    ERROR_CODE = "TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "Transaction raised an error."
