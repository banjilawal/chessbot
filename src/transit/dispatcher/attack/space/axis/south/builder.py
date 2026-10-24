# src/transit/dispatcher/attack/space/axis/south/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.space.axis.south.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import SouthAxisBlueprint
from transit.dispatcher.attack import AxisAttack
from err import SouthAxisAttackException
from artifcat import AttackResult, MethodResultType
from surface.space import SouthAxis
from operation.toolkit import SouthAxisAttackToolkit
from util import LoggingLevelRouter


class SouthAxisAttack(AxisAttack[SouthAxis]):
    """
    Role:
        - Attack
        - Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            attack_toolkit: Optional[SouthAxisAttackToolkit]

    Provides:
        -   def execute(origin: Vector) -> AttackResult[EastAxis]

    Super Class:
        AxisAttack
    """
    def __init__(
            self, 
            attack_toolkit: Optional[SouthAxisAttackToolkit] | 
                             None = SouthAxisAttackToolkit()
    ):
        """
        Args:
            attack_toolkit: Optional[SouthAxisAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: SouthAxisBlueprint
    ) -> AttackResult[SouthAxis]:
        """
        Attack a safe SouthAxis.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The blueprint is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a SouthAxis then,
                send in the success result,
        Args:
            blueprint: SouthAxisBlueprint
        Returns:
            AttackResult[SouthAxis]
        Raises:
            SouthAxisAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        validation = self.attack_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SouthAxisAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthAxisAttackException.MSG,
                    err_code=SouthAxisAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            blueprint=cast(SouthAxisBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SouthAxisAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthAxisAttackException.MSG,
                    err_code=SouthAxisAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(SouthAxis, assembly.payload))