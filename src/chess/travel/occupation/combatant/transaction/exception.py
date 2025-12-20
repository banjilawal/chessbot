# src/chess/owner/travel/occupation/combatant/transaction/collision.py

"""
Module: chess.owner.travel.occupation.combatant.transaction.exception
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from chess.piece import OccupationTransactionException, TravelTransactionException
from chess.system import RollbackException

"""
=============================================================================================================#
==============COMBATANT_OCCUPATION_TRANSACTION EXCEPTION ARE ALWAYS ROLL_BACK_EXCEPTION SUBCLASSES=================#
=============================================================================================================#
"""

__all__ = [
    'CombatantOccupationTransactionException',
    'RolledBackCombatantOccupationTransactionException',
    'FailedDestinationSquareOccupationRolledBackException',
    'FailedActorSquareVacationRolledBackException',
    'FailedActorPositionUpdateRolledBackException',
]


class CombatantOccupationTransactionException(OccupationTransactionException):
    """"""
    ERROR_CODE = "COMBATANT_OCCUPATION_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "An rollback_exception was raised during an CombatantOccupationTransaction."


class RolledBackCombatantOccupationTransactionException(CombatantOccupationTransactionException, RollbackException):
    """"""
    ERROR_CODE = "COMBATANT_OCCUPATION_TRANSACTION_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "The notification failed when an error occurred. The notification was rolled back before raising this rollback_exception."
    )


class FailedDestinationSquareOccupationRolledBackException(RolledBackCombatantOccupationTransactionException):
    ERROR_CODE = "DESTINATION_SQUARE_OCCUPATION_FAILURE_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Destination_Square's occupant was not successfully updated to actor_piece. CombatantOccupationTransaction was rolled "
        "back before rollback_exception was raised."
    )


class FailedActorSquareVacationRolledBackException(RolledBackCombatantOccupationTransactionException):
    ERROR_CODE = "ACTOR_SQUARE_VACATION_FAILURE_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Actor_Square was not successfully emptied. CombatantOccupationTransaction was rolled back before rollback_exception was raised."
    )


class FailedActorPositionUpdateRolledBackException(RolledBackCombatantOccupationTransactionException):
    ERROR_CODE = "ACTOR_POSITION_UPDATE_FAILURE_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Actor.current_position was not successfully set to enemy_square's point. The CombatantOccupationTransaction"
        " was rolled back before rollback_exception was raised."
    )
