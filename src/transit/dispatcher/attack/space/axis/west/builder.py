# src/transit/dispatcher/attack/space/axis/west/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.space.axis.west.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.blueprint import WestAxisBlueprint
from transit.dispatcher.attack import AxisAttack
from err import WestAxisAttackException
from artifcat import AttackResult, MethodResultType
from surface.space import WestAxis
from operation.toolkit import WestAxisAttackToolkit
from util import LoggingLevelRouter


class WestAxisAttack(AxisAttack[WestAxis]):
    """
    Role:
        - Attack
        - Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            attack_toolkit: Optional[WestAxisAttackToolkit]

    Provides:
        -   def execute(origin: Vector) -> AttackResult[EastAxis]

    Super Class:
        AxisAttack
    """
    def __init__(
            self, 
            attack_toolkit: Optional[WestAxisAttackToolkit] | 
                             None = WestAxisAttackToolkit()
    ):
        """
        Args:
            attack_toolkit: Optional[WestAxisAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: WestAxisBlueprint
    ) -> AttackResult[WestAxis]:
        """
        Attack a safe WestAxis.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The blueprint is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a WestAxis then,
                send in the success result,
        Args:
            blueprint: WestAxisBlueprint
        Returns:
            AttackResult[WestAxis]
        Raises:
            WestAxisAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        validation = self.attack_toolkit.root_certifier.execute(
            item=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                WestAxisAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WestAxisAttackException.MSG,
                    err_code=WestAxisAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            blueprint=cast(WestAxisBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                WestAxisAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WestAxisAttackException.MSG,
                    err_code=WestAxisAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(WestAxis, assembly.payload))