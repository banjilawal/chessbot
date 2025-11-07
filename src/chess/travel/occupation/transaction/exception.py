# src/chess/owner/travel/occupation/rollback_exception.py

"""
Module: `chess.owner.travel.occupation.rollback_exception`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.piece import TravelTransactionException
from chess.system import RollbackException

"""
=============================================================================================================#
==============OCCUPATION_TRANSACTION EXCEPTIONS ARE ALWAYS ROLL_BACK_EXCEPTION SUBCLASSES=================#
=============================================================================================================#
"""

__all__ = [
    'OccupationTransactionException',
    'RolledBackOccupationTransactionException',
    'FailedDestinationSquareOccupationRolledBackException',
    'FailedActorSquareVacationRolledBackException',
    'FailedActorPositionUpdateRolledBackException',
]


class OccupationTransactionException(TravelTransactionException):
    """"""
    ERROR_CODE = "OCCUPATION_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "An rollback_exception was raised during an OccupationTransaction."


class RolledBackOccupationTransactionException(OccupationTransactionException, RollbackException):
    """"""
    ERROR_CODE = "OCCUPATION_TRANSACTION_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "The notification failed when an error occurred. The notification was rolled back before raising this rollback_exception."
    )


class FailedDestinationSquareOccupationRolledBackException(RolledBackOccupationTransactionException):
    ERROR_CODE = "DESTINATION_SQUARE_OCCUPATION_FAILURE_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Destination_Square's occupant was not successfully updated to actor_piece. OccupationTransaction was rolled "
        "back before rollback_exception was raised."
    )


class FailedActorSquareVacationRolledBackException(RolledBackOccupationTransactionException):
    ERROR_CODE = "ACTOR_SQUARE_VACATION_FAILURE_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Actor_Square was not successfully emptied. OccupationTransaction was rolled back before rollback_exception was raised."
    )


class FailedActorPositionUpdateRolledBackException(RolledBackOccupationTransactionException):
    ERROR_CODE = "ACTOR_POSITION_UPDATE_FAILURE_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Actor.current_position was not successfully set to enemy_square's coord. The OccupationTransaction"
        " was rolled back before rollback_exception was raised."
    )
