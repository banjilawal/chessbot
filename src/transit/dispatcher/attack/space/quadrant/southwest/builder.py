# src/transit/dispatcher/attack/space/quadrant/southwest/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.space.quadrant.southwest.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import SouthwestQuadrantBlueprint
from transit.dispatcher.attack import QuadrantAttack
from err import SouthwestQuadrantAttackException
from artifcat import AttackResult, MethodResultType
from surface.space import SouthwestQuadrant
from operation.toolkit import SouthwestQuadrantAttackToolkit
from util import LoggingLevelRouter


class SouthwestQuadrantAttack(QuadrantAttack[SouthwestQuadrant]):
    """
    Role:
        - Attack
        - Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            attack_toolkit: Optional[SouthwestQuadrantAttackToolkit]

    Provides:
        -   def execute(origin: Vector) -> AttackResult[EastAxis]

    Super Class:
        QuadrantAttack
    """
    def __init__(
            self, 
            attack_toolkit: Optional[SouthwestQuadrantAttackToolkit] | 
                             None = SouthwestQuadrantAttackToolkit()
    ):
        """
        Args:
            attack_toolkit: Optional[SouthwestQuadrantAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: SouthwestQuadrantBlueprint
    ) -> AttackResult[SouthwestQuadrant]:
        """
        Attack a safe SouthwestQuadrant.

        Action:
            1.  Send an exception chain in the AttackResult if either
                    - The blueprint is flagged unsafe.
                    - The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a SouthwestQuadrant then,
                send in the success result,
        Args:
            blueprint: SouthwestQuadrantBlueprint
        Returns:
            AttackResult[SouthwestQuadrant]
        Raises:
            SouthwestQuadrantAttackException
        """
        method = f"{self.__class__.__name__}.attack"
        
        # Handle the case that the blueprint is not certified safe.
        validation = self.attack_toolkit.root_certifier.execute(
            job=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SouthwestQuadrantAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthwestQuadrantAttackException.MSG,
                    err_code=SouthwestQuadrantAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.attack_toolkit.assembler.execute(
            request=cast(SouthwestQuadrantBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SouthwestQuadrantAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthwestQuadrantAttackException.MSG,
                    err_code=SouthwestQuadrantAttackException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ATTACK_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(cast(SouthwestQuadrant, assembly.payload))