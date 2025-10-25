# src/chess/piece/travel/attack/transaction/transaction.py

"""
Module: chess.piece.travel.attack.transaction.transaction
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from typing import cast

from chess.piece import (
    AttackEvent, AttackEventValidator, OccupationTransaction, TravelTransaction, FailedEnemyRemovalFromSquareRolledBackException,
    FailedRemovalFromRosterRolledBackException, FailedSettingActorAsEnemyCaptorRolledBackException, OccupationEvent,
    FailedHostageAdditionRolledBackException, FailedRemovalFromBoardRolledBackException
)
from chess.piece.travel.check.transaction import
from chess.system import LoggingLevelRouter, TransactionResult, id_emitter
from chess.team import RemoveTeamMemberRolledBackException


class AttackTransaction(TravelTransaction[AttackEvent]):
    
    def __init__(self, event: AttackEvent):
        super().__init__(event)
    
    @LoggingLevelRouter.monitor
    def execute(self) -> TransactionResult:
        """"""
        method = "AttackTransaction.execute"
        
        try:
            event_validation = AttackEventValidator.validate(self.event)
            if event_validation.is_failure():
                return TransactionResult.errored(event_update=self.event, exception=event_validation.exception)
            
            # Set checkpoint 0
            event = cast(AttackEvent, event_validation.payload)
            
            # Set checkpoint 1.
            event.enemy_combatant.captor = event.actor
            
            # Evaluate checkpoint 1 success condition.
            if event.enemy_combatant.captor != event.actor:
                # Rollback all changes in reverse order to checkpoint 0
                event.enemy_combatant.captor = None
                
                # Send the error and last checkpoint in the result on failure.
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedSettingActorAsEnemyCaptorRolledBackException(
                        f"{method}: {FailedSettingActorAsEnemyCaptorRolledBackException.DEFAULT_MESSAGE}"
                    )
                )
            
            # Set checkpoint 2.
            event.enemy_combatant.team.roster.remove(event.enemy_combatant)
            
            # Evaluate checkpoint 2 success condition.
            if event.enemy_combatant in event.enemy_combatant.team.roster:
                event.enemy_combatant.captor = None
                
                # Send the error and last checkpoint in the result on failure.
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedRemovalFromRosterRolledBackException(
                        f"{method}: {FailedRemovalFromRosterRolledBackException.DEFAULT_MESSAGE}"
                    )
                )
            
            event.actor.team.hostages.append(event.enemy_combatant)
            if event.enemy_combatant not in event.actor.team.hostages:
                # Rollback all changes in reverse order
                event.enemy_combatant.team.roster.append(event.enemy_combatant)
                event.enemy_combatant.captor = None
                
                # Send the error and last checkpoint in the result
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedHostageAdditionRolledBackException(
                        f"{method}: {FailedHostageAdditionRolledBackException.DEFAULT_MESSAGE}"
                    )
                )
            
            event.enemy_square.occupant = None
            if event.enemy_square.occupant == event.enemy_combatant:
                # Rollback all changes in reverse order
                event.actor.team.hostages.remove(event.enemy_combatant)
                event.enemy_combatant.team.roster.append(event.enemy_combatant)
                event.enemy_combatant.captor = None
                
                # Send the error and last checkpoint in the result
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedEnemyRemovalFromSquareRolledBackException(
                        f"{method}: {FailedEnemyRemovalFromSquareRolledBackException.DEFAULT_MESSAGE}"
                    )
                )
            
            event.execution_environment.pieces.remove(event.enemy_combatant)
            if event.enemy_combatant in event.execution_environment.pieces:
                # Rollback all changes in reverse order
                event.actor.team.hostages.remove(event.enemy_combatant)
                event.enemy_combatant.team.roster.append(event.enemy_combatant)
                event.enemy_combatant.captor = None
                
                # Send the error and last checkpoint in the result
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedRemovalFromBoardRolledBackException(
                        f"{method}: {FailedRemovalFromBoardRolledBackException.DEFAULT_MESSAGE}"
                    )
                )
            
            occupation_event = OccupationEvent(
                parent=event,
                actor=event.actor,
                id=id_emitter.event_id,
                actor_square=event.actor_square,
                destination_square=event.enemy_square,
                execution_environment=event.execution_environment
            )
            
            return OccupationTransaction(event=occupation_event).execute()
        except Exception as e:
            return TransactionResult.errored(event_update=self.event, exception=e)