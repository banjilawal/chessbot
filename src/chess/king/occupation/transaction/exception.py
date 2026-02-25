# src/chess/king/occupation/transaction/collision.py

"""
Module: `chess.king.occupation.transaction.exception`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.piece import TravelTransactionException
from chess.system import RollbackException

"""
=============================================================================================================#
==============OCCUPATION_TRANSACTION EXCEPTION ARE ALWAYS ROLL_BACK_EXCEPTION SUBCLASSES=================#
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
    ERR_CODE = "OCCUPATION_TRANSACTION_ERROR"
    MSG = "An rollback_exception was raised during an OccupationTransaction."


class RolledBackOccupationTransactionException(OccupationTransactionException, RollbackException):
    """"""
    ERR_CODE = "OCCUPATION_TRANSACTION_ERROR_ROLLED_BACK"
    MSG = (
        "The notification failed when an error occurred. The notification was rolled back before raising this rollback_exception."
    )


class FailedDestinationSquareOccupationRolledBackException(RolledBackOccupationTransactionException):
    ERR_CODE = "DESTINATION_SQUARE_OCCUPATION_FAILURE_ROLLED_BACK"
    MSG = (
        "Destination_Square's occupant was not successfully updated to actor_piece. OccupationTransaction was rolled "
        "back before rollback_exception was raised."
    )


class FailedActorSquareVacationRolledBackException(RolledBackOccupationTransactionException):
    ERR_CODE = "ACTOR_SQUARE_VACATION_FAILURE_ROLLED_BACK"
    MSG = (
        "Actor_Square was not successfully emptied. OccupationTransaction was rolled back before rollback_exception was raised."
    )


class FailedActorPositionUpdateRolledBackException(RolledBackOccupationTransactionException):
    ERR_CODE = "ACTOR_POSITION_UPDATE_FAILURE_ROLLED_BACK"
    MSG = (
        "Actor.current_position was not successfully set to enemy_square's point. The OccupationTransaction"
        " was rolled back before rollback_exception was raised."
    )
