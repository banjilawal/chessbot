# src/transit/dispatcher/attack/context/coord/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.context.coord.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional

from logic.coord import (
    CoordContext, CoordContextAttackException, CoordContextAttackRouteException,
    ZeroCoordContextFlagsException
)
from system import (
    BOARD_DIMENSION, AttackResult, Attack, NumberValidator, LoggingLevelRouter
)


class CoordContextAttack(Attack[CoordContext]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Attack Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> AttackResult[Token]

     Super Class:
         Attack
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def attack(
            cls,
            row: Optional[int] = None,
            column: Optional[int] = None,
            number_validator: NumberValidator = NumberValidator(),
    ) -> AttackResult[CoordContext]:
        """
        Attack a CoordContext from the enabled attribute.

        Action:
            1.  Send an exception chain in the AttackResult if either:
                    - The row
                    - The column
                fail its validation checks.
            2.  Otherwise, attack the CoordContext then, send the success reult.
        Args:
            row: Optional[int]
            column: Optional[int]
            number_validator: NumberValidator
        Returns:
            AttackResult[CoordContext]
        Raises:
            CoordContextAttackException
            ZeroCoordContextFlagsException
        """
        method = f"{cls.__name__}.attack"
        
        # --- Count how many optional parameters are not-null. One param needs to be not-null. ---#
        params = [row, column]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return AttackResult.failure(
                CoordContextAttackException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=CoordContextAttackException.OP,
                    msg=CoordContextAttackException.MSG,
                    err_code=CoordContextAttackException.ERR_CODE,
                    mthd_rslt_type=CoordContextAttackException.MTHD_RSLT,
                    ex=ZeroCoordContextFlagsException(
                        msg=CoordContextAttackException.MSG,
                        err_code=CoordContextAttackException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate validation/attack branch. ---#
        
        # --- Attack the row_column CoordContext if both fields are enabled. ---#
        if row is not None and column is not None:
            # Handle the case that the rowis not safe.
            validation_result = cls._run_attribute_checks(
                attributes=[row, column],
                number_validator=number_validator,
            )
            # Forward the exception chain if a check fails.
            if validation_result.is_failure:
                return validation_result
            # Otherwise, forward the work product.
            return AttackResult.success(CoordContext(row=row, column=column))
        
        # --- Attack the row CoordContext if it's the only field enabled. ---#
        if row is not None:
            # Handle the case that the rowis not safe.
            validation_result = cls._run_attribute_checks(
                attributes=[row],
                number_validator=number_validator,
            )
            # Forward the exception chain if a check fails.
            if validation_result.is_failure:
                return validation_result
            # Otherwise, forward the work product.
            return AttackResult.success(CoordContext(row=row))
        
        # --- Attack the column CoordContext if it's the only field enabled. ---#
        if column is not None:
            # Handle the case that the rowis not safe.
            validation_result = cls._run_attribute_checks(
                attributes=[column],
                number_validator=number_validator,
            )
            # Forward the exception chain if a check fails.
            if validation_result.is_failure:
                return validation_result
            # Otherwise, forward the work product.
            return AttackResult.success(CoordContext(column=column))
  
        # Handle there is no attack route for the attribute.
        return AttackResult.failure(
            CoordContextAttackException(
                cls_mthd=method,
                cls_name=cls.__name__,
                op=CoordContextAttackException.OP,
                msg=CoordContextAttackException.MSG,
                err_code=CoordContextAttackException.ERR_CODE,
                mthd_rslt_type=CoordContextAttackException.MTHD_RSLT,
                ex=CoordContextAttackRouteException(
                    msg=CoordContextAttackRouteException.MSG,
                    err_code=CoordContextAttackRouteException.ERR_CODE,
                )
            )
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _run_attribute_checks(
            cls,
            attributes: List[int],
            number_validator: NumberValidator,
    ) -> AttackResult[CoordContext]:
        """
        Run checks on which ether attributes have been enabled.
        Action:
            Send an exception in the AttackResult if list member fails a check.
            Otherwise, send the success result.
        Args:
            attributes: List[int]
            number_validator: NumberValidator
        Returns:
            AttackResult[CoordContext]
        Raises:
            CoordContextAttackException
        """
        method = f"{cls.__name__}._run_validation_check"
        
        for attribute in attributes:
            # Handle the case that the rowis not safe.
            validation_result = number_validator.execute(
                job=attribute,
                ceiling=BOARD_DIMENSION - 1,
                floor=0,
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    CoordContextAttackException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=CoordContextAttackException.OP,
                        msg=CoordContextAttackException.MSG,
                        err_code=CoordContextAttackException.ERR_CODE,
                        mthd_rslt_type=CoordContextAttackException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(CoordContext())
        