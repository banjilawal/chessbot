# src/transit/dispatcher/attack/space/axis/east/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.space.axis.east.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.blueprint import EastAxisBlueprint
from transit.dispatcher.attack import AxisAttack
from err import EastAxisAttackException
from artifcat import AttackResult, MethodResultType
from surface.space import EastAxis
from operation.toolkit import EastAxisAttackToolkit
from util import LoggingLevelRouter


class EastAxisAttack(AxisAttack[EastAxis]):
    """
    Role:
        - Attack
        - Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            attack_toolkit: Optional[EastAxisAttackToolkit]

    Provides:
        -   def execute(origin: Vector) -> AttackResult[EastAxis]

    Super Class:
        AxisAttack
    """
    def __init__(
            self, 
            attack_toolkit: Optional[EastAxisAttackToolkit] |  None = None
    ):
        """
        Args:
            attack_toolkit: Optional[EastAxisAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit or EastAxisAttackToolkit())
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: EastAxisBlueprint
    ) -> AttackResult[EastAxis]:
        """
        Attack a safe EastAxis.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The blueprint is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a EastAxis then,
                send in the success result,
        Args:
            blueprint: EastAxisBlueprint
        Returns:
            AttackResult[EastAxis]
        Raises:
            EastAxisAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        validation = self.attack_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                EastAxisAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EastAxisAttackException.MSG,
                    err_code=EastAxisAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            blueprint=cast(EastAxisBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                EastAxisAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EastAxisAttackException.MSG,
                    err_code=EastAxisAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(EastAxis, assembly.payload))