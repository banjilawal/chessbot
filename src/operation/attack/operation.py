# src/operation/attack/operation.py

"""
Module: operation.attack.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from copy import deepcopy

from err import AttackDestinationEmptyException, AttackEventNullException, AttackException
from event import AttackEvent
from model import Hostage, SquareState
from operation import Maneuver
from report import AttackApproval, ManeuverApproval
from result import EventResult, MethodResultType
from util import IdFactory, LoggingLevelRouter
from validation import PrimingValidator


class Attack:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Square entry exception owner.
        2.  Preserve original and updated square data for rollbacks.
        3.  Ensure both the token and the squares are consistent throughout
            square entry lifecycle.

    Attributes:
    
    Provides:
        -   execute(
                    token: Token,
                    square: Square,
                    token_freedom_analyzer: TokenFreedomAnalyzer,
                    validation_primer: ValidationPrimer,
            ) -> EventResult:

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            report: AttackApproval,
            validation_primer: PrimingValidator | None = None,
    ) -> EventResult:
        """
        Action:
            1.  Send the original square along with an exception chain in the validation result if:
                    -   The square or token are insecure.
                    -   The token is disabled
                    -   The token belongs to a different board.
                    -   The new token is being deployed to the wrong square.
                    -   The square is already occupied.
                    -   The square accepts the token but the token cannot update its position.
            2.  Otherwise, each updates its state.
            3.  Send the success result.
        Args:
            report: AttackApproval
            validation_primer: ValidationPrimer
       Returns:
            EventResult
        Raises:
        """
        method = f"{cls.__class__.__name__}.execute"
        
        if validation_primer is None:
            validation_primer = PrimingValidator()
            
        # Handle the case that, the itinerary is not valid.
        validation_result = validation_primer.validate(
            candidate=report,
            target_type=AttackApproval,
            null_ex_cls=AttackEventNullException,
        )
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return EventResult.failure(
                AttackException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=AttackException.MSG,
                    err_code=AttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.EVENT_RESULT,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the destination is not empty.
        if report.target_square.is_empty:
            # Send the exception chain on failure.
            return EventResult.failure(
                AttackException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=AttackException.MSG,
                    err_code=AttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.EVENT_RESULT,
                    ex=AttackDestinationEmptyException(
                        msg=AttackDestinationEmptyException.MSG,
                        err_code=AttackDestinationEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Security tests are passed. Return the registration result to the caller. ---#
        hostage = cls._capture_enemy(report)

        departure_result = cls._depart(origin=report.origin,)
        maneuver_result = Maneuver.execute(
            ManeuverApproval(
                id=IdFactory.next_id("Maneuver"),
                origin=report.origin,
                recipient=report.recipient,
                destination=report.target_square,
            )
        )
        if maneuver_result.is_failure:
            return EventResult.failure(
                AttackException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=AttackException.MSG,
                    err_code=AttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.EVENT_RESULT,
                    ex=maneuver_result.exception,
                )
            )
        
        return EventResult.success(
            AttackEvent(
                id=IdFactory.next_id("AttackEvent"),
                attack_origin=report.origin,
                attacker=report.recipient,
                target_square=report.target_square,
                enemy_combatant=hostage.prisoner,
                child=maneuver_result.payload,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _capture_enemy(cls, report: AttackApproval) -> Hostage:
        """
        Puts the token into the square.

        Action:
            1.  Send the square and an exception chain in the UpdateResult if:
                    - Pushing the square's coord onto the token's schema fails.
            2.  Otherwise, after:
                    -   The square makes the token its occupant
                    -   The token updates its position
                    -   Each updates its state.
            3.  Send the success result.
        Args:
            traveller: Token
            destination: Square
        Returns:
            UpdateResult[Square]
        """
        method = f"{cls.__name__}._capture_enemy"
        
        report_copy = deepcopy(report)
        board = report.target_square.board
        hostage_db = board.hostage_database
        
        report.enemy_combatant.captor = report.recipient
        report.target_square.occupant = None
        report.target_square.state = SquareState.EMPTY
        
        # --- Forward the work product to the caller. ---#
        return Hostage(
            id=IdFactory.next_id("Hostage"),
            victor=report.recipient,
            prisoner=report.enemy_combatant,
            captured_square=report.target_square,
        )
